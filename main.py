import discord
import os
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

number = 1

@client.event
async def on_message(message):
  global number
  if message.author == client.user:
    return
  a = message.content
  if "hi" in [x.lower() for x in a.split()]:
    number += 1
    await message.channel.send(f"hi {str(number)}");
  if "test" in a:
    await message.author.send("Testing...")

token = os.environ.get("DISCORD_BOT_SECRET")
keep_alive()
client.run(token)
