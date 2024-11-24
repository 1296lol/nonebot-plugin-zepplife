from nonebot.adapters.onebot.v11 import Message, PrivateMessageEvent, Bot
from nonebot import on_command
from nonebot.internal.params import ArgPlainText
from .Config import Config, conf
from nonebot.plugin import PluginMetadata
from .Step import Step

# ---------------------------Configurations---------------------------
__plugin_meta__ = PluginMetadata(
    name="nonebot-plugin-zepplife",
    description="基于调用xwteam平台专属api运行的机器人插件，目前仅支持Zepp、微信、支付宝刷步，后续还会更新其他功能",
    usage="",
    type='application',
    homepage="https://github.com/1296lol/nonebot-plugin-zepplife",
    config=Config,
    supported_adapters={"~onebot.v11"},
    extra={
        "author": "1296",
        "email": "hh1296@foxmail.com"
    }
)


# key = conf.xwteam_key
user = conf.zepplife_user
password = conf.zepplife_password
private_chat = conf.private_chat
message_block_private = conf.message_block_private
message_block_config = conf.message_block_config
message_block_users = conf.message_block_users
handle_module = conf.handle_module
superusers = conf.superusers
only_superusers_used = conf.only_superusers_used

matcher = on_command('刷步', priority=50, block=True)


# 私聊响应
@matcher.handle()
async def start(bot: Bot, event: PrivateMessageEvent):
    await matcher.send(Message("刷步方式：发送对应前缀指令后按提示操作即可\n\nmanualstep:手动刷步\n\nautostep:自动刷步"))


manual = on_command("manualstep", priority=50, block=True)

auto = on_command("autostep", priority=50, block=True)


@manual.got("manual_input",
            prompt="请输入账号、密码、步数，格式为：账号,密码,步数。\n\n例如：abc@example.com,password,1000\n\n输入”取消“退出。")
async def handle_choice(event: PrivateMessageEvent, manual_input: str = ArgPlainText()):
    user_id = event.get_user_id()

    if not user or not password:
        # if not key or not user or not password:
        # raise ValueError(message_block_config)
        await matcher.finish(Message(message_block_config))
        return

    if user_id not in superusers and only_superusers_used:
        await matcher.finish(Message(message_block_users))
        return

    if not private_chat:
        await matcher.finish(Message(message_block_private))
        return
    await Step.manual_step(event, manual_input, manual)


@auto.got("steps", prompt="请输入步数，输入“取消”退出。")
async def handle_auto_step(event: PrivateMessageEvent, steps: str = ArgPlainText()):
    user_id = event.get_user_id()

    if not user or not password:
        # if not key or not user or not password:
        # raise ValueError(message_block_config)
        await matcher.finish(Message(message_block_config))
        return

    if user_id not in superusers and only_superusers_used:
        await matcher.finish(Message(message_block_users))
        return

    if not private_chat:
        await matcher.finish(Message(message_block_private))
        return
    await Step.auto_step(event, steps, auto)
