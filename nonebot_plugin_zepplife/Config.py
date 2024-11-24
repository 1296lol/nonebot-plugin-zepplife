from nonebot import get_plugin_config, get_driver
from pydantic import BaseModel
from typing import List


class Config(BaseModel):
    # 配置项信息
    # xwteam_key: str
    zepplife_user: str
    zepplife_password: str
    superusers: List[str]
    # 接口地址
    url: str = "https://free.xwteam.cn/api/wechat/step"
    # 私聊设置
    private_chat: bool = True  # 允许私聊
    message_block_private: str = "私聊功能已关闭。如有需要，请联系管理员处理。"
    message_block_config: str = "缺少必要的配置项，请检查配置文件中的关键字是否正确填写。"
    message_block_users: str = "权限不足，请联系管理员处理。"
    # 权限设置
    only_superusers_used: bool = False  # 仅超级用户可使用
    # 其他设置
    handle_module: bool = True  # 是否输出详情，推荐调试时使用


conf = get_plugin_config(Config)
config = get_driver().config
