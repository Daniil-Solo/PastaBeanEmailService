from pydantic import EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """
    Class for loading the necessary env variables
    """

    SMTP_HOST: str
    SMTP_PORT: int
    SERVICE_EMAIL: EmailStr
    SERVICE_PASSWORD: str

    model_config = SettingsConfigDict(env_file=".env")


app_config = Config()
