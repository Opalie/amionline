import discord
from discord.ext import commands
from config import BOT_TOKEN

intents = discord.Intents.default()
intents.members = True  # Subscribe to the privileged members intent.
bot = commands.Bot(command_prefix='$', intents=intents)
# I was told not to use both discord.Client and commands.Bot but let's try because I'm lost
client = discord.Client(intents=intents)

class MyContext(commands.Context):
    async def tick(self, value):
        emoji = '\N{WHITE HEAVY CHECK MARK}' if value else '\N{CROSS MARK}'
        try:
            await self.message.add_reaction(emoji)
        except discord.HTTPException:
            pass

class MyBot(commands.Bot):
    async def get_context(self, message, *, cls=MyContext):
        return await super().get_context(message, cls=cls)


# Doesn't work
class MyClient(discord.Client):
    async def on_user_update(self, before, after):
        print("{} is {}.".format(after.name,after.status))

# Ping Pong

@bot.command()
async def hello(ctx):
    await ctx.send("Do you need anything?")

# "$avatar @user"

@bot.command()
async def avatar(ctx, *, avamember : discord.Member = None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

# No idea of which token to get for client, gotta have a look
client.run()
bot.run(BOT_TOKEN)
