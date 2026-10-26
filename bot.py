import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send("Pong ! 🏓")


@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel:
        await channel.send(f"Bienvenue {member.mention} ! 👋")


bot.run("MTU2NDIxMjk3OTMxMzE1NjE0Nw.GA29mm.y4JC_eTaL2y1ZUgGY4HBKZGj7syzp8bu-r2WU4")
