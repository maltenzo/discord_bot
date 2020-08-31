from discord.ext.commands import Bot as BotBase
from discord.ext.commands import CommandNotFound
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from ..db import db
PREFIX = "-"
OWNER_IDS = [221307082396139520]

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        db.autosave(self.scheduler)
        super().__init__(command_prefix = PREFIX, owner_ids = OWNER_IDS)

    def run(self, version):
        self.VERSION = version
        with open("./lib/bot/token.0", "r" , encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("running bot...")
        super().run(self.TOKEN, reconnect = True)

    async def on_connect(self):
        print("bot online")

    async def on_disconect(self):
        print("bot offline")

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            await args[0].send("something went wrong")
        raise

    async def on_command_error(self, ctx, exc)    :
        if isinstance(exc, CommandNotFound):
            pass
        elif hassattr(exc, "original"):
            raise exc.original
        else:
            raise exc

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(698347986148655187)
            self.scheduler.start()
            print("Bot ready")

            channel = self.get_channel(698347986148655190)
            #await channel.send("Que onda perro!?!?!?!?!?!?!?")
        else:
            print("bot reconnected")

    async def on_message(self, message):
        pass

bot=Bot()
