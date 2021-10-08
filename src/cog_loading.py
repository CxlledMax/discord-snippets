import os
from discord.ext import commands

client = commands.Bot(command_prefix="!")

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        client.load_extension(f"cogs.{file.replace('.py', '')}")