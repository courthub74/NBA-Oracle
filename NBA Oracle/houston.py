import requests
import json

# TEAM DATA API SCRAPING
########################################################################################
# HOUSTON CALLS (ROCKETS)

# ROCKETS Info 134876
rocketsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Houston%20Rockets")
# ROCKETS Last Game Info 134876
rocketsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134876")
# ROCKETS Next Game Info 134876
rocketsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134876")

# ROCKETS Info Parsed 134876
dataHOU = rocketsRE.text
parseHOU = json.loads(dataHOU)
# ROCKETS Last Game Parsed 134876
LGdataHOU = rocketsLG.text
LGparseHOU = json.loads(LGdataHOU)
# ROCKETS Next Game Parsed 134876
NGdataHOU = rocketsNG.text
NGparseHOU = json.loads(NGdataHOU)

# info Layout for the Drop Down Menu to Gather from ROCKETS 134876
rocketsTeam = parseHOU["teams"][0]["strTeam"]
yearFormedHOU = parseHOU["teams"][0]["intFormedYear"]
teamStadiumHOU = parseHOU["teams"][0]["strStadium"]
teamInfoHOU = parseHOU["teams"][0]["strDescriptionEN"]
lastGameDateHOU = LGparseHOU["results"][0]["dateEventLocal"]
homeTeamHOU = LGparseHOU["results"][0]["strHomeTeam"]
awayTeamHOU = LGparseHOU["results"][0]["strAwayTeam"]
homeScoreHOU = LGparseHOU["results"][0]["intHomeScore"]
awayScoreHOU = LGparseHOU["results"][0]["intAwayScore"]

# Last Game Info Printout LAKERS
rocketsHome = "Home: " + str(homeTeamHOU) + " " + str(homeScoreHOU)
rocketsAway = "Away: " + str(awayTeamHOU) + " " + str(awayScoreHOU)

rocketsGame = lastGameDateHOU + """
""" + rocketsHome + """
""" + rocketsAway + ""


# DETERMINING the WIN or LOSS
teamHome = homeTeamHOU
teamAway = awayTeamHOU

scoreHome = int(homeScoreHOU)
scoreAway = int(awayScoreHOU)


def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "Houston Rockets" and scoreHome > scoreAway:
		return "Rockets Win"
	elif teamAway == "Houston Rockets" and scoreAway > scoreHome:
		return "Rockets Win"
	else:
		return "Rockets Lose"

win()