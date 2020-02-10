import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# CHICAGO BULLS

# BULLS General Info 134870
bullsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Chicago%20Bulls")
# BULLS Last Game Info 134870
bullsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134870")
# BULLS Next Game Info 134870
bullsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134870")

# General Info Parsed
dataCHI = bullsRE.text
parseCHI = json.loads(dataCHI)

# Last Game Parsed
LGdataCHI = bullsLG.text
LGparseCHI = json.loads(LGdataCHI)

# Next Game Parsed
NGdataCHI = bullsNG.text
NGparseCHI = json.loads(NGdataCHI)

# info Layout for the Drop Down Menu to Gather from BULLS 134870
bullsTeam = parseCHI["teams"][0]["strTeam"]
yearFormedCHI = parseCHI["teams"][0]["intFormedYear"]
teamStadiumCHI = parseCHI["teams"][0]["strStadium"]
teamInfoCHI = parseCHI["teams"][0]["strDescriptionEN"]
lastGameDateCHI = LGparseCHI["results"][0]["dateEventLocal"]
homeTeamCHI = LGparseCHI["results"][0]["strHomeTeam"]
awayTeamCHI = LGparseCHI["results"][0]["strAwayTeam"]
homeScoreCHI = LGparseCHI["results"][0]["intHomeScore"]
awayScoreCHI = LGparseCHI["results"][0]["intAwayScore"]

# Last Game Info Printout BULLS
bullsHome = "Home: " + str(homeTeamCHI) + " " + str(homeScoreCHI)
bullsAway = "Away: " + str(awayTeamCHI) + " " + str(awayScoreCHI)

bullsGame = lastGameDateCHI + """
""" + bullsHome + """
""" + bullsAway + ""

# DETERMINING the WIN or LOSS
teamHome = homeTeamCHI
teamAway = awayTeamCHI

scoreHome = homeScoreCHI
scoreAway = awayScoreCHI


def win():
	if teamHome == "Chicago Bulls" and scoreHome > scoreAway:
		return "Bulls Win"
		
	elif teamAway == "Chicago Bulls" and scoreAway > scoreHome:
		return "Bulls Win"
	else:
		return "Bulls Lose"

win()