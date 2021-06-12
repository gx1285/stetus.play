import os
import discord
from server import keep_alive

client = discord.Client()



keep_alive()

client.run("token")
