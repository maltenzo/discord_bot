from discord.ext.commands import Bot as BotBase
from discord.ext.commands import CommandNotFound
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from glob import glob
from asyncio import sleep
from ..db import db
PREFIX = "-"
OWNER_IDS = [221307082396139520]
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]


class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)

    def ready_up(self, cog):
        setattr(self, cog, True)

    def all_ready(self):
        return all([getattr(self, cog) for cog in COGS])







class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()
        self.cogs_ready = Ready()
        db.autosave(self.scheduler)
        super().__init__(command_prefix = PREFIX, owner_ids = OWNER_IDS)

    def setup(self):
        for cog in COGS:
            self.load_extension(f"lib.cogs.{cog}")
            print("cog loaded")
        print("setup complete")

    def run(self, version):
        self.VERSION = version
        print("running setup")
        self.setup()
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

            self.guild = self.get_guild(698347986148655187)
            self.scheduler.start()
            self.stdout = self.get_channel(698347986148655190)

            while  not self.cogs_ready.all_ready():
                    await sleep(0.3)


            self.ready = True
            print("Bot ready")
            #await self.stdout.send("Que onda perro!?!?!?!?!?!?!?")

        else:
            print("bot reconnected")

    async def on_message(self, message):
        pass

bot=Bot()
