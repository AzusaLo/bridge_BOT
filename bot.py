import discord
from discord.ext import commands
import json

with open('bridge_BOT/setting.json', 'r', encoding='utf-8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='[')


@bot.event
async def on_ready():
    print(">> Bot is online <<")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['LOBBY_CHANNEL']))
    await channel.send(f'{member} join!')


@bot.event
async def on_member_leave(member):
    channel = bot.get_channel(int(jdata['LOBBY_CHANNEL']))
    await channel.send(f'{member} leave!')


@bot.command()
async def ping(ctx):
    await ctx.send(f'{bot.latency*1000:.3f} (ms)')

bot.run(jdata['TOKEN'])
