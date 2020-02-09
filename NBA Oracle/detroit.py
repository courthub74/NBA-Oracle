import requests
import json

# TEAM DATA API SCRAPING
#################################################################################
# DETROIT PISTONS

# PISTONS General Info 134872
pistonsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Detroit%20Pistons")
# PISTONS Last Game 134872
pistonsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134872")
# PISTONS Next Game 134872
pistonsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134872")

# General Info Parsed
dataDET = pistonsRE.text
parseDET = json.loads(dataDET)
# For the Test
# print(pistonsRE.status_code)
# print(json.dumps(parseDET, indent=4))

# Last Game Parsed
LGdataDET = pistonsLG.text
LGparseDET = json.loads(LGdataDET)

# Next Game Parsed
NGdataDET = pistonsNG.text
NGparseDET = json.loads(NGdataDET)

# info Layout for the Drop Down Menu to Gather from PISTONS 134872
pistonsTeam = parseDET["teams"][0]["strTeam"]
yearFormedDET = parseDET["teams"][0]["intFormedYear"]
teamStadiumDET = parseDET["teams"][0]["strStadium"]
teamInfoDET = parseDET["teams"][0]["strDescriptionEN"]
lastGameDateDET = LGparseDET["results"][0]["dateEventLocal"]
homeTeamDET = LGparseDET["results"][0]["strHomeTeam"]
awayTeamDET = LGparseDET["results"][0]["strAwayTeam"]
homeScoreDET = LGparseDET["results"][0]["intHomeScore"]
awayScoreDET = LGparseDET["results"][0]["intAwayScore"]

# Last Game Info Printout PISTONS
pistonsHome = "Home: " + str(homeTeamDET) + " " + str(homeScoreDET)
pistonsAway = "Away: " + str(awayTeamDET) + " " + str(awayScoreDET)

pistonsGame = lastGameDateDET + """
""" + pistonsHome + """
""" + pistonsAway + ""