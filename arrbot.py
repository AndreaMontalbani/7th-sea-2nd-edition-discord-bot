# This example requires the 'members' privileged intents
import itertools
import re

import discord
from discord.ext import commands
import random

token='addyourtokenhere'
client = commands.Bot(command_prefix= '!')

def coupling(throw, x, target):
    for c in itertools.combinations(throw, x):
        if sum(list(c)) == target:
            for i in c:
                throw.remove(i)
            return 1, throw
    return 0, throw


def calcIncrements(throw):
    incr = 0
    # preprocessing
    while 10 in throw:
        incr = incr + 1
        throw.remove(10)
    for t in range(10, 20):
        for x in range(2, len(throw)):
            newincr, throw = coupling(throw, x, t)
            incr = incr + newincr
            if 20 > sum(throw) > 10:
                incr = incr + 1
                return incr
            elif sum(throw) < 10:
                return incr
    return incr

@client.event
async def on_ready():
    print('Arrrrrr bot is ready')

@client.event
async def on_member_join(member):
    print('Welcome on board {member}, arrrrrr!')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command(aliases=['r','rol'])
async def roll(ctx,*, rollarg):
    if rollarg.isnumeric():
        dnum=int(rollarg)+1
    results=[random.randint(1,10) for x in range (1,dnum)]
    await ctx.send(results)
    incr=calcIncrements(results)
    await ctx.send(incr)

@client.command()
async def h(ctx):
    helpmess='!h !help prints this message\n' \
             '!r <n> !roll <n> rolls n dice, returns the roll, increments and unused dice'
    await ctx.send(helpmess)


client.run(token)