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
    await boRobot.send(ctx, constants.TEXT["FR"]["ping"] + str(round(bot.latency*1000)) + "ms") 

@bot.command(aliases=['temp', 'cpuTemp'])
async def _temp(ctx):
    await boRobot.send(ctx, boRobot.getCpuTemp())

@bot.command(aliases=['talk', 'tts'])
async def _talk(ctx):
    boRobot.ttsSwitch()
    await boRobot.send(ctx, "Ma variable: talk = " + str(boRobot.talk))

bot.run(key.getKey(os.path.join(dir_path, "key.txt")))


