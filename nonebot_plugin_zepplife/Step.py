import httpx
from httpx import AsyncClient
from nonebot.adapters.onebot.v11 import Message, PrivateMessageEvent
from nonebot.matcher import Matcher
from nonebot.log import logger
from .Config import conf
from .ResultModule import load_module

handle_module = conf.handle_module
user = conf.zepplife_user
password = conf.zepplife_password
url = conf.url


class Step:
    @staticmethod
    async def manual_step(event: PrivateMessageEvent, manual_input: str, matcher: Matcher):
        try:
            if manual_input == "取消":
                await matcher.finish(Message("已取消手动刷步。"))
                return
            if '，' in manual_input:
                await matcher.reject(Message("请重新输入，不要使用中文逗号..."))
                return
            user, password, steps = manual_input.split(',')
            if not steps.isdigit() or int(steps) > 98800:
                await matcher.reject(Message("步数输入无效，请重新输入一个不超过98800的纯数字组成的数。"))
                return
            await matcher.send(Message("正在修改中..."))
            params = {
                'user': user,
                'password': password,
                'steps': steps
            }
            logger.info(f"{params}")
            async with AsyncClient() as client:
                response = await client.get(url, params=params)
                response.raise_for_status()  # 如果响应状态码不是200，会抛出HTTPError异常
                result = response.json()
            module = load_module(result)
            message = "步数修改成功！\n\nTips:建议刷步时间每次间隔30分钟，防止封号。"
            if handle_module:
                message += f"\n详情: {module}"
            await matcher.finish(Message(message))
        except ValueError:
            await matcher.reject(Message("输入格式错误，请按照账号,密码,步数的格式输入。"))
        except httpx.RequestError as e:
            message = "服务器请求失败，请稍后再试。"
            if handle_module:
                message += f"\n详情: {e}"
            await matcher.finish(Message(message))
        except Exception as e:
            message = "发生未知错误，请检查是否刷步成功，若成功则忽略该条信息。"
            if handle_module:
                message += f"\n详情: {e}"
            await matcher.finish(Message(message))

    @staticmethod
    async def auto_step(event: PrivateMessageEvent, steps: str, matcher: Matcher):
        if steps == "取消":
            await matcher.finish(Message("已取消自动刷步。"))
            return
        elif not steps.isdigit() or int(steps) > 98800:
            await matcher.reject(Message("输入无效，请重新输入一个不超过98800的纯数字组成的数。"))
            return
        await matcher.send(Message("正在修改中..."))
        params = {
            # 'key': key,
            'user': user,
            'password': password,
            'steps': steps
        }
        logger.info(f"{params}")
        try:
            async with AsyncClient() as client:
                response = await client.get(url, params=params)
                response.raise_for_status()  # 如果响应状态码不是200，会抛出HTTPError异常
                result = response.json()
            module = load_module(result)
            message = "步数修改成功！\n\nTips:建议刷步时间每次间隔30分钟，防止封号。"
            if handle_module:
                message += f"\n详情: {module}"
            await matcher.finish(Message(message))
        except httpx.RequestError as e:
            message = "服务器请求失败，请稍后再试。"
            if handle_module:
                message += f"\n详情: {e}"
            await matcher.finish(Message(message))
        except ValueError:
            message = "服务器返回了无效的数据，请稍后再试。"
            if handle_module:
                message += f"\n详情: {result}"
            await matcher.finish(Message(message))
