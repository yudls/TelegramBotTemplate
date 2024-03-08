from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    admin_token: int


@dataclass
class Settings:
    bots: Bots


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str("TOKEN"),
            admin_token=env.int("ADMIN_ID")
        )
    )


settings = get_settings('config.txt')
print(settings)
