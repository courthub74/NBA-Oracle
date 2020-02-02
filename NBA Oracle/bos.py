import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# BOSTON CELTICS

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

# Info Layout for Drop Down BOSTON 134860
celticsTeam = parseBOS["teams"][0]["strTeam"]
yearFormedBOS = parseBOS["teams"][0]["intFormedYear"]
teamStadiumBOS = parseBOS["teams"][0]["strStadium"]
teamInfoBOS = parseBOS["teams"][0]["strDescriptionEN"]
lastGameDateBOS = LGparseBOS["results"][0]["dateEventLocal"]
homeTeamBOS = LGparseBOS["results"][0]["strHomeTeam"]
awayTeamBOS = LGparseBOS["results"][0]["strAwayTeam"]
homeScoreBOS = LGparseBOS["results"][0]["intHomeScore"]
awayScoreBOS = LGparseBOS["results"][0]["intAwayScore"]

# Last Game Info Printout CELTICS
celticsHome = "Home: " + str(homeTeamBOS) + " " + str(homeScoreBOS)
celticsAway = "Away: " + str(awayTeamBOS) + " " + str(awayScoreBOS)

celticsGame = lastGameDateBOS + """
""" + celticsHome + """
""" + celticsAway + ""