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

######################################################################
# NEXT GAME

# Next Game Info Variables PACERS 134873
try:
	nextOppIND = NGparseIND["events"][0]["strEventAlternate"]
	nextHomeIND = NGparseIND["events"][0]["strHomeTeam"]
	nextAwayIND = NGparseIND["events"][0]["strAwayTeam"]
	nextOppDateIND = NGparseIND["events"][0]["dateEventLocal"]
except:
	nextOppIND = 'null'
	nextHomeIND = 'null'
	nextAwayIND = 'null'
	nextOppDateIND = "TBD"

#Season Suspension Variables
nextGameOpp = "No Games at the Moment"
nextGameLoc = "In the Bubble"

# DETERMINING NEXT OPPONENT

def next():
	if nextHomeIND == "Indiana Pacers":
		return str(nextAwayIND)  
	elif nextAwayIND == "Indiana Pacers":
		return "@" + str(nextHomeIND) 

next()

# DETERMINING WHERE NEXT OPPONENT

def where():
	if nextHomeIND == "Indiana Pacers":
		return "@Home" + " --- " + teamStadiumIND
	elif nextAwayIND == "Indiana Pacers":
		return "Away"

where()

# If you need to print the API data for review
# print(json.dumps(NGparseIND, indent=4))