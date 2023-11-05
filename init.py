from dataclasses import dataclass


@dataclass
class Settings:
    login: str
    password: str


settings = Settings(login='', password='')

