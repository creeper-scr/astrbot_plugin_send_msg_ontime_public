flag_not_support = False
try:
    from util.plugin_dev.api.v1.bot import Context, AstrMessageEvent, CommandResult
    from util.plugin_dev.api.v1.config import *
except ImportError:
    flag_not_support = True
    print("导入接口失败。请升级到 AstrBot 最新版本。")
import asyncio
from util.plugin_dev.api.v1.platform import *
from datetime import datetime, time as dt_time
from util.plugin_dev.api.v1.types import Image, Plain
from addons.plugins.astrbot_plugin_qqAD.config import *

'''
注意以格式 XXXPlugin 或 Main 来修改插件名。
提示：把此模板仓库 fork 之后 clone 到机器人文件夹下的 addons/plugins/ 目录下，然后用 Pycharm/VSC 等工具打开可获更棒的编程体验（自动补全等）
'''
class qqADPlugin:
    """
    AstrBot 会传递 context 给插件。
    
    - context.register_commands: 注册指令
    - context.register_task: 注册任务
    - context.message_handler: 消息处理器(平台类插件用)
    """
    def __init__(self, context: Context) -> None:
        self.context = context
        self.context.register_task(self.send_qq_msg(), 'send_qq_msg')

    """
    指令处理函数。
    
    - 需要接收两个参数：message: AstrMessageEvent, context: Context
    - 返回 CommandResult 对象
    """
    async def send_qq_msg(self):
        while True:
            now = datetime.now()
            for send_time in send_times:
                if now.hour == send_time:
                    await asyncio.sleep(5)
                    await self.send_msg()
            await asyncio.sleep(3400)

    async def send_msg(self):
        platforms = self.context.platforms
        platform = None
        for p in platforms:
            if p.platform_name == 'aiocqhttp':
                print(p.platform_name)
                platform = p
                break
        if platform:
            inst = platform.platform_instance
            for group in groups:
                await inst.send_msg({"group_id": group}, CommandResult(message_chain=[Plain(txt), Image.fromFileSystem(photo)]))
                await asyncio.sleep(5)



