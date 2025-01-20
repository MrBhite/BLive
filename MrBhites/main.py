import win32com.client
from blive import BLiver,  Events, BLiverCtx, const
from blive.msg import (
    DanMuMsg,
    EntryEffectMsg,
    InteractWordMsg,
    SendGiftMsg,
    SuperChatMsg,
)
import GPT_SoVITS

app = BLiver(9541125)

def say(body: str):
    speak = win32com.client.Dispatch("SAPI.SpVoice")
    speak.Speak(body)

@app.on(Events.DANMU_MSG)
async def listen(ctx: BLiverCtx):
    danmu = DanMuMsg(ctx.body)
    if const.TEST:
        print(
            f'[弹幕] {danmu.sender.name} ({danmu.sender.medal.medal_name}:{danmu.sender.medal.medal_level}): "{danmu.content}"\n'
        )
    say(danmu.sender.name + "说:" + danmu.content)

@app.on(Events.HEARTBEAT_REPLY)
async def liver_popularity(ctx: BLiverCtx):
    print("[HB] 当前人气值:", ctx.body['popularity'])

@app.on(Events.INTERACT_WORD)
async def listen_join(ctx: BLiverCtx):
    join = InteractWordMsg(ctx.body)
    if const.TEST:
        print(
            "[欢迎]",
            f"{join.user['name']} ({join.user['medal']['medal_name']}:{join.user['medal']['medal_level']})",
            "进入直播间\n",
        )
    say("[欢迎]" + join.user['name'] + "进入直播间")


@app.on(Events.SUPER_CHAT_MESSAGE)
async def listen_sc(ctx: BLiverCtx):
    msg = SuperChatMsg(ctx.body)
    if const.TEST:
        print(
            f"[SC] 感谢 {msg.sender['name']}({msg.sender['medal']['medal_name']}:{msg.sender['medal']['medal_level']})的价值 {msg.price} 的sc\n\n\t{msg.content}\n"
        )
    say("感谢" + msg.sender['name'] + "送出价值" + msg.price + "的sc")


@app.on(Events.SEND_GIFT)
async def listen_gift(ctx: BLiverCtx):
    msg = SendGiftMsg(ctx.body)
    if const.TEST:
        print(
            f"[礼物] {msg.sender['name']} ({msg.sender['medal']['medal_name']}:{msg.sender['medal']['medal_level']}) 送出 {msg.gift['gift_name']}\n"
        )
    say("感谢" + msg.sender['name'] + "送出的" + msg.gift['gift_name'])


@app.on(Events.ENTRY_EFFECT)
async def welcome_captain(ctx: BLiverCtx):
    msg = EntryEffectMsg(ctx.body)
    if const.TEST:
        print(f"[热烈欢迎] {msg.copy_writting}\n")
    say("热烈欢迎" + msg.copy_writting + "老爷进入直啵间")


@app.on(Events.LIVE)
async def liver_popularity(ctx: BLiverCtx):
    if const.TEST:
        print("[TEST] 上啵")
    say("上播")

@app.on(Events.PREPARING)
async def liver_popularity(ctx: BLiverCtx):
    if const.TEST:
        print("[TEST] 下啵")
    say("下播")

if __name__ == "__main__":
    try:
        app.run()
    except KeyboardInterrupt as exc:
        print('Quit.')