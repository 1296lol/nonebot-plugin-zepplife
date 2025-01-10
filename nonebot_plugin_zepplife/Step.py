import json
import httpx
from httpx import AsyncClient
from nonebot.adapters.onebot.v11 import Message, MessageEvent
from nonebot.exception import FinishedException
from nonebot.matcher import Matcher
from nonebot.log import logger
from .Config import conf
from .ResultModule import load_module
from .Userdata import loaduserdata

# user = conf.zepplife_user
# password = conf.zepplife_password
handle_module = conf.handle_module
url = conf.url
message_success = conf.message_success
message_block_requesterror = conf.message_block_requesterror
message_block_unknownerror = conf.message_block_unknownerror
message_block_step = conf.message_block_step
message_block_chinesecomma = conf.message_block_chinesecomma
message_loading = conf.message_loading
group_at = conf.group_at


class Step:
    # 手动刷步
    @staticmethod
    async def manual_step(event: MessageEvent, manual_input: str, matcher: Matcher):
        try:
            if manual_input == "取消":
                await matcher.finish(Message("已取消手动刷步。"), at_sender=group_at)
                return
            if '，' in manual_input:
                await matcher.reject(Message(message_block_chinesecomma), at_sender=group_at)
                return
            user, password, steps = manual_input.split(',')
            if not steps.isdigit() or int(steps) > 98800:
                await matcher.reject(Message(message_block_step), at_sender=group_at)
                return
            await matcher.send(Message(message_loading), at_sender=group_at)
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
            message = message_success
            if handle_module:
                message += f"\n详情: {module}"
            await matcher.finish(Message(message), at_sender=group_at)
        except ValueError:
            await matcher.reject(Message("输入格式错误，请按照账号,密码,步数的格式输入。"))
        except httpx.RequestError as e:
            message = message_block_requesterror
            if handle_module:
                message += f"\n详情: {e}"
            await matcher.finish(Message(message), at_sender=group_at)
        except FinishedException:
            raise FinishedException
        except Exception as e:
            message = message_block_unknownerror
            if handle_module:
                message += f"\n详情: {e}"
            await matcher.finish(Message(message), at_sender=group_at)

    # 自动刷步
    @staticmethod
    async def auto_step(event: MessageEvent, steps: str, matcher: Matcher):
        if steps == "取消":
            await matcher.finish(Message("已取消自动刷步。"), at_sender=group_at)
            return
        elif not steps.isdigit() or int(steps) > 98800:
            await matcher.reject(Message(message_block_step), at_sender=group_at)
            return
        await matcher.send(Message(message_loading), at_sender=group_at)
        data = await loaduserdata(f"{event.get_user_id()}.json")
        if not data:
            await matcher.finish(Message("自动刷步失败！请检查你的个人配置后重新自动刷步或联系管理员处理。"))
            return
        params = {
            'user': data['user'],
            'password': data['password'],
            'steps': steps
        }
        logger.info(f"{params}")
        try:
            async with AsyncClient() as client:
                response = await client.get(url, params=params)
                response.raise_for_status()  # 如果响应状态码不是200，会抛出HTTPError异常
                result = response.json()
            module = load_module(result)
            message = message_success
            if handle_module:
                message += f"\n详情: {module}"
            await matcher.finish(Message(message), at_sender=group_at)
        except httpx.RequestError as e:
            message = message_block_requesterror
            if handle_module:
                message += f"\n详情: {e}"
            await matcher.finish(Message(message), at_sender=group_at)
        except ValueError:
            message = "服务器返回了无效的数据，请检查你的自动刷步账号密码，若无问题请稍后再试。"
            if handle_module:
                message += f"\n详情: {result}"
            await matcher.finish(Message(message), at_sender=group_at)
