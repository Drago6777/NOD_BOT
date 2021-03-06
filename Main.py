#!/usr/bin/python3
import datetime

import discord
from discord.ext import commands

import BotFunctions as bf
import FuzzworksFunctions as Fzw
import ZkillFunctions as Zkbf

# get token from file
tokenFile = open('token', 'r')
token = tokenFile.read()
# strip off any training whitespaces or newlines from end of file
token = token.rstrip()
bot = commands.Bot(command_prefix='!')



online_time = datetime.datetime.now()

# bot channel ID
channel = discord.Object(id='531113274201341955')


alertRunning = False


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(bf.roll_out_init())
    print('------')


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def upTime(ctx):
    await ctx.send("Online for: " + str(datetime.datetime.now() - online_time))

# zkill related functions


@bot.command()
async def kills(ctx, *, corp_name):
    await ctx.send(Zkbf.get_corp_current_month_stats(corp_name))


@bot.command()
async def ships(ctx, amount: int, *, corp_name):
    await ctx.send(Zkbf.get_killer_summary(amount, corp_name))


@bot.command()
async def stats(ctx, *, corp_name):
    await ctx.send(Zkbf.get_fleet_size_stats(corp_name))


@bot.command()
async def rankings(ctx):
    await ctx.send(bf.get_ranked_isk_killed())


@bot.command()
async def intel(ctx, *, corp_name):
    await ctx.send(Zkbf.get_intel(corp_name))


@bot.command()
async def fit(ctx, ship: str, *, corp):
    await ctx.send(Zkbf.get_last_fit(ship, corp))


# market functions


@bot.command()
async def pc(ctx, *, a):
    await ctx.send(Fzw.get_item_value(a))


@bot.command()
async def fuel(ctx):
    await ctx.send(Fzw.get_fuel_prices())


# Rollout Tracker ---------------------------------


@bot.command()
async def rolled(ctx, name: str):
    await ctx.send(bf.update_rolled_out(name))


@bot.command()
async def lastRolled(ctx):
    await ctx.send(bf.get_rolled_out_date())


# ping-command -----------------------------------
@bot.command()
async def batphone(ctx, ping_text):
    target_channel = "440447527905394689"
    # await ctx.send("Ping Sending")
    ctx.send_message(discord.Object(id=target_channel), "@everyone " + ping_text)
    # await ctx.send("Ping Sent")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        print("Command Not Found")
        bot.send_message(channel, "Command Not Found")
        return




bot.run(token)
