import discord
import json
import os
from discord.ext import commands
from prsaw import RandomStuff

client= commands.Bot(command_prefix="!!", case_insensitive=True)
client.remove_command("help")
re= RandomStuff()
with open("config.json", "r") as f:
	config= json.load(f)
	f.close()

TOKEN= config['token']
extensions= [
"commands",
]

@client.event
async def on_ready():
	for extension in extensions:
		client.load_extension(f"cogs.{extension}")

	if os.name == 'nt':
		os.system("cls")
	else:
		os.system('clear')

	print("[ Discord ChatBot ]\n")
	print(f"\nCurrently Logged in as: {client.user.name}")
	print(f"ID: {client.user.id}")