from pydantic import BaseModel, SecretStr


class BaseConfig(BaseModel):
    APP_TITLE: str = "Autogen"
    DESCRIPTION: str = "PDF"

    SECRET: str = "SECRET"
    VK_TOKEN: SecretStr


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
