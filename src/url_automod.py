import discord, re

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):
    if not message.author.bot:
        if re.search("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", message.content) != None:
            await message.delete()