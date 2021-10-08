import os
from discord.ext import commands

client = commands.Bot(command_prefix="!")

bypass_directories = ["example"]
subdirectories = [directory.path.replace(".\\", "") for directory in os.scandir(".") if directory.is_dir()]

for subdir in subdirectories:
    if subdir not in bypass_directories:
        for file in os.listdir(subdir):
            if file.endswith(".py"):
                client.load_extension(f"{subdir}.{file.replace('.py', '')}")
                print(f"[{subdir}] Extension {file.replace('.py', '')} successfully loaded")