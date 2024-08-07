from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

# from pydantic_settings import BaseSettings, SettingsConfigDict


# class Settings(BaseSettings):
#     DB_HOST: str
#     DB_PORT: int
#     DB_NAME: str
#     DB_USER: str
#     DB_PASS: str

#     @property
#     def DATABASE_URL_psycopg(self):
#         # postgresql+psycopg2://postgres:postgres@localhost:5432/crm_app
#         return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
#     model_config = SettingsConfigDict(env_file=".env")

# settings = Settings()
