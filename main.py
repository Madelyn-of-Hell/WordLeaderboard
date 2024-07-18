from tokens import TOKEN
import leaderboard
import discord
import json
import re
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
db:dict = {}
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
        await message.channel.send('```'+leaderboard.export(int(message.content[12:len(message.content)]))+'```')
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
    print(message.content)
    print(db)


    




client.run(TOKEN)