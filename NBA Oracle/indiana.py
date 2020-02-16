import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# INDIANA PACERS

# PACERS General Info 134873
pacersRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Indiana%20Pacers")
# PACERS Last Game Info
pacersLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134873")
# PACERS Next Game Info
pacersNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134873")

# PACERS General Info Parsed 134873
dataIND = pacersRE.text
parseIND = json.loads(dataIND)
# Last Game Parsed
LGdataIND = pacersLG.text
LGparseIND = json.loads(LGdataIND)
# Next Game Parsed
NGdataIND = pacersNG.text
NGparseIND = json.loads(NGdataIND)

# info Layout for the Drop Down Menu to Gather from PACERS 134873
pacersTeam = parseIND["teams"][0]["strTeam"]
yearFormedIND = parseIND["teams"][0]["intFormedYear"]
teamStadiumIND = parseIND["teams"][0]["strStadium"]
teamInfoIND = parseIND["teams"][0]["strDescriptionEN"]
lastGameDateIND = LGparseIND["results"][0]["dateEventLocal"]
homeTeamIND = LGparseIND["results"][0]["strHomeTeam"]
awayTeamIND = LGparseIND["results"][0]["strAwayTeam"]
homeScoreIND = LGparseIND["results"][0]["intHomeScore"]
awayScoreIND = LGparseIND["results"][0]["intAwayScore"]

# Last Game Info Printout PACERS
pacersHome = "Home: " + str(homeTeamIND) + " " + str(homeScoreIND)
pacersAway = "Away: " + str(awayTeamIND) + " " + str(awayScoreIND)

pacersGame = lastGameDateIND + """
""" + pacersHome + """
""" + pacersAway + ""


# DETERMINING the WIN or LOSS
teamHome = homeTeamIND
teamAway = awayTeamIND 

scoreHome = int(homeScoreIND)
scoreAway = int(awayScoreIND)

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "Indiana Pacers" and scoreHome > scoreAway:
		return "Pacers Win"
	elif teamAway == "Indiana Pacers" and scoreAway > scoreHome:
		return "Pacers Win"
	else:
		return "Pacers Lose"

win()