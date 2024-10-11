import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Logged as {bot.user}')

async def load():
    for filename in os.listdir('.\\cogs'):
        print(filename)
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load()
    
asyncio.run(main())
bot.run('MTI4NzY2ODYyOTYwMDQ2OTA0Mg.G6gErP.j7o3AhoynhUOHFIkSkT0VQc_HGXkW2MdXR49BA')
