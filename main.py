import os
import discord
from server import keep_alive

client = discord.Client(activity=discord.Game(name='my game'))

# or, for watching:
activity = discord.Activity(name='起動中', type=discord.ActivityType.watching)
client = discord.Client(activity=activity)

keep_alive()

client.run("token")
