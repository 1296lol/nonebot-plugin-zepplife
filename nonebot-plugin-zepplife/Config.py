from pydantic import BaseModel
import nonebot
from typing import List

config = nonebot.get_driver().config


class Config(BaseModel):
    key: str = config.xwteam_key
    user: str = config.xwteam_user
    password: str = config.xwteam_password
    superusers: List[str] = config.superusers
    # 私聊设置
    private_chat: bool = True  # 允许私聊
    message_block_private: str = "私聊功能已关闭。如有需要，请联系管理员处理。"
    message_block_config: str = "缺少必要的配置项，请检查配置文件中的关键字是否正确填写。"
    message_block_users: str = "权限不足，请联系管理员处理。"
    # 权限设置
    only_superusers_used: bool = True  # 仅超级用户可使用
    # 其他设置
    handle_module: bool = True  # 是否输出详情，推荐调试时使用
