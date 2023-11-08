from pydantic_settings import BaseSettings, SettingsConfigDict

from src.app.schemas.settings import BaseConfig, DatabaseConfig

# , UtilConfig


class Settings(BaseSettings):
    base: BaseConfig
    db: DatabaseConfig
    # util: UtilConfig

    model_config = SettingsConfigDict(
        env_file=".env", env_nested_delimiter="__", extra="ignore"
    )


settings = Settings()
