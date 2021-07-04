# bot.py
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
import random


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='assign')
async def assign(ctx, people, tasks):
    print(people)
    print(tasks)
    response = []
    people_array = people.split(',')
    tasks_array = tasks.split(',')
    random.shuffle(people_array)
    for i,task in enumerate(tasks_array):
        response.append(f"**{task}**:`{people_array[i]}`")
    await ctx.send("\n".join(response))

bot.run(TOKEN)