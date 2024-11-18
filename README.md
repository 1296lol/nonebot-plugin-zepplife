<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-zepplife

_✨一款基于修改ZeppLife数据实现刷步的Nonebot机器人插件✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/1296lol/nonebot-plugin-zepplife.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-zepplife">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-zepplife.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">

</div>

这是一款基于调用xwteam平台专属api运行的机器人插件，目前仅支持Zepp、微信、支付宝刷步，后续还会更新其他功能

## 📖 介绍

这里是插件的详细介绍部分

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-zepplife

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-zepplife
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-zepplife
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-zepplife
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-zepplife
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_zepplife"]

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项 | 必填 | 默认值 | 类型 |
|:-----:|:----:|:----:|:----:|
| XWTEAM_KEY | 是 | 替换为你的key | String |
| XWTEAM_USER | 是 | Zepp账号邮箱 | String |
| XWTEAM_PASSWORD | 是 | Zepp密码 | String |

## 🎉 使用
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| 刷步 | 好友 | 是 | 私聊 | 直接发送 |
### 效果图

