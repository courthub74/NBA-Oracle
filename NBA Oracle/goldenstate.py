import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# GOLDEN STATE WARRIORS

# WARRIORS General Info 134865
warriorsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Golden%20State%20Warriors")

# WARRIORS Last Game 134865
warriorsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134865")

# WARRIORS Next Game 134865
warriorsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134865")

# General Info Parsed
dataGS = warriorsRE.text
parseGS = json.loads(dataGS)
# For the Test
# print(warriorsRE.status_code)

# Last Game Parsed
LGdataGS = warriorsLG.text
LGparseGS = json.loads(LGdataGS)

# Next Game Parsed
NGdataGS = warriorsNG.text
NGparseGS = json.loads(NGdataGS)

# info Layout for the Drop Down Menu to Gather from WARRIORS 134865
warriorsTeam = parseGS["teams"][0]["strTeam"]
yearFormedGS = parseGS["teams"][0]["intFormedYear"]
teamStadiumGS = parseGS["teams"][0]["strStadium"]
teamInfoGS = parseGS["teams"][0]["strDescriptionEN"]
lastGameDateGS = LGparseGS["results"][0]["dateEventLocal"]
homeTeamGS = LGparseGS["results"][0]["strHomeTeam"]
awayTeamGS = LGparseGS["results"][0]["strAwayTeam"]
homeScoreGS = LGparseGS["results"][0]["intHomeScore"]
awayScoreGS = LGparseGS["results"][0]["intAwayScore"]

# Last Game Info Printout WARRIORS
warriorsHome = "Home: " + str(homeTeamGS) + " " + str(homeScoreGS)
warriorsAway = "Away: " + str(awayTeamGS) + " " + str(awayScoreGS)

warriorsGame = lastGameDateGS + """
""" + warriorsHome + """
""" + warriorsAway + ""

# DETERMINING the WIN or LOSS
teamHome = homeTeamGS
teamAway = awayTeamGS 

scoreHome = int(homeScoreGS) 
scoreAway = int(awayScoreGS)

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	if teamHome == "Golden State Warriors" and scoreHome > scoreAway:
		return "Warriors Win"		
	elif teamAway == "Golden State Warriors" and scoreAway > scoreHome:
		return "Warriors Win"
	else:
		return "Warriors Lose"

win()

######################################################################
# NEXT GAME

# Next Game Info Variables WARRIORS 134865
nextOppGS = NGparseGS["events"][0]["strEventAlternate"]
nextHomeGS = NGparseGS["events"][0]["strHomeTeam"]
nextAwayGS = NGparseGS["events"][0]["strAwayTeam"]
nextOppDateGS = NGparseGS["events"][0]["dateEventLocal"]

# DETERMINING NEXT OPPONENT

def next():
	if nextHomeGS == "Golden State Warriors":
		return str(nextAwayGS)
	elif nextAwayGS == "Golden State Warriors":
		return "@" + str(nextHomeGS)

next()


# DETERMINING WHERE NEXT OPPONENT

def where():
	if nextHomeGS == "Golden State Warriors":
		return "@Home" + " --- " + teamStadiumGS
	else:
		return "Away"

where()
