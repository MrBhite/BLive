import warnings
import json
import asyncio
from typing import List, Union
import aiohttp
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiowebsocket.converses import AioWebSocket
from pyee import AsyncIOEventEmitter
from .core import (
    BLiveMsgPackage,
    PackageHeader,
    Events,
    Operation,
    get_blive_room_info,
    get_blive_ws_url,
    certification,
    heartbeat,
)
from . import const


class BLiverCtx:
    def __init__(self, bliver, msg) -> None:
        self.ws = bliver.ws
        self.bliver: BLiver = bliver
        self.msg: tuple[PackageHeader, dict] = msg  # 原始消息
        self.header: PackageHeader = self.msg[0]  # 消息头部
        self.body: dict = json.loads(msg[1])


class BLiver(AsyncIOEventEmitter):
    real_room_id: Union[None, int]
    uname: Union[None, str]

    def __init__(self, room_id, uid=0):
        super().__init__()
        self.running = False
        
        self.room_id = room_id
        self.uid = uid
        self.aio_session = aiohttp.ClientSession()
        self.packman = BLiveMsgPackage()
        self.scheduler = AsyncIOScheduler(timezone="Asia/ShangHai")

    def register_handler(self, event: Union[Events, List[Events]], handler):
        warnings.warn(
            "`register_handler` is deprecated function please use `on`",
            DeprecationWarning,
        )
        self.on(event, handler)

    async def heartbeat(self):
        try:
            if self.ws is not None and not self.ws.closed:
                await self.ws.send_bytes(
                    self.packman.pack(heartbeat(), Operation.HEARTBEAT)
                )
                if const.TEST: print("[HB] OUT")
                return
        except (
            aiohttp.ClientConnectionError,
            asyncio.TimeoutError,
            ConnectionError,
            ConnectionResetError,
        ):
            await self.connect()  # 重新连接

    async def connect(self, retries=5):
        if const.TEST: print("连接中...")
        for i in range(retries):
            try:
                if not hasattr(self,"real_room_id") or not hasattr(self,"uname"):
                    self.real_room_id, self.uname = await get_blive_room_info(
                        self.room_id, self.aio_session
                    )
                url, token = await get_blive_ws_url(self.real_room_id, self.aio_session)
                self.ws = await self.aio_session.ws_connect(
                    url,
                    headers={'User-Agent': const.USER_AGENT,
                             'cache-control': 'no-cache',
                             'connection': 'Upgrade',
                             'pragma': 'no-cache',
                             'sec-websocket-extensions':'permessage-deflate; client_max_window_bits'
                             },
                    )
                # 发送认证
                await self.ws.send_bytes(
                    self.packman.pack(
                        certification(self.real_room_id, token, uid=self.uid),
                        Operation.AUTH,
                    )
                )
                if const.TEST: print("连接成功...")
                return
            except (
                aiohttp.ClientConnectionError,
                asyncio.TimeoutError,
                ConnectionError,
                ConnectionResetError,
            ):            
                
                if const.TEST: print("第", i, "次链接尝试失败")
                await asyncio.sleep(1)
        if const.TEST: raise aiohttp.ClientConnectionError("与服务器连接失败")

    async def listen(self):
        self.running = True
        # start listening
        # await self.connect()
        try:
            await self.connect()
        except Exception as e:
            print(f"An error occurred: {e}")

        # 开始30s发送心跳包的定时任务
        # self.scheduler.add_job(self.heartbeat, trigger="interval", seconds=30)
        # 开始5s发送心跳包的定时任务
        if const.TEST: print("保持连接，心跳间隔:", const.HB_time, "秒...")
        self.scheduler.add_job(self.heartbeat, trigger="interval", seconds=const.HB_time)
        self.scheduler.start()
        print("弹幕监听就绪...")

        # 开始监听
        while self.running:
            try:
                # 从live server pp对websocket的仿真发送来看，本机给本机发的消息都能收到，
                # 也就是说，这里receive不到的本质是ws没有发消息，或者中途被拦截了
                msg = await self.ws.receive(timeout=60)
                if msg.type in (
                    aiohttp.WSMsgType.CLOSING,
                    aiohttp.WSMsgType.CLOSED,
                    aiohttp.WSMsgType.ERROR,
                ):
                    if self.running:
                        await self.connect()  # reconnect
                        continue
                    else:
                        return 0
                if msg.type != aiohttp.WSMsgType.BINARY:
                    continue
                mq = self.packman.unpack(msg.data)
                ctxs = filter(lambda ctx: ctx.body.get("cmd", None), [BLiverCtx(self, m) for m in mq])
                for ctx in ctxs:
                    if const.TEST:
                        if ctx.body["cmd"] not in(Events.HEARTBEAT_REPLY) :
                            print(ctx.body["cmd"])
                    self.emit(ctx.body["cmd"], ctx)
            except (
                aiohttp.ClientConnectionError,
                ConnectionResetError,
                asyncio.TimeoutError,
            ) as e:
                if const.TEST: print(e)
                await self.connect()

    async def graceful_close(self):
        self.running = False
        self.scheduler.shutdown()
        await self.aio_session.close()
        await self.ws.close()

    def run(self):
        loop = asyncio.get_event_loop()
        # if const.TEST:    loop.run_until_complete(self.listen())
        loop.create_task(self.listen())
        loop.run_forever()

    def run_as_task(self):
        loop = asyncio.get_event_loop()
        return loop.create_task(self.listen())