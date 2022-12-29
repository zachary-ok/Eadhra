import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv, find_dotenv

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
load_dotenv(find_dotenv()) #Finds .env and loads it

#Startup Actions
@client.event
async def on_ready():
    await client.tree.sync() #Sync Command Tree
    print("Bot is online!") #Ready message in console
    await client.change_presence(activity=discord.Game("/help")) #Sets bot status

#Cog loader
async def load(): 
    for filename in os.listdir("./cogs"): #For testing purposes use "./bot/cogs"
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:
        await load()
        await client.start(os.getenv('DISCORD_TOKEN')) #Passes .env and Discord Bot Token for login

asyncio.run(main()) #Runs above function