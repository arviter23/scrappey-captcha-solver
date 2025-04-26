import nextcord
from nextcord.ext import commands
bot = commands.Bot(command_prefix="!")
intents = nextcord.Intents.default()
intents.message_content = True

@bot.command(name="hi")
async def SendMessage(ctx):
    await ctx.send('Hello!')
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

if __name__ == '__main__':
    bot.run("MTM2NTY3MzkyMDIyMDM2ODk5OA.GZEDFC.M9jWgZLHX-fqZXb5-Cb0bOJo2QclKFOwDR5kM4")
