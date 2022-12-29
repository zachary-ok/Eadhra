import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv, find_dotenv

intents = discord.Intents.all()

client = discord.Client(intents=intents)
load_dotenv(find_dotenv())

#Startup Actions
@client.event
async def on_ready():
    await client.tree.sync()
    await client.change_presence(activity=discord.Game("/help"))
    print("Bot is online!")

#Cog loader
async def load(): 
    for filename in os.listdir("./cogs"): #For testing purposes use "./bot/cogs"
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:
        await load()
        await client.start(os.getenv('DISCORD_TOKEN')) 

asyncio.run(main())