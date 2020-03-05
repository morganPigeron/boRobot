# bot.py
import discord
from discord.ext import commands
from classes.bot import Bot
import os

from library import key, constants

dir_path = os.path.dirname(os.path.realpath(__file__))

bot = commands.Bot(command_prefix = ">")

boRobot = Bot()

@bot.event
async def on_ready():
    print(constants.TEXT["FR"]["on_ready"])


"""
@bot.event
async def on_member_join(member):
    print(str(member) +" "+ constants.TEXT["FR"]["on_member_join"])


@bot.event
async def on_member_remove(member):
    print(str(member) + constants.TEXT["FR"]["on_member_remove"])
"""

@bot.command(aliases=['ping', 'latency', 'latence'])
async def _ping(ctx):
    await ctx.send(boRobot.print(constants.TEXT["FR"]["ping"] + str(round(bot.latency*1000)) + "ms"))

@bot.command(aliases=['temp', 'cpuTemp'])
async def _temp(ctx):
    await ctx.send(boRobot.print(boRobot.getCpuTemp()))

@bot.command(aliases=['speech', 'talk'])
async def _talk(ctx):
    if boRobot.speech :
        boRobot.speech = False
        await ctx.send(boRobot.print("Talk deactivated"))
    else : 
        boRobot.speech = True
        await ctx.send(boRobot.print("Talk activated"))
    

bot.run(key.getKey(os.path.join(dir_path, "key.txt")))


