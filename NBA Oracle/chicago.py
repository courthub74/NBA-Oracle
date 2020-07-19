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

# Last Game Info Variables BULLS 134870
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

scoreHome = int(homeScoreCHI)
scoreAway = int(awayScoreCHI)


def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "Chicago Bulls" and scoreHome > scoreAway:
		return "Bulls Win"
		
	elif teamAway == "Chicago Bulls" and scoreAway > scoreHome:
		return "Bulls Win"
	else:
		return "Bulls Lose"

win()

######################################################################
# NEXT GAME

# Next Game Info Variables BULLS 134870
try:
	nextOppCHI = NGparseCHI["events"][0]["strEventAlternate"]
	nextHomeCHI = NGparseCHI["events"][0]["strHomeTeam"]
	nextAwayCHI = NGparseCHI["events"][0]["strAwayTeam"]
	nextOppDateCHI = NGparseCHI["events"][0]["dateEventLocal"]
except:
	nextOppCHI = 'null'
	nextHomeCHI = 'null'
	nextAwayCHI = 'null'
	nextOppDateCHI = "TBD"

#Season Suspension Variables
nextGameOpp = "No Games at the Moment"
nextGameLoc = "In the Bubble"
	
# DETERMINING NEXT OPPONENT

def next():
	if nextHomeCHI == "Chicago Bulls":
		return str(nextAwayCHI)
	elif nextAwayCHI == "Chicago Bulls":
		return "@" + str(nextHomeCHI)

next()


# DETERMINING WHERE NEXT OPPONENT

def where():
	if nextHomeCHI == "Chicago Bulls":
		return "@Home" + " --- " + teamStadiumCHI
	elif nextAwayCHI == "Chicago Bulls":
		return "Away"

where()
