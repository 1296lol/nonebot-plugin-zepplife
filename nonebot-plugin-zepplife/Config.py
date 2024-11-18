from pydantic import BaseModel
import nonebot

config = nonebot.get_driver().config


class Config(BaseModel):
    key: str = config.xwteam_key
    user: str = config.xwteam_user
    password: str = config.xwteam_password



