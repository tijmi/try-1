import json
from datetime import datetime
from pathlib import Path
import toml


def log_post(submission: tuple, outputplace: str):

    with open("config.toml", "r") as f:
        config = toml.load(f)

    timenow = datetime.now()
    data = {
        "id": submission[2],
        "title": submission[0],
        "subreddit": config["preferances"]["subreddit"],
        "time": timenow.strftime("%H:%M:%S"),
        "date": timenow.strftime("%m/%d/%Y"),
        "location": outputplace,
    }
    with open("log.json", "r+") as f:
        log = json.load(f)

        log["made posts"].append(data)

        f.seek(0)

        json.dump(log, f, indent=4)
        

def checkifdone(id:str):
    with open("log.json", "r") as f:
        log = json.load(f)

    done = True

    if id in log["made posts"].__str__():
        done = False

    return done

    
    
    