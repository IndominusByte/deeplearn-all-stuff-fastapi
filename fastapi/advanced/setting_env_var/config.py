from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Awesome API"
    environment: str
    token_expired: int

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
