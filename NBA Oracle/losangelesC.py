import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# LOS ANGELES CLIPPERS
# CLIPPERS General Info 134866
clippersRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Los%20Angeles%20Clippers")
# CLIPPERS last game info 134866
clippersLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134866")
# CLIPPERS next game info 134866
clippersNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134866")

# CLIPPERS General Info Parsed 134866
dataLAC = clippersRE.text
parseLAC = json.loads(dataLAC)
# Last Game Parsed
LGdataLAC = clippersLG.text
LGparseLAC = json.loads(LGdataLAC)
# Next Game Parsed
NGdataLAC = clippersNG.text
NGparseLAC = json.loads(NGdataLAC)

# info Layout for the Drop Down Menu to Gather from CLIPPERS 134867
clippersTeam = parseLAC["teams"][0]["strTeam"]
yearFormedLAC = parseLAC["teams"][0]["intFormedYear"]
teamStadiumLAC = parseLAC["teams"][0]["strStadium"]
teamInfoLAC = parseLAC["teams"][0]["strDescriptionEN"]
lastGameDateLAC = LGparseLAC["results"][0]["dateEventLocal"]
homeTeamLAC = LGparseLAC["results"][0]["strHomeTeam"]
awayTeamLAC = LGparseLAC["results"][0]["strAwayTeam"]
homeScoreLAC = LGparseLAC["results"][0]["intHomeScore"]
awayScoreLAC = LGparseLAC["results"][0]["intAwayScore"]

# Last Game Info Printout CLIPPERS
clippersHome = "Home: " + str(homeTeamLAC) + " " + str(homeScoreLAC)
clippersAway = "Away: " + str(awayTeamLAC) + " " + str(awayScoreLAC)

clippersGame = lastGameDateLAC + """
""" + clippersHome + """
""" + clippersAway + ""


# DETERMINING the WIN or LOSS
teamHome = homeTeamLAC
teamAway = awayTeamLAC 

scoreHome = int(homeScoreLAC)
scoreAway = int(awayScoreLAC)

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "Los Angeles Clippers" and scoreHome > scoreAway:
		return "Clippers Win"
	elif teamAway == "Los Angeles Clippers" and scoreAway > scoreHome:
		return "Clippers Win"
	else:
		return "Clippers Lose"

win()