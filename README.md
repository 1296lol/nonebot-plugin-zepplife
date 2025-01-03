<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
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

# <font color="red">注意</font>
在刷步之前，请确保你拥有ZeppLife的账号以及该账号已绑定微信、支付宝等第三方平台。(这点非常重要哦)

### 📢 常见问题
如果出现特殊报错，请试着在本地关闭某些配置项。路径如下：
`~\your_bot\.venv\Lib\site-packages\nonebot_plugin_zepplife\Config.py`

## ~~About:如何获取key~~


~~进入[xwteam平台官网](https://api.xwteam.cn/)，注册后即可在密钥管理中查看自己专属的api_key~~

## Tips


由于未知原因，网站关闭了接口功能。现改用新的接口实现刷步，仅需注册zepplife账号并绑定微信或支付宝即可。


zepplife账号注册请在手机应用商店中下载Zepplife(原小米运动)，按提示注册并绑定后即可卸载软件。


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
| ZEPPLIFE_USER | 是 | none | String |
| ZEPPLIFE_PASSWORD | 是 | none | String |

以下是一个样例

```
ZEPPLIFE_USER="123456@example.com" #这里换成你的Zepp邮箱
ZEPPLIFE_PASSWORD="123456" #这里换成你的Zepp密码
```

## 🎉 使用
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| stephelp/刷步帮助 | -- | 是 | 私聊、群聊 | 获得帮助 |
| stepcheck/刷步检查 | -- | 是 | 私聊、群聊 | 检查配置 |
| autostep/自动刷步 | -- | 是 | 私聊、群聊 | 自动刷步 |
| manualstep/手动刷步 | -- | 是 | 私聊、群聊 | 手动刷步 |
### 效果图
![没有图片就代表我还没做效果图，哈哈](https://gitee.com/lol1296/picturebases/raw/master/nonebot-plugin-zepplife-4.png)
