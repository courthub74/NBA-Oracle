import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# MIAMI HEAT

# HEAT General Info 134882
heatRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Miami%20Heat")
# Last Game Info HEAT 134882
heatLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134882")
# Next Game Info HEAT 134882
heatNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134882")

# HEAT General Info Parsed 134882
dataMIA = heatRE.text
parseMIA = json.loads(dataMIA)
# Last Game Parsed
LGdataMIA = heatLG.text
LGparseMIA = json.loads(LGdataMIA)
# Next Game Parsed
NGdataMIA = heatNG.text
NGparseMIA = json.loads(NGdataMIA)

# info Layout for the Drop Down Menu to Gather from HEAT 134882
heatTeam = parseMIA["teams"][0]["strTeam"]
yearFormedMIA = parseMIA["teams"][0]["intFormedYear"]
teamStadiumMIA = parseMIA["teams"][0]["strStadium"]
teamInfoMIA = parseMIA["teams"][0]["strDescriptionEN"]
lastGameDateMIA = LGparseMIA["results"][0]["dateEventLocal"]
homeTeamMIA = LGparseMIA["results"][0]["strHomeTeam"]
awayTeamMIA = LGparseMIA["results"][0]["strAwayTeam"]
homeScoreMIA = LGparseMIA["results"][0]["intHomeScore"]
awayScoreMIA = LGparseMIA["results"][0]["intAwayScore"]

# Last Game Info Printout BUCKS
heatHome = "Home: " + str(homeTeamMIA) + " " + str(homeScoreMIA)
heatAway = "Away: " + str(awayTeamMIA) + " " + str(awayScoreMIA)

heatGame = lastGameDateMIA + """
""" + heatHome + """
""" + heatAway + ""


# DETERMINING the WIN or LOSS
teamHome = homeTeamMIA
teamAway = awayTeamMIA 

scoreHome = int(homeScoreMIA)
scoreAway = int(awayScoreMIA)

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "Miami Heat" and scoreHome > scoreAway:
		return "Heat Win"
	elif teamAway == "Miami Heat" and scoreAway > scoreHome:
		return "Heat Win"
	else:
		return "Heat Lose"

win()
