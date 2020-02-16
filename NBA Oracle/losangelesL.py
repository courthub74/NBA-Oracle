import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# LOS ANGELES LAKERS


# KCal the LAKERS are playing 134867
lakersRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Los%20Angeles%20Lakers")
# LAKERS last game info
lakersLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134867")
# LAKERS next game info
lakersNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134867")

# LAKERS General Info Parsed 134867
dataLAL = lakersRE.text
parseLAL = json.loads(dataLAL)
# Last Game Parsed
LGdataLAL = lakersLG.text
LGparseLAL = json.loads(LGdataLAL)
# Next Game Parsed
NGdataLAL = lakersNG.text
NGparseLAL = json.loads(NGdataLAL)

# info Layout for the Drop Down Menu to Gather from LAKERS 134867
lakersTeam = parseLAL["teams"][0]["strTeam"]
yearFormedLAL = parseLAL["teams"][0]["intFormedYear"]
teamStadiumLAL = parseLAL["teams"][0]["strStadium"]
teamInfoLAL = parseLAL["teams"][0]["strDescriptionEN"]
lastGameDateLAL = LGparseLAL["results"][0]["dateEventLocal"]
homeTeamLAL = LGparseLAL["results"][0]["strHomeTeam"]
awayTeamLAL = LGparseLAL["results"][0]["strAwayTeam"]
homeScoreLAL = LGparseLAL["results"][0]["intHomeScore"]
awayScoreLAL = LGparseLAL["results"][0]["intAwayScore"]

# Last Game Info Printout LAKERS
lakersHome = "Home: " + str(homeTeamLAL) + " " + str(homeScoreLAL)
lakersAway = "Away: " + str(awayTeamLAL) + " " + str(awayScoreLAL)

lakersGame = lastGameDateLAL + """
""" + lakersHome + """
""" + lakersAway + ""


# DETERMINING the WIN or LOSS
teamHome = homeTeamLAL
teamAway = awayTeamLAL

scoreHome = int(homeScoreLAL)
scoreAway = int(awayScoreLAL)

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "Los Angeles Lakers" and scoreHome > scoreAway:
		return "Lakers Win"
	elif teamAway == "Los Angeles Lakers" and scoreAway > scoreHome:
		return "Lakers Win"
	else:
		return "Lakers Lose"

win()