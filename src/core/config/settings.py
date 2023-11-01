import os

from pathlib import Path
from pydantic_settings import BaseSettings


BASE_PATH = Path(__file__).resolve().parent.parent.parent.parent
LOG_PATH = os.path.join(BASE_PATH, 'logs')


class Settings(BaseSettings):

    BOT_TOKEN: str
    TITLE: str = 'Tg_bot_mongo'
    VERSION: str = '0.1'
    DESCRIPTION: str = 'tg bot on mongodb'

    # Log
    LOG_FILENAME: str = 'tg_bot.log'
    DEBUG: str


settings = Settings()
