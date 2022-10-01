# config.py
from pydantic import BaseSettings


class Settings(BaseSettings):
    PSQL_USER: str
    PSQL_PWD: str
    PSQL_HOST: str
    PSQL_PORT: str
    PSQL_DB: str

# specify .env file location as Config attribute
    class Config:
        env_file = ".env.local"