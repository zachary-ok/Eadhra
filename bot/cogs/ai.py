import discord
from discord import app_commands
from discord.ext import commands
import openai
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
openai.api_key=os.getenv('OPENAI_API_KEY')

class AI(commands.Cog):
    def __init__(self,client):
        self.client = client

    #Ready Message in Console
    @commands.Cog.listener()
    async def on_ready(self):
        print("AI command is ready!")

    #Command
    @app_commands.command(name="ai", description="Interact with AI using OpenAI's GPT-3 & Dall-E")
    @app_commands.describe(model='Choose which AI you would like to querey')
    @app_commands.choices(model=[
        discord.app_commands.Choice(name='Dall-E', value="1"),
        discord.app_commands.Choice(name='GPT-3', value="2"),
    ])
    @app_commands.describe(prompt='State your prompt to the AI')
    async def ai(self, interaction: discord.Interaction, model: discord.app_commands.Choice[str], prompt: str):
        await interaction.response.defer(ephemeral=True)
        await interaction.followup.send(content=f"*{model.name}*, `{prompt}`\n waiting for generation...", ephemeral=True)

        if model.name == "Dall-E":
            response = openai.Image.create(
                prompt=prompt,
                size="256x256"
            )
            generation=response['data'][0]['url']
        else: 
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                max_tokens=60,
                temperature=0.5,
                top_p=0.3,
                frequency_penalty=0.5,
                presence_penalty=0.0
            )
            generation = response['choices'][0]['text']
            generation = generation.strip('\n')
        
        await interaction.channel.send(content=f"{interaction.user.mention}\n*{model.name}*, `{prompt}`\n{generation}")
        await interaction.delete_original_response()
        

async def setup(client):
    await client.add_cog(AI(client))