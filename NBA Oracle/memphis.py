import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# MEMPHIS GRIZZLIES

# GRIZZLIES General Info 134877
grizzRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Memphis%20Grizzlies")
# Last Game info for GRIZZLIES 134877
grizzLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134877")
# Next Game info for GRIZZLIES 134877
grizzNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134877")

# GRIZZ General Info Parsed 134877
dataMEM = grizzRE.text
parseMEM = json.loads(dataMEM)
# GRIZZ Last Game Parsed
LGdataMEM = grizzLG.text
LGparseMEM = json.loads(LGdataMEM)
# GRIZZ Next Game Parsed
NGdataMEM = grizzNG.text
NGparseMEM = json.loads(NGdataMEM)

# info Layout for the Drop Down Menu to Gather from GRIZZ 134877
grizzTeam = parseMEM["teams"][0]["strTeam"]
yearFormedMEM = parseMEM["teams"][0]["intFormedYear"]
teamStadiumMEM = parseMEM["teams"][0]["strStadium"]
teamInfoMEM = parseMEM["teams"][0]["strDescriptionEN"]
lastGameDateMEM = LGparseMEM["results"][0]["dateEventLocal"]
homeTeamMEM = LGparseMEM["results"][0]["strHomeTeam"]
awayTeamMEM = LGparseMEM["results"][0]["strAwayTeam"]
homeScoreMEM = LGparseMEM["results"][0]["intHomeScore"]
awayScoreMEM = LGparseMEM["results"][0]["intAwayScore"]

# Last Game Info Printout GRIZZLIES
grizzHome = "Home: " + str(homeTeamMEM) + " " + str(homeScoreMEM)
grizzAway = "Away: " + str(awayTeamMEM) + " " + str(awayScoreMEM)

grizzGame = lastGameDateMEM + """
""" + grizzHome + """
""" + grizzAway + ""


# DETERMINING the WIN or LOSS
teamHome = homeTeamMEM
teamAway = awayTeamMEM

scoreHome = int(homeScoreMEM)
scoreAway = int(awayScoreMEM)

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "Memphis Grizzlies" and scoreHome > scoreAway:
		return "Grizzlies Win"
	elif teamAway == "Memphis Grizzlies" and scoreAway > scoreHome:
		return "Grizzlies Win"
	else:
		return "Grizzlies Lose"

win()
