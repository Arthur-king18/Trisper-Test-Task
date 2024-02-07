import os
from pathlib import Path

from pydantic import BaseModel
from dotenv import load_dotenv

dotenv_path = Path('.env.local')
load_dotenv(dotenv_path=dotenv_path)
WRITE_DB_URL = os.environ.get('WRITE_DB_URL')
READ_DB_URL = os.environ.get('READ_DB_URL')
TEST_DB_URL = os.environ.get('TEST_DB_URL')

class Config(BaseModel):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "localhost"
    APP_PORT: int = 8000
    WRITER_DB_URL: str = WRITE_DB_URL
    READER_DB_URL: str = READ_DB_URL
    TEST_DB_URL: str = TEST_DB_URL
    JWT_SECRET_KEY: str = "threhgrgerg"
    JWT_ALGORITHM: str = "HS256"
    SENTRY_SDN: str = None

class DevelopmentConfig(Config):
    WRITER_DB_URL: str = WRITE_DB_URL
    READER_DB_URL: str = READ_DB_URL
    TEST_DB_URL: str = TEST_DB_URL


class LocalConfig(Config):
    WRITER_DB_URL: str = WRITE_DB_URL
    READER_DB_URL: str = READ_DB_URL
    TEST_DB_URL: str = TEST_DB_URL


class ProductionConfig(Config):
    DEBUG: str = False
    WRITER_DB_URL: str = WRITE_DB_URL
    READER_DB_URL: str = READ_DB_URL


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "dev": DevelopmentConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()