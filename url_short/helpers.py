import base64
import hashlib
import urllib.parse

from quart import url_for


def make_short_url(url: str) -> str:
    hashed = hashlib.sha256(url.encode()).digest()
    safe_hashed = base64.urlsafe_b64encode(hashed).decode()
    short_id = safe_hashed[:8]
    return short_id


def short_id_to_url(short_url: str) -> str:
    return url_for("use", _external=True, short_id=short_url)


def make_url_safe(url: str) -> str:
    url_split = urllib.parse.urlparse(url, scheme="http")
    url_split.path.replace("\t", "")
    return urllib.parse.urlunparse(url_split)
