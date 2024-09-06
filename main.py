from tokens import TOKEN
import leaderboard
# import matplotlib
import asyncio
import discord
import json
import re
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
db:dict = {}
mabdie = discord.User
tree = discord.app_commands.CommandTree(client)
try: open('db.json', 'x')
except: 
    with open('db.json', 'r') as f:
        db:dict = json.load(f)


@client.event
async def on_ready():
    await tree.sync()
    print('connected and loaded!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if  '!suggest' in message.content.strip() and message.content.strip()[0] == '!': 
        await suggest('566579790556037140', message.content[8:])
        return
    if  '!index' in message.content.strip() and message.content.strip()[0] == '!': 
        await message.channel.send('`'+message.content[6:].strip() +':\t' + str(await leaderboard.index(message.content[6:].strip()))+'`')
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

@tree.command(
    name="leaderboard",
    description="Displays the leaderboard as an embed."
    )
async def leaderboard_command(interaction):
    embeds = leaderboard.export(1)
    await interaction.response.send_message(embed=embeds)

@tree.command(
    name="reset",
    description="a debug command, currently available only to the creator."
    )
async def reset_command(interaction, target:str):
    if interaction.user.id == 566579790556037140:
        db[target] = 0
        with open('db.json', 'w') as f:
            f.write(json.dumps(db))
        await interaction.response.send_message('`'+target +' has been reset to 0!''`')
    else:
        await interaction.response.send_message(f'`{interaction.user.capitalize()} has no admin permissions. BEGONE, HEATHEN!`')
    return

@tree.command(
    name="index",
    description="Displays the count for a requested value."
    )
async def index_command(interaction, index_value:str):
    embeds = await leaderboard.index(index_value)
    await interaction.response.send_message(embed=embeds)



client.run(TOKEN)