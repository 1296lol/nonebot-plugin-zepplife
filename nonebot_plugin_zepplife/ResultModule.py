from .Config import conf


# 详情模板
def load_module(data):
    # 可自行修改详情，美观建议
    module = (
        f"\n状态码: {data['code']}\n"
        f"状态信息: {data['msg']}\n"
        f"用户账号: {data['data']['user']}\n"
        f"密码: {data['data']['password']}\n"
        f"提示信息: {data['data']['steps']}\n"
        f"执行耗时: {data['exec_time']}秒\n"
        f"客户端IP: {data['ip']}\n"
        # f"接口作者: {data['debug']['author']}\n"
        # f"博客地址: {data['debug']['blog']}\n"
        # f"接口介绍: {data['debug']['server_info']}\n"
        # f"接口地址: {data['debug']['api_platform']}\n"
        # f"服务端通知: {data['debug']['notice']}\n"
        # f"服务端赞助: {data['debug']['sponsor']}\n"
        # f"服务端广告: {data['debug']['AD']}\n"
    )
    return module


# 检查模板
def load_check():
    module = (
        f"\n是否配置自动刷步账号:{bool(conf.zepplife_user)}\n"
        f"是否配置自动刷步密码:{bool(conf.zepplife_password)}\n"
        f"是否仅允许超级用户使用:{conf.only_superusers_used}\n"
        f"是否允许私聊:{conf.private_chat}\n"
        f"是否允许群聊:{conf.group_chat}\n"
        f"群聊回复是否艾特:{conf.group_at}\n"
        f"是否输出详情:{conf.handle_module}\n"
    )
    return module
