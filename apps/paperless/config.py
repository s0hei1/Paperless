from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    debug: bool = False
    development_db : str = ''

    class Config:
        env_file = '.env'

