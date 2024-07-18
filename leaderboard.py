import json

def update():
    with open('db.json', 'r') as f:
        db:dict = json.loads(f.read())

    t10:dict = {"10":{"name": "", "count": 0},"9":{"name": "", "count": 0},"8":{"name": "", "count": 0},"7":{"name": "", "count": 0},"6":{"name": "", "count": 0},"5":{"name": "", "count": 0},"4":{"name": "", "count": 0},"3":{"name": "", "count": 0},"2":{"name": "", "count": 0},"1":{"name": "", "count": 0}, "debug": {"count": 9999999, "name": "DEBUG"}}
    for word in db: 
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
            
    with open('t10.json', 'w') as f:
        f.write(json.dumps(t10))

def export() -> str:
    update()
    with open('t10.json', 'r') as f:
        t10 = json.load(f)
    leaderboard:str = ""
    
    for i in range(1,11):
        leaderboard += f"{(' ' if i < 10 else '') + str(i)}: {t10[str(i)]['name']} - {t10[str(i)]['count']}\n"
    return leaderboard