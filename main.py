# bot.py
import discord
from discord.ext import commands
from classes.bot import Bot
import os

from library import key, constants

dir_path = os.path.dirname(os.path.realpath(__file__))

bot = commands.Bot(command_prefix = ">")

boRobot = Bot(language="EN")

@bot.event
async def on_ready():
    if boRobot.language == "FR":
        print(constants.TEXT["FR"]["on_ready"])
    if boRobot.language == "EN":
        print(constants.TEXT["EN"]["on_ready"])

@bot.event
async def on_member_join(member):
    if boRobot.language == "FR":
        print(str(member) +" "+ constants.TEXT["FR"]["on_member_join"])
    if boRobot.language == "EN":
        print(str(member) +" "+ constants.TEXT["EN"]["on_member_join"])

@bot.event
async def on_member_remove(member):
    if boRobot.language == "FR":
        print(str(member) + constants.TEXT["FR"]["on_member_remove"])
    if boRobot.language == "EN":
        print(str(member) + constants.TEXT["EN"]["on_member_remove"])

@bot.command()
async def ping(ctx):
    if boRobot.language == "FR":
        await ctx.send( constants.TEXT["FR"]["ping"] + round(bot.latency*1000) + "ms")
    if boRobot.language == "EN":
        await ctx.send( constants.TEXT["EN"]["ping"] + round(bot.latency*1000) + "ms")


"""
@bot.command(aliases=['8ball', 'ditMoi'])
async def _8ball(ctx, *args, **kwargs):
"""  

bot.run(key.getKey(os.path.join(dir_path, "key.txt")))


