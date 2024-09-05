import json
from discord import Embed
def update(length:int) -> dict:
    with open('db.json', 'r') as f:
        db:dict = json.loads(f.read())

    t10:dict = {"10":{"name": "", "count": 0},"9":{"name": "", "count": 0},"8":{"name": "", "count": 0},"7":{"name": "", "count": 0},"6":{"name": "", "count": 0},"5":{"name": "", "count": 0},"4":{"name": "", "count": 0},"3":{"name": "", "count": 0},"2":{"name": "", "count": 0},"1":{"name": "", "count": 0}, "debug": {"count": 9999999, "name": "DEBUG"}}
    for word in db: 
        if len(word) >= length if length > 0 else 1:
            if db[word] > t10["10"]["count"]:
                stop = False
                for place in range(10,0, -1):
                    if db[word] <= t10[str(place)]["count"]:
                        stop = True
                        if word != t10[str(place)]["name"]:
                            t10[str(place+1)]["name"] = word
                            t10[str(place+1)]["count"] = db[word]
                            break
                        
                if not stop:
                    t10[str(1)]["name"] = word
                    t10[str(1)]["count"] = db[word]
    return t10

def export(length:int) -> Embed:
    t10:dict = update(length)

    # leaderboard:str = ""

    # for i in range(1,11):
    #     leaderboard += f"{(' ' if i < 10 else '') + str(i)}: {t10[str(i)]['name']} - {t10[str(i)]['count']}\n"
    # return leaderboard
    embed = Embed(title="Leaderboard", color=0xff0000)
    embed.add_field(name=f"1. \t {t10['1'] ['name']} - {t10["1"] ["count"]}",value='', inline=False)
    embed.add_field(name=f"3. \t {t10['2'] ['name']} - {t10["2"] ["count"]}",value='', inline=False)
    embed.add_field(name=f"4. \t {t10['3'] ['name']} - {t10["3"] ["count"]}",value='', inline=False)
    embed.add_field(name=f"5. \t {t10['4'] ['name']} - {t10["4"] ["count"]}",value='', inline=False)
    embed.add_field(name=f"6. \t {t10['5'] ['name']} - {t10["5"] ["count"]}",value='', inline=False)
    embed.add_field(name=f"7. \t {t10['6'] ['name']} - {t10["6"] ["count"]}",value='', inline=False)
    embed.add_field(name=f"8. \t {t10['7'] ['name']} - {t10["7"] ["count"]}",value='', inline=False)
    embed.add_field(name=f"9. \t {t10['8'] ['name']} - {t10["8"] ["count"]}",value='', inline=False)
    embed.add_field(name=f"9. \t {t10['9'] ['name']} - {t10["9"] ["count"]}",value='', inline=False)
    embed.add_field(name=f"10. \t{t10['10']['name']} - {t10["10"]["count"]}",value='', inline=False)
    return embed

async def index(query:str) -> int:
    with open('db.json', 'r') as f:
        db:dict = json.loads(f.read())
    try: return db[query]
    except: return 0
