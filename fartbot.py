'''
A simple discord bot built using the discord.py library

If there are syntax errors then it's most likely because some of the variable names were changed to be more appropriate

'''

import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

import urllib.request
import json

# bot setup
load_dotenv()
BOT = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


# --- sh!tpost commands ---
@client.command()
async def shart(ctx):
    await ctx.send("MURDER EKJNFA K!!!!!!!")

# sends a funny image of that guy with the monster energy drink with the caption "kill"
@client.command()
async def violence(ctx):
    await ctx.send("https://i.kym-cdn.com/photos/images/facebook/001/688/902/e4b.jpg")

# image that says "come here cupcake" multiple times
@client.command()
async def peace(ctx):
    await ctx.send("https://i.redd.it/gnp7p9f1jzz51.jpg")

# posts a funny stock photo of a man sleeping
@client.command()
async def goodnight(ctx):
    await ctx.send("https://comps.canstockphoto.com/maintaining-consistent-circadian-rhythm-stock-photo_csp77229249.jpg")


# --- actual commands ---

# prints ascii art based on args given
@client.command()
async def text(ctx, arg):
    # replace spaces in string provided with "+"
    s = arg.replace(" ", "+")
    # url is loaded
    url = "https://artii.herokuapp.com/make?text={}".format(s)
    uf = urllib.request.urlopen(url)
    # strip html from data + join lines
    l = [i.decode("utf-8") for i in uf]
    l = "".join(l)
    # send w/ ``` wrapped around the ascii cus it looks wonky otherwise
    await ctx.send("```" + l + "```")

# raises error if no args are provided
@text.error
async def text_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("please")

# provides recipes based on ingredients given
@client.command()
async def recipe(ctx, arg):
    # replaces spaces with commas
    s = arg.replace(" ", ",")
    # puts args in url and opens url
    url = "http://www.recipepuppy.com/api/?i={}&p=1".format(s)
    uf = urllib.request.urlopen(url)
    # parses data
    l = [i.decode() for i in uf]
    l = "\n".join(l)

    # loads the data as json to make
    l = json.loads(l)
    l = l["results"]

    results = []
    for i in l:
        results.append("**{}**".format(i["title"].strip()))
        results.append("**ingredients**: {}".format(i["ingredients"].strip()))
        results.append("**link**: <{}>\n".format(i["href"].strip()))

    results = "\n".join(results)
    await ctx.send(results)

# raised when no args are provided for !recipe
@recipe.error
async def recipe_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("please provide one or more ingredients - eg: &recipe 'onion cheese'")

# runs the bot
client.run(BOT)
