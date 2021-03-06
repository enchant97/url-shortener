import logging

from quart import Quart, abort, jsonify, redirect, render_template, request
from tortoise.contrib.quart import register_tortoise

from .config import get_settings
from .database import crud, models
from .helpers import make_short_url, make_url_safe, short_id_to_url

app = Quart(__name__)


async def process_short_url(long_url) -> str:
    long_url = make_url_safe(long_url)
    short_url = await crud.get_url_by_url(long_url)
    if not short_url:
        short_url = make_short_url(long_url)
        valid_url = await crud.get_or_create_url(short_url, long_url)
        if valid_url is None:
            # somehow the hash is used in another url
            logging.error("hash was used in another url: %s", short_url)
            abort(500)
        short_url = short_id_to_url(short_url)
    else:
        short_url = short_id_to_url(short_url.short_id)
    return short_url


@app.route("/", methods=["GET", "POST"])
async def create():
    short_url = None
    if request.method == "POST":
        long_url = (await request.form)["url"]
        short_url = await process_short_url(long_url)
    return await render_template("create.html", short_url=short_url)


@app.route("/api/create", methods=["POST"])
async def create_api():
    try:
        json_data = await request.get_json(silent=True)
        long_url = json_data["url"]
        short_url = await process_short_url(long_url)
        return jsonify(short_url=short_url)
    except (TypeError, KeyError):
        return jsonify(error="missing required json fields"), 400


@app.route("/<short_id>")
async def use(short_id: str):
    url = await crud.get_url_by_short_id(short_id)
    if url is None:
        abort(404)
    return redirect(url.url)


def create_app():
    logging.basicConfig(
        level=logging.getLevelName(get_settings().LOG_LEVEL))
    app.config["SERVER_NAME"] = get_settings().SERVER_NAME
    register_tortoise(
        app,
        db_url=get_settings().DB_URI,
        modules={"models": [models]},
        generate_schemas=True)
    return app
