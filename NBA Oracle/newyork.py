import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# NEW YORK KNICKS

# KNICKS General Info 134862
knicksRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=new_york_knicks")
# KNICKS Last Game 134862
knicksLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134862")
# KNICKS Next Game 134862
knicksNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134862")

# KNICKS General Info Parse
dataNYK = knicksRE.text
parseNYK = json.loads(dataNYK)

# KNICKS Last Game Parse
LGdataNYK = knicksLG.text
LGparseNYK = json.loads(LGdataNYK)

# KNICKS Next Game Parse
NGdataNYK = knicksNG.text
NGparseNYK = json.loads(NGdataNYK)

#Last Game Info Variables Knicks 134862
knicksTeam = parseNYK["teams"][0]["strTeam"]
yearFormedNYK = parseNYK["teams"][0]["intFormedYear"]
teamStadiumNYK = parseNYK["teams"][0]["strStadium"]
teamInfoNYK = parseNYK["teams"][0]["strDescriptionEN"]
lastGameDateNYK = LGparseNYK["results"][0]["dateEventLocal"]
homeTeamNYK = LGparseNYK["results"][0]["strHomeTeam"]
awayTeamNYK = LGparseNYK["results"][0]["strAwayTeam"]
homeScoreNYK = LGparseNYK["results"][0]["intHomeScore"]
awayScoreNYK = LGparseNYK["results"][0]["intAwayScore"]

#Last Game Info Printout KNICKS
knicksHome = "Home: " + str(homeTeamNYK) + " " + str(homeScoreNYK)
knicksAway = "Away: " + str(awayTeamNYK) + " " + str(awayScoreNYK)

knicksGame = lastGameDateNYK + """
""" + knicksHome + """
""" + knicksAway + ""

# DETERMINING the WIN or LOSS
teamHome = homeTeamNYK
teamAway = awayTeamNYK

scoreHome = int(homeScoreNYK)
scoreAway = int(awayScoreNYK)

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "New York Knicks" and scoreHome > scoreAway:
		return "Knicks Win"
	elif teamAway == "New York Knicks" and scoreAway > scoreHome:
		return "Knicks Win"
	else:
		return "Knicks Lose"

win()

###############################################################################
# NEXT GAME

# Next Game Info Variables KNICKS 134862

try:
	nextOppNYK = NGparseNYK["events"][0]["strEventAlternate"]
	nextHomeNYK = NGparseNYK["events"][0]["strHomeTeam"]
	nextAwayNYK = NGparseNYK["events"][0]["strAwayTeam"]
	nextOppDateNYK = NGparseNYK["events"][0]["dateEventLocal"] 
except:
	nextOppNYK = 'null'
	nextHomeNYK = 'null'
	nextAwayNYK = 'null'
	nextOppDateNYK = "TBD" 

#Season Suspension Variables
nextGameOpp = "No Games at the Moment"
nextGameLoc = "In the Bubble"


# DETERMINING NEXT OPPONENT

def next():
	if nextHomeNYK == "New York Knicks":
		return str(nextAwayNYK)
	elif nextAwayNYK == "New York Knicks":
		return "@" + str(nextHomeNYK)

next()


# DETERMINING WHERE NEXT OPPONENT

def where():
	if nextHomeNYK == "New York Knicks":
		return "@Home"  + " --- " + teamStadiumNYK
	elif nextAwayNYK == "New York Knicks":
		return "Away"

where()

# In Case you need to review API data
# print(json.dumps(x, indent=4))