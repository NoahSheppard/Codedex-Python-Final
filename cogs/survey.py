import discord
from discord import app_commands
from discord.ext import commands
import requests, json

class Survey(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Survey cog loaded.')

    @commands.command()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync()
        await ctx.send(
          f"Synced {len(fmt)} commands to the current guild."
        )
        return

    @app_commands.command(name="meme", description="Get a meme")
    @app_commands.describe(memes='Genres to choose from')
    @app_commands.choices(memes=[
        discord.app_commands.Choice(name='programming', value=1),
        discord.app_commands.Choice(name='general', value=2),
    ])
    async def choosecolour(self, interaction: discord.Interaction, memes: discord.app_commands.Choice[int]):
        response = requests.get('https://meme-api.com/gimme/programmingmemes') if memes.name == 'programming' else requests.get('https://meme-api.com/gimme')
        json_data = json.loads(response.text)
        await interaction.response.send_message(json_data['url'])

async def setup(bot):
    await bot.add_cog(Survey(bot))