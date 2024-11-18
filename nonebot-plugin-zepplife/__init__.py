import requests
from nonebot import on_command, get_plugin_config
from nonebot.adapters.onebot.v11 import Message, Event
from nonebot.internal.params import ArgPlainText
from nonebot.log import logger
from nonebot.plugin import PluginMetadata

from .Config import Config

__plugin_meta__ = PluginMetadata(
    name="修改ZeppLife数据实现刷步的Nonebot机器人插件",
    description="这是一款基于调用xwteam平台专属api运行的机器人插件，目前仅支持Zepp、微信、支付宝刷步，后续还会更新其他功能",
    usage="",
    type="application",
    homepage="https://github.com/1296lol/nonebot-plugin-zepplife",
    config=Config,
    supported_adapters={"~onebot.v11"},
    extra={
        "author": "1296lol"
    },
)

conf = get_plugin_config(Config)

matcher = on_command('刷步', priority=50, block=True)


@matcher.got("steps", prompt="请输入步数，输入“取消”退出。")
async def get_steps(event: Event, steps: str = ArgPlainText()):
    if steps == "取消":
        await matcher.finish(Message("已取消操作。"))
        return
    elif not steps.isdigit() or int(steps) > 98800:
        await matcher.reject(Message("输入无效，请输入一个不超过98800的纯数字组成的数。"))
        return

    await matcher.send(Message("正在修改中..."))

    url = 'https://api.xwteam.cn/api/wechat/step'
    # stepList = [segment.data['text'] for segment in steps if segment.type == 'text']
    # step = ''.join(stepList)
    params = {
        'key': conf.key,
        'user': conf.user,
        'password': conf.password,
        'steps': steps
    }
    logger.info(f"{params}")
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # 如果响应状态码不是200，会抛出HTTPError异常
        result = response.json()
        # print(result)
        await matcher.finish(Message("步数修改成功！"))
    except requests.exceptions.RequestException as e:
        # print(f"请求失败: {e}")
        await matcher.finish(Message("服务器请求失败，请稍后再试。"))
    except ValueError:
        # print("响应内容不是有效的 JSON 格式")
        await matcher.finish(Message("服务器返回了无效的数据，请稍后再试。"))
