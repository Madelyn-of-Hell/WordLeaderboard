from tokens import TOKEN
import discord
import json
import re
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
db:dict = {}
t10:dict = {}
try: open('db.json', 'x')
except: 
    with open('db.json', 'r') as f:
        db:dict = json.loads(f.read())

try: open('t10.json', 'x')
except: 
    with open('t10.json', 'r') as f:
        t10:dict = json.loads(f.read())

@client.event
async def on_ready():
    print('connected and loaded!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    leaderboard:str = ""
    for i in db:
        leaderboard += f"{i}: {db[i]}\n"
    if message.content.strip() == '!leaderboard': await message.channel.send('```'+leaderboard+'```')

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