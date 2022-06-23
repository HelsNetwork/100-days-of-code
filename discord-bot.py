import os
import discord

intents = discord.Intents(messages=True, guilds=True)

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f"{client.user.name} has connected to Discord!")


@client.event
async def on_member_join(member):
    await member.send(f"Hello {member.name}, welcome to my Discord server!!")


client.run(TOKEN)
