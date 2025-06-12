from pydantic import BaseSettings

# settings class for application confiuration which extends BaseSettings from pydantic
# this allows for enviroment variable loading and validation
class Settings(BaseSettings):
    DATABASE_URL: str 
    SECRET_KEY: str
    DEBUG: bool = False  # default value for DEBUG is False 

    class Config:
        env_file = ".env"

settings = Settings()

