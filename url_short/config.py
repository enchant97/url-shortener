from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_URI: str
    SERVER_NAME: Optional[str] = None
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    LOG_LEVEL: str = "WARNING"

    class Config:
        case_sensitive = True
        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache()
def get_settings():
    """
    returns the Settings obj
    """
    return Settings()
