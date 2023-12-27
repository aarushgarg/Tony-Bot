import discord
import random
import asyncio
from discord.ext import commands, tasks

TOKEN = 'MTE4OTQzNTU2NTQzNTc4OTQ0Mg.GOaZfx.ej-wIfcIZhilMfhYS_CY1D7cqgBnt_bXXd5BbY'

messages = [
    "Tony bait",
    "Ting a Ling",
    "Coin clutcha"
]

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@tasks.loop(minutes=.1)
async def send_random_message():
    channel_id = 1182800728947957891


    channel = bot.get_channel(channel_id)


    await channel.send(random.choice(messages))

@bot.event
async def on_message(message):
    await bot.process_commands(message)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    send_random_message.start()

bot.run(TOKEN)

#bot invite URL: https://discordapp.com/api/oauth2/authorize?scope=bot&client_id=xxxxx <-- put in client id from dev. portal