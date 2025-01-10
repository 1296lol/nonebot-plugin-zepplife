from nonebot import get_plugin_config, get_driver
from pydantic import BaseModel
from typing import List


# 出现奇怪的报错试试关闭某些配置项，如输出详情、群聊回复是否at_sender等
class Config(BaseModel):
    # 配置项信息
    # zepplife_user: str  # Zepplife账号
    # zepplife_password: str  # Zepplife密码
    superusers: List[str]  # 超级用户
    # 相关指令
    zepplife_commands: dict[str, str | list[str]] = {
        "help": ["刷步帮助", "stephelp"],  # 刷步帮助
        "check": ["刷步检查", "stepcheck"],  # 刷步检查
        "auto_step": ["自动刷步", "autostep"],  # 自动刷步
        "manual_step": ["手动刷步", "manualstep"],  # 手动刷步
        "save_my_data": ["保存我的数据", "savemydata"],  # 保存个人数据
        "modify_my_data": ["修改我的数据", "modifymydata"],  # 修改个人数据
        "delete_my_data": ["删除我的数据", "deletemydata"],  # 删除个人数据
        "select_my_data": ["查看我的数据", "selectmydata"],  # 查看个人数据
    }
    # zepplife_admin_commands: dict[str, str | list[str]] = {
    #     "save_data": ["保存数据", "savedata"],  # 保存数据
    #     "modify_data": ["修改数据", "modifydata"],  # 修改数据
    #     "delete_data": ["删除数据", "deletedata"],  # 删除数据
    #     "select_data": ["查看数据", "selectdata"],  # 查看数据
    # }
    # 接口地址
    url: str = "https://free.xwteam.cn/api/wechat/step"
    # 权限设置
    private_chat: bool = True  # 允许私聊
    group_chat: bool = True  # 允许群聊
    group_at: bool = True  # 群聊回复是否at_sender
    only_superusers_used: bool = False  # 仅超级用户可用
    # 其他设置
    handle_module: bool = True  # 是否输出详情，推荐调试时使用
    # 响应文本
    message_block_requesterror: str = "服务器请求失败，请稍后再试。"
    message_block_unknownerror: str = "发生了未知错误！（肯定是服务器的问题喵~）请检查是否刷步成功，若成功则忽略该条信息。"
    message_success: str = "步数修改成功！\n\nTips:建议刷步时间每次间隔30分钟，防止封号。"
    message_block_step: str = "步数输入无效，请重新输入一个不超过98800的纯数字组成的数。"
    message_block_chinesecomma: str = "请重新输入，不要使用中文逗号！"
    message_loading: str = "正在修改中..."
    message_help_user: str = "刷步方式：向机器人发送对应的中文或英文指令后按提示操作即可。\n" \
                             "\n通用指令:" \
                             "\n【stepcheck】: 【刷步检查】" \
                             "\n【manualstep】: 【手动刷步】" \
                             "\n【autostep】: 【自动刷步】" \
                             "\n私聊指令:" \
                             "\n【savemydata】: 【保存我的数据】" \
                             "\n【modifymydata】: 【修改我的数据】" \
                             "\n【deletemydata】: 【删除我的数据】" \
                             "\n【selectmydata】: 【查看我的数据】"
    # message_help_admin: str = "\n以下是超级用户专属*私聊*指令:" \
    #                           "\n【savedata】: 【保存数据】" \
    #                           "\n【modifydata】: 【修改数据】" \
    #                           "\n【deletedata】: 【删除数据】" \
    #                           "\n【selectdata】: 【查看数据】"
    message_block_users: str = "权限不足，请联系管理员处理。"
    message_block_private: str = "私聊功能已关闭。如有需要，请联系管理员处理。"
    message_block_config: str = "缺少必要的配置项，请检查配置文件中的关键字是否正确填写。"
    message_block_group: str = "群聊功能已关闭。如有需要，请联系管理员处理。"
    message_save_success: str = "保存成功！如需确认请发送刷步检查的命令。"
    message_save_failed: str = "保存失败！请联系管理员处理。"
    message_block_dao: str = "【保存】、【删除】、【修改】、【查看】个人信息的操作请不要在群聊中使用哦，如有需要请向机器人私聊。"
    message_empty_config: str = "个人配置项为空，请确认你已保存个人信息或联系管理员处理。"


conf = get_plugin_config(Config)
config = get_driver().config
