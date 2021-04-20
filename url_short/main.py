import logging

from quart import Quart
from tortoise.contrib.quart import register_tortoise

from .config import get_settings
from .database import models

app = Quart(__name__)


app.route("/", methods=["GET", "POST"])
async def create():
    pass


app.route("/<short_id>")
async def use(short_id):
    pass


def create_app():
    logging.basicConfig(
        level=logging.getLevelName(get_settings().LOG_LEVEL))
    register_tortoise(
        app,
        db_url=get_settings().DB_URL,
        modules={"models": [models]},
        generate_schemas=True)
    return app
