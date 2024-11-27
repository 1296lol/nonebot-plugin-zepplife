from nonebot import on_message
from nonebot.adapters.onebot.v11 import Message, MessageEvent, PrivateMessageEvent, GroupMessageEvent
from nonebot.internal.params import ArgPlainText
from nonebot.internal.rule import Rule
from nonebot.plugin import PluginMetadata
from nonebot.rule import to_me, command, is_type
from .ResultModule import load_check
from .Config import Config, conf
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

user = conf.zepplife_user
password = conf.zepplife_password
private_chat = conf.private_chat
group_chat = conf.group_chat
group_at = conf.group_at
message_block_group = conf.message_block_group
message_block_private = conf.message_block_private
message_block_config = conf.message_block_config
message_block_users = conf.message_block_users
message_help = conf.message_help
handle_module = conf.handle_module
superusers = conf.superusers
only_superusers_used = conf.only_superusers_used
zepplife_commands = conf.zepplife_commands


# 命令转换函数
def trans_command(cmds: str | list[str]):
    if isinstance(cmds, str):
        cmds = [cmds]
    return command(*cmds)


# # 私聊阻断函数
# async def privateblock() -> bool:
#     return not private_chat
# block_private = is_type(PrivateMessageEvent) & privateblock
#
#
# private_block_matcher = on_message(rule=block_private, priority=50, block=True)
#
#
# @private_block_matcher.handle()
# async def private_chat_block():
#     await private_block_matcher.finish(Message(message_block_private))
#
#
# # 群聊阻断函数
# async def groupblock() -> bool:
#     return not group_chat
# block_group = is_type(GroupMessageEvent) & groupblock
# group_block_matcher = on_message(rule=block_group, priority=50, block=True)
#
#
# @group_block_matcher.handle()
# async def group_chat_block():
#     await group_block_matcher.finish(Message(message_block_group), at_sender=group_at)


# # 通用阻断函数
# async def block_message(event: MessageEvent) -> bool:
#     if isinstance(event, PrivateMessageEvent):
#         return not private_chat
#     elif isinstance(event, GroupMessageEvent):
#         return not group_chat
#     return False
#
#
# def command_block_rule(commands: dict[str, str | list[str]]) -> Rule:
#     async def rule(event: MessageEvent) -> bool:
#         if isinstance(event, MessageEvent):
#             for command, aliases in commands.items():
#                 if isinstance(aliases, str):
#                     aliases = [aliases]
#                 for alias in aliases:
#                     if event.get_plaintext().strip().startswith(f"/{alias}"):
#                         return await block_message(event)
#         return False
#     return Rule(rule)
#
#
# block_matcher = on_message(rule=command_block_rule(zepplife_commands), priority=50, block=True)
#
#
# @block_matcher.handle()
# async def handle_blocked_message(event: MessageEvent):
#     if isinstance(event, PrivateMessageEvent):
#         await block_matcher.finish(Message(message_block_private))
#     elif isinstance(event, GroupMessageEvent):
#         await block_matcher.finish(Message(message_block_group), at_sender=group_at)


# 刷步帮助
zepplife_help = to_me() & trans_command(zepplife_commands["help"])

matcher_help = on_message(rule=zepplife_help, priority=50, block=True)


@matcher_help.handle()
async def start():
    await matcher_help.finish(Message(message_help), at_sender=group_at)


# 刷步检查
zepplife_check = to_me() & trans_command(zepplife_commands["check"])

check = on_message(rule=zepplife_check, priority=50, block=True)


@check.handle()
async def checking():
    await check.finish(Message(f"检查结果:\n{load_check()}"), at_sender=group_at)


# 刷步实现
manual_step = to_me() & trans_command(zepplife_commands["manual_step"])
auto_step = to_me() & trans_command(zepplife_commands["auto_step"])

manual = on_message(rule=manual_step, priority=50, block=True)

auto = on_message(rule=auto_step, priority=50, block=True)


@manual.got("manual_input",
            prompt="请输入账号、密码、步数，格式为：账号,密码,步数。\n\n例如：abc@example.com,password,1000\n\n输入”取消“退出。")
async def handle_choice(event: MessageEvent, manual_input: str = ArgPlainText()):
    user_id = event.get_user_id()

    if not user or not password:
        # raise ValueError(message_block_config)
        await manual.finish(Message(message_block_config), at_sender=group_at)
        return

    if user_id not in superusers and only_superusers_used:
        await manual.finish(Message(message_block_users), at_sender=group_at)
        return

    if not private_chat:
        await manual.finish(Message(message_block_private), at_sender=group_at)
        return

    if not group_chat:
        await manual.finish(Message(message_block_group), at_sender=group_at)
        return

    await Step.manual_step(event, manual_input, manual)


@auto.got("steps", prompt="请输入步数，输入“取消”退出。")
async def handle_auto_step(event: MessageEvent, steps: str = ArgPlainText()):
    user_id = event.get_user_id()

    if not user or not password:
        # raise ValueError(message_block_config)
        await auto.finish(Message(message_block_config), at_sender=group_at)
        return

    if user_id not in superusers and only_superusers_used:
        await auto.finish(Message(message_block_users), at_sender=group_at)
        return

    if not private_chat:
        await auto.finish(Message(message_block_private), at_sender=group_at)
        return

    if not group_chat:
        await auto.finish(Message(message_block_group), at_sender=group_at)
        return

    await Step.auto_step(event, steps, auto)
