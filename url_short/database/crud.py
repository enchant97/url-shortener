from typing import Union

from tortoise.exceptions import IntegrityError

from .models import Url


async def get_or_create_url(short_id: str, long_url: str) -> Union[None, Url]:
    try:
        url = await Url.get_or_create(
            short_id=short_id, url=long_url)
        return url
    except IntegrityError:
        return None


async def get_url_by_short_id(short_id: str) -> Union[None, Url]:
    return await Url.filter(short_id=short_id).get_or_none()


async def get_url_by_url(url: str) -> Union[None, Url]:
    return await Url.filter(url=url).get_or_none()
