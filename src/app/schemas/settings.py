from pydantic import BaseModel, SecretStr


class BaseConfig(BaseModel):
    APP_TITLE: str = "Autogen"
    DESCRIPTION: str = "PDF"

    SECRET: str = "SECRET"


class ParserConfig(BaseModel):
    host: str = "api.vk.ru"
    vk_token: SecretStr
    version: float = 5.154

    method_get_user: str = "users.get"

    method_get_friends: str = "friends.get"
    fields_friend: str = "contacts"

    method_get_group: str = "groups.get"
    filter_group: str = "groups,publics"


class DatabaseConfig(BaseModel):
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "autogen"
    DB_USER: str = "postgres"
    DB_PASS: str = "postgres"
    DATABASE_URL: str = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


# class UtilConfig(BaseModel):
#     ZERO: int = 0
#     LENGTH_NAME: int = 100
#     MIN_ANYSTR_LENGTH: int = 1
#     MIN_LENGTH_PASS: int = 3
#     LIFETIME_JWT: int = 3600
