# AmongUs.py

import discord
from discord.ext import commands
from discord.utils import get


client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Among Us bot is ready!')

@client.command()
async def ping(ctx):
    await ctx.send('pong!')

@client.command()
async def test(ctx, role: discord.Role, user: discord.Member):
    await user.add_roles(role)
    await ctx.send(f'{user} now has role {role}.')

client.run('{BOT_TOKEN}')
