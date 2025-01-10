import json
from pathlib import Path

import aiofiles
from nonebot.adapters.onebot.v11 import Message, PrivateMessageEvent
from nonebot.internal.matcher import Matcher
from nonebot.log import logger
from .Config import conf
from .ResultModule import load_personal_config

PATH = Path(".") / "ZepplifeUserData"

message_block_chinesecomma = conf.message_block_chinesecomma
group_at = conf.group_at
handle_module = conf.handle_module
message_save_success = conf.message_save_success
message_save_failed = conf.message_save_failed
message_block_dao = conf.message_block_dao
message_empty_config = conf.message_empty_config


# 存储用户数据
async def saveuserdata(filename, data):
    if not PATH.exists():
        PATH.mkdir(parents=True)

    async with aiofiles.open(PATH / filename, 'w', encoding='utf-8') as f:
        await f.write(json.dumps(data, ensure_ascii=False, indent=4))


# 读取用户数据
async def loaduserdata(filename):
    try:
        async with aiofiles.open(PATH / filename, 'r', encoding='utf-8') as f:
            data = json.loads(await f.read())
            return data
    except FileNotFoundError:
        return None


# 删除用户数据
async def deleteuserdata(filename):
    file_path = PATH / filename
    try:
        file_path.unlink()
        return f"用户 {filename} 的数据已成功删除。"
    except FileNotFoundError:
        return f"未找到用户 {filename} 的数据。"
    except Exception as e:
        return f"删除用户数据时发生了错误：{e}。如果多次出现该异常，请联系管理员。"


# 修改用户数据
async def modifyuserdata(filename, field, new_value):
    # 读取现有数据
    data = await loaduserdata(filename)

    if data is None:
        return "未找到相关个人配置。"

    # 对应字段field有对应值new_value
    if field in data:
        data[field] = new_value
    else:
        return "未找到相关个人配置。"

    async with aiofiles.open(PATH / filename, 'w', encoding='utf-8') as f:
        await f.write(json.dumps(data, ensure_ascii=False, indent=4))

    return "已成功保存个人数据。"


class Userdata:
    # 保存我的数据
    @staticmethod
    async def save_my_data(event: PrivateMessageEvent, userdata: str, matcher: Matcher):
        if userdata == "取消":
            await matcher.finish(Message("已取消保存个人数据。"))
            return
        if '，' in userdata:
            await matcher.reject(Message(message_block_chinesecomma))
            return
        user, password = userdata.split(',')
        try:
            data = {
                'qqnumber': event.get_user_id(),
                'user': user,
                'password': password
            }
            logger.info(f"{data}")
            filename = f"{event.get_user_id()}.json"
            await saveuserdata(filename, data)
            await matcher.finish(Message(message_save_success))
        except Exception as e:
            message = message_save_failed
            if handle_module:
                message += f"\n详情:{e}"
            await matcher.finish(Message(message))

    # 修改我的数据
    @staticmethod
    async def modify_my_data(event: PrivateMessageEvent, reply: str, matcher: Matcher):
        if reply == "取消":
            await matcher.finish(Message("已取消修改个人数据。"))
            return
        if '，' in reply:
            await matcher.reject(Message(message_block_chinesecomma))
            return
        user, password = reply.split(',')
        try:
            data = {
                'qqnumber': event.get_user_id(),
                'user': user,
                'password': password
            }
            logger.info(f"{data}")
            filename = f"{event.get_user_id()}.json"
            await saveuserdata(filename, data)
            await matcher.finish(Message(message_save_success))
        except Exception as e:
            message = message_save_failed
            if handle_module:
                message += f"\n详情:{e}"
            await matcher.finish(Message(message))

    # 删除我的数据
    @staticmethod
    async def delete_my_data(event: PrivateMessageEvent, reply: str, matcher: Matcher):
        if reply == "取消":
            await matcher.finish(Message("已取消删除个人数据。"))
            return
        if reply == event.get_user_id():
            try:
                result = await deleteuserdata(f"{event.get_user_id()}.json")
                await matcher.finish(Message(result))
            except Exception as e:
                await matcher.finish(Message(f"删除过程中发生了错误：{e}。\n请稍后再试。如果多次出现该异常，请联系管理员。"))

    # 查看我的数据
    @staticmethod
    async def select_my_data(event: PrivateMessageEvent, matcher: Matcher):
        filename = f"{event.get_user_id()}.json"
        result = await loaduserdata(filename)
        if result:
            message = f"以下是{event.get_user_id()}的个人信息" + load_personal_config(result)
            await matcher.finish(Message(message))
        else:
            await matcher.finish(Message(message_empty_config))
