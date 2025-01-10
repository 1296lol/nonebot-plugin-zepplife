from .Config import conf


# 详情
def load_module(data):
    # 可自行修改详情，美观建议
    module = (
        f"\n状态码: {data['code']}"
        f"\n状态信息: {data['msg']}"
        f"\n用户账号: {data['data']['user']}"
        f"\n密码: {data['data']['password']}"
        f"\n提示信息: {data['data']['steps']}"
        f"\n执行耗时: {data['exec_time']}秒"
        f"\n客户端IP: {data['ip']}"
        # f"接口作者: {data['debug']['author']}\n"
        # f"博客地址: {data['debug']['blog']}\n"
        # f"接口介绍: {data['debug']['server_info']}\n"
        # f"接口地址: {data['debug']['api_platform']}\n"
        # f"服务端通知: {data['debug']['notice']}\n"
        # f"服务端赞助: {data['debug']['sponsor']}\n"
        # f"服务端广告: {data['debug']['AD']}\n"
    )
    return module


# 检查
def load_check(data):
    module = (
        f"\n是否配置自动刷步账号:{bool(data['user'])}"
        f"\n是否配置自动刷步密码:{bool(data['password'])}"
        f"\n是否仅允许超级用户使用:{conf.only_superusers_used}"
        f"\n是否允许私聊:{conf.private_chat}"
        f"\n是否允许群聊:{conf.group_chat}"
        f"\n群聊回复是否艾特:{conf.group_at}"
        f"\n是否输出详情:{conf.handle_module}"
    )
    return module


# 个人配置
def load_personal_config(data):
    module = (
        f"\nQQ号:{data['qqnumber']}"
        f"\nZepplife账号:{data['user']}"
        f"\nZepplife密码:{data['password']}"
    )
    return module
