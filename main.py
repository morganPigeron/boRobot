# bot.py
import discord
from discord.ext import commands

def getKey(fileName):
    file = open(fileName)
    key = file.readline()
    return key

bot = commands.Bot(command_prefix = ">")

@bot.event
async def on_ready():
    print("BoRobot est là !")

@bot.event
async def on_member_join(member):
    print(f"{member} est maintenant parmis nous.")

@bot.event
async def on_member_remove(member):
    print(f"{member} est parti :( ")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Mon temps de réaction : {round(bot.latency*1000)} ms")
"""
@bot.command(aliases=['8ball', 'ditMoi'])
async def _8ball(ctx, *args, **kwargs):
"""  

bot.run(getKey("key.txt"))


