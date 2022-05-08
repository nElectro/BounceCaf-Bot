import nextcord
from nextcord.ext import commands
from nextcord import ButtonStyle
from nextcord.ui import Button, View
import random
import aiohttp
import json
import requests


intents = nextcord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = "b!", case_insensitive=True, intents=intents)

@bot.event
async def on_ready():
    print("{0.user}".format(bot))
    print("------------------")
    await bot.change_presence(activity=nextcord.Game(name="Bounce Café"))


@bot.command()
async def game(ctx):
    style = ButtonStyle.green
    button = Button(label="Join Game!", style=style, url="https://www.roblox.com/games/9414248414")
    view = View()
    view.add_item(button)
    await ctx.send("Play Now!", view=view)


@bot.command()
async def group(ctx):
    style = ButtonStyle.green
    button = Button(label="Join Now!", style=style, url="https://www.roblox.com/groups/3278742")
    view = View()
    view.add_item(button)
    await ctx.send("Join Now!", view=view)


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : nextcord.Member, *, Reason=None):
    if Reason == None:
        Reason = "No Reason Has Been Provided."
    await ctx.guild.ban(member)
    await ctx.send(f"{member.mention} has been banned for: {reason}")   

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : nextcord.Member, *, Reason=None):
    if Reason == None:
        Reason = "No Reason Provided."
    await ctx.guild.kick(member)
    await ctx.send(f"{member.mention} has been kicked for: {reason}")    

@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def luck(ctx, *, question):
    if question == None:
        await ctx.reply("No question made, so i can't awnser it.")
    else:    
        responses = ['As I see it, yes.',
                    'Yes.',
                        'Positive',
                        'From my point of view, yes',
                        'Convinced.',
                        'Most Likley.',
                        'Chances High',
                        'No.',
                        'Negative.',
                        'Not Convinced.',
                        'Perhaps.',
                        'Not Sure',
                        'Mayby',
                        'I cannot predict now.',
                        'Im to lazy to predict.',
                        'I am tired. *proceeds with sleeping*'
                ]
        awnser = random.choice(responses)
        await ctx.reply(f"{awnser}. The lucky charmer has made its response")

@bot.command()
async def meme(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json') as r:
            res = await r.json()
            await ctx.send(res['data']['children'] [random.randint(0, 25)]['data']['url'])

@bot.command()
async def information(ctx):
    embed=nextcord.Embed(title="Information")
    embed.set_author(name="M1GVUEL", url="https://www.roblox.com/users/354323493")
    embed.add_field(name="<:developer:972560171719073852> Developer", value="`M1GVUEL / miguel;#2727`", inline=False)
    embed.add_field(name="<:heroku:972560171547111454> Server", value=f"Local Host", inline=False)
    embed.add_field(name="<:heroku:972560171547111454> Server", value=f"Local Host", inline=False)
    embed.add_field(name="<:wifi:972560171563905054> Ping (MS)", value="{0} ms".format(round(bot.latency * 1000)), inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def search(ctx, userid):
    response = requests.get(f'https://verify.eryn.io/api/user/{userid}')
    username = response.json()['robloxUsername']
    user_id = response.json()['robloxId']

    embed=nextcord.Embed(title="This is what i found")
    embed.set_thumbnail(url=f"https://roblox.com/Thumbs/Avatar.ashx?x=100&y=100&Format=Png&userid={user_id}")
    embed.add_field(name="Username", value=f"`{username}`", inline=False)
    embed.add_field(name="User ID", value=f"`{user_id}`", inline=True)
    await ctx.send(embed=embed)
        
bot.run("TOKEN")    

