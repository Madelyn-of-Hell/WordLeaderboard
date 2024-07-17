import json

def Update():
    with open('db.json', 'r') as f:
        db:dict = json.loads(f.read())

    try: open('t10.json', 'x')
    except: 
        with open('t10.json', 'r') as f:
            t10:dict = json.loads(f.read())

    