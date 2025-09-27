# backend/app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    mongo_uri: str = "mongodb+srv://auragarzonr_db_user:Prueba123@cluster0.lkdpmah.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    mongo_db: str = "btg_db"

    class Config:
        env_file = ".env"

settings = Settings()
