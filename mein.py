import discord

client = discord.Client(activity=discord.Game(name='my game'))

# or, for watching:
activity = discord.Activity(name='起動中', type=discord.ActivityType.watching)
client = discord.Client(activity=activity)

client.run("ODQyOTc5OTU1Njc1NjI3NTI0.YJ9MQw.9rl6blRacfecuLFZe1aF_9b895Q")
