import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# CLEVELAND CAVALIERS

# CAVALIERS General Info 134871
cavsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Cleveland%20Cavaliers")
# CAVALIERS Last Game 134871
cavsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134871")
# CAVALIERS Next Game 134871
cavsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134871")

# General Info Parsed
dataCLE = cavsRE.text
parseCLE = json.loads(dataCLE)
# print(cavsRE.status_code)

# Last Game Parsed
LGdataCLE = cavsLG.text
LGparseCLE = json.loads(LGdataCLE)

# Next Game Parsed
NGdataCLE = cavsNG.text
NGparseCLE = json.loads(NGdataCLE)

# info Layout for the Drop Down Menu to Gather from CAVALIERS 134871
cavsTeam = parseCLE["teams"][0]["strTeam"]
yearFormedCLE = parseCLE["teams"][0]["intFormedYear"]
teamStadiumCLE = parseCLE["teams"][0]["strStadium"]
teamInfoCLE = parseCLE["teams"][0]["strDescriptionEN"]
lastGameDateCLE = LGparseCLE["results"][0]["dateEventLocal"]
homeTeamCLE = LGparseCLE["results"][0]["strHomeTeam"]
awayTeamCLE = LGparseCLE["results"][0]["strAwayTeam"]
homeScoreCLE = LGparseCLE["results"][0]["intHomeScore"]
awayScoreCLE = LGparseCLE["results"][0]["intAwayScore"]

# Last Game Info Printout CAVALIERS
cavsHome = "Home: " + str(homeTeamCLE) + " " + str(homeScoreCLE)
cavsAway = "Away: " + str(awayTeamCLE) + " " + str(awayScoreCLE)

cavsGame = lastGameDateCLE + """
""" + cavsHome + """
""" + cavsAway + ""

# DETERMINING the WIN or LOSS
teamHome = homeTeamCLE
teamAway = awayTeamCLE 

scoreHome = int(homeScoreCLE)
scoreAway = int(awayScoreCLE)

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "Cleveland Cavaliers" and scoreHome > scoreAway:
		return "Cavs Win"
	elif teamAway == "Cleveland Cavaliers" and scoreAway > scoreHome:
		return "Cavs Win"
	else:
		return "Cavs Lose"

win()


######################################################################
# NEXT GAME

# Next Game Info Variables CAVALIERS 134871
nextOppCLE = NGparseCLE["events"][0]["strEventAlternate"]
nextHomeCLE = NGparseCLE["events"][0]["strHomeTeam"]
nextAwayCLE = NGparseCLE["events"][0]["strAwayTeam"]
nextOppDateCLE = NGparseCLE["events"][0]["dateEventLocal"]

# DETERMINING NEXT OPPONENT

def next():
	if nextHomeCLE == "Cleveland Cavaliers":
		return str(nextAwayCLE)
	elif nextAwayCLE == "Cleveland Cavaliers":
		return "@" + str(nextHomeCLE)

next()


# DETERMINING WHERE NEXT OPPONENT

def where():
	if nextHomeCLE == "Cleveland Cavaliers":
		return "@Home" + " --- " + teamStadiumCLE
	else:
		return "Away"

where()
