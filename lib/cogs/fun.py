from discord.ext.commands import Cog
from discord.ext.commands import command
from random import choice

class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="bardear nacho", aliases=["bn"])
    async def bardear_nacho(self, ctx):
        hola = "<@!361588573033594880>"
        await ctx.send(F"{hola}" " te voy a reportar por manco!")

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("fun") #paso fun por ser el nombre del archivo no de la clase
        print("fun cog ready")

def setup(bot):
    bot.add_cog(Fun(bot))
