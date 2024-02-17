from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    REDIS_HOST: str
    REDIS_PORT: int

    SECRET_KEY_1: str
    SECRET_KEY_2: str

    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASS: str

    class Config:
        env_file = ".env"


settings = Settings()
