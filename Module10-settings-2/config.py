from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    admin_email: str

    model_config = SettingsConfigDict(env_file=".env")
