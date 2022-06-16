import nonebot
from .data_source import wfClock
from nonebot.adapters.onebot.v11 import Event, Bot, MessageSegment

__zx_plugin_name__ = "Warframe时间查询"
__plugin_usage__ = """
usage：
    触发方式：发送 wf平原/wf地球/wf金星/wf火卫二 查看指定地图时间
""".strip()
__plugin_des__ = "查询Warframe地图时间"
__plugin_type__ = ("一些工具",)
__plugin_cmd__ = ["发送:wf平原/wf地球/wf金星/wf火卫二 进行查询"]
__plugin_version__ = 0.1
__plugin_author__ = "zmyy"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    'cmd': __plugin_cmd__
}

eidolon = nonebot.on_command("wf平原")
earth = nonebot.on_command("wf地球")
vallis = nonebot.on_command("wf金星")
cambion = nonebot.on_command("wf火卫二")

@eidolon.handle()
async def _(bot: Bot, event: Event):
    image = await wfClock.eidolon()
    if image:
        await eidolon.finish(MessageSegment.image(image))
    else:
        await eidolon.finish("出现未知错误，请稍后再试。")


@earth.handle()
async def _(bot: Bot, event: Event):
    image = wfClock.earth()
    await earth.finish(MessageSegment.image(image))


@vallis.handle()
async def _(bot: Bot, event: Event):
    image = wfClock.vallis()
    await vallis.finish(MessageSegment.image(image))

@cambion.handle()
async def _(bot: Bot, event: Event):
    image = await wfClock.cambion()
    if image:
        await eidolon.finish(MessageSegment.image(image))
    else:
        await eidolon.finish("出现未知错误，请稍后再试。")