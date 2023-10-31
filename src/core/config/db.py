from pydantic import MongoDsn
from pydantic_settings import BaseSettings


class ConfigDataBase(BaseSettings):
    MONGO_HOST: str
    MONGO_PORT: str
    MONGO_USER: str
    MONGO_PASS: str
    MONGO_DB: str
    MONGO_COLLECTION: str

    @property
    def database_url(self) -> MongoDsn | None:
        return (
            f'mongodb://{self.MONGO_USER}:{self.MONGO_PASS}@'
            f'{self.MONGO_HOST}:{self.MONGO_PORT}/?retryWrites=true&w=majority'
        )


settings_db = ConfigDataBase()
