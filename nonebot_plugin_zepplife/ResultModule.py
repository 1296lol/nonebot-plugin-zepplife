def load_module(data):
    # 可自行修改详情，美观建议
    module = (
        f"状态码: {data['code']}\n"
        f"状态信息: {data['msg']}\n"
        f"用户账号: {data['data']['user']}\n"
        f"密码: {data['data']['password']}\n"
        f"步数: {data['data']['steps']}\n"
        f"执行耗时: {data['exec_time']}秒\n"
        f"客户端IP: {data['ip']}\n"
        # f"接口作者: {data['debug']['author']}\n"
        # f"博客地址: {data['debug']['blog']}\n"
        # f"接口介绍: {data['debug']['server_info']}\n"
        # f"接口地址: {data['debug']['api_platform']}\n"
        # f"服务端通知: {data['debug']['notice']}\n"
        # f"服务端赞助: {data['debug']['sponsor']}\n"
        # f"服务端广告: {data['debug']['AD']}"
    )
    return module
