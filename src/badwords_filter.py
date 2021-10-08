import discord

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):
    if not message.author.bot:
        badwords = ["twitter", "facebook", "instagram"]
        for word in message.content.split():
            if word.lower() in badwords:
                await message.delete()