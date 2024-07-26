from tokens import TOKEN
import leaderboard
import asyncio
import discord
import json
import re
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
db:dict = {}
mabdie = discord.User

try: open('db.json', 'x')
except: 
    with open('db.json', 'r') as f:
        db:dict = json.load(f)


@client.event
async def on_ready():
    print('connected and loaded!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if  '!leaderboard' in message.content.strip() and message.content.strip()[0] == '!': 
        try: min = int(message.content[12:])
        except: min = 0
        await message.channel.send('```'+leaderboard.export(min)+'```')
        return
    if  '!suggest' in message.content.strip() and message.content.strip()[0] == '!': 
        await suggest('566579790556037140', message.content[8:])
        return
    if  '!index' in message.content.strip() and message.content.strip()[0] == '!': 
        await message.channel.send('`'+message.content[6:].strip() +':\t' + str(await leaderboard.index(message.content[6:].strip()))+'`')
        return
    if  '!reset' in message.content.strip() and message.content.strip()[0] == '!': 
        if message.author == await client.fetch_user('566579790556037140'):
            db[message.content.strip()[7:]] = 0
            await message.channel.send('`'+message.content.strip()[7:] +' has been reset to 0!''`')
        else:
            await message.channel.send(f'`{message.author} has no admin permissions. BEGONE, HEATHEN!`')
            discord.Embed
        return

    words:list = message.content.strip().split(' ')

    for word in words: word.splitlines()
    
    for word in words:
        if word in db:
            db[word] += 1
        else:
            db[word] = 1
    with open('db.json', 'w') as f:
        f.write(json.dumps(db))

async def suggest(user: str, content):
    user = await client.fetch_user(user)
    await user.send(content)




client.run(TOKEN)