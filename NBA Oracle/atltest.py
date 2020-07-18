import requests
import json


# ATLANTA Last Game 134880
hawksLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134880")

LGdataATL = hawksLG.text
LGparseATL = json.loads(LGdataATL) 

homeScoreATL = LGparseATL["results"][0]["intHomeScore"]
awayScoreATL = LGparseATL["results"][0]["intAwayScore"]

scoreHome = (homeScoreATL)
scoreAway = (awayScoreATL)

print(homeScoreATL)  # This prints as NULL or none type parce que il n'y avait pas de jeu joue

# print(json.dumps(LGparseATL, indent=4))