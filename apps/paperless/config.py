from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    debug: bool = False
    development_db : str = ''
    secret_key : str = ""
    refresh_secret_key : str = ""
    token_algorithm : str = ""
    access_token_expire_minutes : int = 0
    refresh_token_expire_minutes : int = 0

    class Config:
        env_file = r'C:\Users\m.rahimi\PycharmProjects\Papaerless\apps\paperless\.env'

