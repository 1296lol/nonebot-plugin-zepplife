from nonebot import get_plugin_config, get_driver
from pydantic import BaseModel
from typing import List


class Config(BaseModel):
    # 配置项信息
    zepplife_user: str
    zepplife_password: str
    superusers: List[str]
    # 相关指令
    zepplife_commands: dict[str, str | list[str]] = {
        "help": ["刷步帮助", "stephelp"],  # 刷步帮助
        "check": ["刷步检查", "stepcheck"],  # 刷步检查
        "auto_step": ["自动刷步", "autostep"],  # 自动刷步
        "manual_step": ["手动刷步", "manualstep"],  # 手动刷步
    }
    # 接口地址
    url: str = "https://free.xwteam.cn/api/wechat/step"
    # 权限设置
    private_chat: bool = True  # 允许私聊
    group_chat: bool = True  # 允许群聊
    group_at: bool = True  # 群聊回复是否at_sender
    only_superusers_used: bool = False  # 仅超级用户可使用
    # 其他设置
    handle_module: bool = True  # 是否输出详情，推荐调试时使用
    message_block_requesterror: str = "服务器请求失败，请稍后再试。"
    message_block_unknownerror: str = "发生了未知错误！（肯定是服务器的问题喵~）请检查是否刷步成功，若成功则忽略该条信息。"
    message_success: str = "步数修改成功！\n\nTips:建议刷步时间每次间隔30分钟，防止封号。"
    message_block_step: str = "步数输入无效，请重新输入一个不超过98800的纯数字组成的数。"
    message_block_chinesecomma: str = "请重新输入，不要使用中文逗号！"
    message_loading: str = "正在修改中..."
    message_help: str = "刷步方式：向机器人发送对应的中文或英文指令后按提示操作即可。\n\nstepcheck: 刷步检查\n\nmanualstep: 手动刷步\n\nautostep: 自动刷步"
    message_block_users: str = "权限不足，请联系管理员处理。"
    message_block_private: str = "私聊功能已关闭。如有需要，请联系管理员处理。"
    message_block_config: str = "缺少必要的配置项，请检查配置文件中的关键字是否正确填写。"
    message_block_group: str = "群聊功能已关闭。如有需要，请联系管理员处理。"


conf = get_plugin_config(Config)
config = get_driver().config
