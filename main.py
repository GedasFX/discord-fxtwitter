import discord
import os
import re

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    content = message.content

    if re.search(r'https:\/\/(x|twitter)\.com', content) == None:
        return

    sub = re.sub(r'https:\/\/(x|twitter)\.com', 'https://fxtwitter.com', content)

    await message.channel.send(f"{message.author.mention} posted a boring twitter link:\n{sub}", silent=True, allowed_mentions=discord.AllowedMentions(users=False))
    await message.delete()

client.run(os.environ["DISCORD_TOKEN"])