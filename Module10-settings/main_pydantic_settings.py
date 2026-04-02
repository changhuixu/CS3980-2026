from pydantic_settings import BaseSettings, SettingsConfigDict


class MySettings(BaseSettings):
    app_name: str = "Awesome App"
    admin_email: str
    items_per_user: int = 50
    accepted_currencies: list[str]

    model_config = SettingsConfigDict(env_file=".env")


settings = MySettings()
print(settings)
