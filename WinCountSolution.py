# HERE IS SOMETHING THAT CAN PROJECT A WIN OR LOSS FOR BOSTON 

import requests
import json

# CELTICS General Info 134860
celticsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Boston%20Celtics")
# CELTICS Last Game 134860
celticsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134860")
# CELTICS Next Game 134860
celticsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134860")

# CELTICS General Info Parse
dataBOS = celticsRE.text
parseBOS = json.loads(dataBOS)

# CELTICS Last Game Parse
LGdataBOS = celticsLG.text
LGparseBOS = json.loads(LGdataBOS)

# CELTICS Next Game Parse
NGdataBOS = celticsNG.text
NGparseBOS = json.loads(NGdataBOS)

homeTeamBOS = LGparseBOS["results"][0]["strHomeTeam"]
awayTeamBOS = LGparseBOS["results"][0]["strAwayTeam"]
homeScoreBOS = LGparseBOS["results"][0]["intHomeScore"]
awayScoreBOS = LGparseBOS["results"][0]["intAwayScore"]

# Last Game Info Printout CELTICS
celticsHome = "Home: " + str(homeTeamBOS) + " " + str(homeScoreBOS)
celticsAway = "Away: " + str(awayTeamBOS) + " " + str(awayScoreBOS)

print(celticsHome)
print(celticsAway)

focusTeam = homeTeamBOS
oppTeam = awayTeamBOS


def callWinner():
    if str(homeScoreBOS) > str(awayScoreBOS):
        return focusTeam


winner = callWinner()
print(winner)


def countWin1():
    if winner == "Boston Celtics":
        print("W")


countWin1()


def countLoss1():
    if winner != "Boston Celtics":
        print("L")


countLoss1()


# So NOW Count the W's and L's and then Parse them
