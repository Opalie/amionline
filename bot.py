import discord
from discord.ext import commands
from config import BOT_TOKEN

# End my misery

intents = discord.Intents.default()
intents.members = True  # Subscribe to the privileged members intent.
bot = commands.Bot(command_prefix='$', intents=intents)

# Who are you?

class MyContext(commands.Context):
    async def tick(self, value):
        emoji = '\N{WHITE HEAVY CHECK MARK}' if value else '\N{CROSS MARK}'
        try:
            await self.message.add_reaction(emoji)
        except discord.HTTPException:
            pass

# Make it not respond to itself iirc?

class MyBot(commands.Bot):
    async def get_context(self, message, *, cls=MyContext):
        return await super().get_context(message, cls=cls)

# Ping Pong

@bot.command()
async def hello(ctx):
    await ctx.send("Do you need anything?")

# Get pinged user avatar "$avatar @user"

@bot.command()
async def avatar(ctx, *, avamember : discord.Member = None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)


# Let's try to get the bot to at least say that someone goes offline.

@bot.event
async def on_member_update(before, after):
  print(after.raw_status)

bot.run(BOT_TOKEN)