from discord.ext import commands
from discord.ext import tasks
import discord
import config
import asyncio
import os
import random
import calendar
import datetime

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=config.COMMAND_PREFIX, intents=intents, application_id=config.APPLICATION_ID, activity=discord.Activity(type=discord.ActivityType.watching, name="Nichijou"))

# Getting unix timestamp for when the bot started
date_start = datetime.datetime.now(datetime.timezone.utc)
utc_time_start = calendar.timegm(date_start.utctimetuple())

@bot.event
async def on_ready():
    print('shinonome nano desu!')
    nano_hour.start() # starting hourly nano

async def load():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}') # loading cogs

@tasks.loop(hours=1)
async def nano_hour():
    channel = bot.get_channel(config.CHANNEL_ID)
    date = datetime.datetime.now(datetime.timezone.utc)
    utc_time = calendar.timegm(date.utctimetuple())
    path = random.choice(os.listdir('./images/'))
    await channel.send(file=discord.File("./images/"+path), content=
        'sending Nano every hour! <a:NanoHype:1121146993406918686>\n\ngoing since <t:'
        + str(utc_time_start)
        + ':F>\ncurrent time: <t:'
        + str(utc_time) + ':F>')

    print("Sent nano image at " + (str(datetime.datetime.now())))

async def main():
    await load()
    await bot.start(config.TOKEN)

asyncio.run(main())