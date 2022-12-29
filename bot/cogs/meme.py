import discord
from discord import app_commands
from discord.ext import commands

class Meme(commands.Cog):
    def __init__(self,client):
        self.client = client

    #Ready Message in Console
    @commands.Cog.listener()
    async def on_ready(self):
        print("Meme command is ready!")

    #Command
    @app_commands.command(name="meme", description="Blesses you with a variety of memes")
    @app_commands.describe(options='Choose the meme you would like')
    @app_commands.choices(options=[
        discord.app_commands.Choice(name='Thot', value="https://i.imgur.com/RoJ9IYz.jpg"),
        discord.app_commands.Choice(name='Bueno', value="https://i.imgur.com/a4pQcxn.jpg"),
        discord.app_commands.Choice(name='Wodl', value="https://i.imgur.com/9G7fL7l.jpg"),
        discord.app_commands.Choice(name='Flat Fuck', value="https://imgur.com/a/Z4lHs7r"),
        discord.app_commands.Choice(name='Will Smith', value="https://tenor.com/view/will-smith-doom-eternal-gif-18735959"),
    ])
    async def meme(self, interaction: discord.Interaction, options: discord.app_commands.Choice[str]):
        await interaction.response.send_message(f"{options.value}")

async def setup(client):
    await client.add_cog(Meme(client))