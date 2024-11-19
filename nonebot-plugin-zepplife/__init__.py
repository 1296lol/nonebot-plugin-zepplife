import requests
from .ResultModule import load_module
from nonebot.adapters.onebot.v11 import Message, PrivateMessageEvent, Bot
from nonebot import on_command, get_plugin_config
from nonebot.internal.params import ArgPlainText
from nonebot.matcher import Matcher
from .Config import Config
from nonebot.log import logger

conf = get_plugin_config(Config)
key = conf.key
user = conf.user
password = conf.password
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
    user_id = event.get_user_id()

    if not key or not user or not password:
        # raise ValueError(message_block_config)
        await matcher.finish(Message(message_block_config))
        return

    if user_id not in superusers and only_superusers_used:
        await matcher.finish(Message(message_block_users))
        return

    if not private_chat:
        await matcher.finish(Message(message_block_private))
        return


@matcher.got("steps", prompt="请输入步数，输入“取消”退出。")
async def get_steps(event: PrivateMessageEvent, steps: str = ArgPlainText()):
    if steps == "取消":
        await matcher.finish(Message("已取消操作。"))
        return
    elif not steps.isdigit() or int(steps) > 98800:
        await matcher.reject(Message("输入无效，请重新输入一个不超过98800的纯数字组成的数。"))
        return
    await matcher.send(Message("正在修改中..."))

    url = 'https://api.xwteam.cn/api/wechat/step'
    # stepList = [segment.data['text'] for segment in steps if segment.type == 'text']
    # step = ''.join(stepList)
    params = {
        'key': key,
        'user': user,
        'password': password,
        'steps': steps
    }
    logger.info(f"{params}")
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # 如果响应状态码不是200，会抛出HTTPError异常
        result = response.json()
        # logger.info(result)
        module = load_module(result)
        message = "步数修改成功！\n\nTips:建议刷步时间每次间隔30分钟，防止封号。"
        if handle_module:
            message += f"\n详情: {module}"
        await matcher.finish(Message(message))

    except requests.exceptions.RequestException as e:
        # print(f"请求失败: {e}")
        message = "服务器请求失败，请稍后再试。"
        if handle_module:
            message += f"\n详情: {e}"
        await matcher.finish(Message(message))
    except ValueError:
        # print("响应内容不是有效的 JSON 格式")
        message = "服务器返回了无效的数据，请稍后再试。"
        if handle_module:
            message += f"\n详情: {result}"
        await matcher.finish(Message(message))
