import discord
from discord import app_commands
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self,client):
        self.client = client

    #Ready Message in Console
    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping command is ready!")

    #Command
    @app_commands.command(name="ping", description="Demonstrates bot latency in milliseconds")
    async def ping(self, interaction: discord.Interaction):
        bot_latency = round(self.client.latency * 1000)

        await interaction.response.send_message(f"*Pong!* `{bot_latency} ms`")

async def setup(client):
    await client.add_cog(Ping(client))