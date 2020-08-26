from discord.ext.commands import Bot as BotBase
from apscheduler.schedulers.asyncio import AsyncIOScheduler
PREFIX = "-"
OWNER_IDS = [221307082396139520]

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

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

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(698347986148655187)
            print("Bot ready")
        else:
            print("bot reconnected")

    async def on_message(self, message):
        pass

bot=Bot()