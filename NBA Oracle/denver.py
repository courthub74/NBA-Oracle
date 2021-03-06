import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# DENVER NUGGETS


# NUGGETS Info Parsed 134885
nuggetsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Denver%20Nuggets")
# NUGGETS Last Game 134885
nuggetsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134885")
# NUGGETS Next Game 134885
nuggetsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134885")

# General Info Parsed
dataDEN = nuggetsRE.text
parseDEN = json.loads(dataDEN)

# Last Game Parsed
LGdataDEN = nuggetsLG.text
LGparseDEN = json.loads(LGdataDEN)

# Next Game Parsed
NGdataDEN = nuggetsNG.text
NGparseDEN = json.loads(NGdataDEN)

# info Layout for the Drop Down Menu to Gather from NUGGETS 134885
nuggetsTeam = parseDEN["teams"][0]["strTeam"]
yearFormedDEN = parseDEN["teams"][0]["intFormedYear"]
teamStadiumDEN = parseDEN["teams"][0]["strStadium"]
teamInfoDEN = parseDEN["teams"][0]["strDescriptionEN"]
lastGameDateDEN = LGparseDEN["results"][0]["dateEventLocal"]
homeTeamDEN = LGparseDEN["results"][0]["strHomeTeam"]
awayTeamDEN = LGparseDEN["results"][0]["strAwayTeam"]
homeScoreDEN = LGparseDEN["results"][0]["intHomeScore"]
awayScoreDEN = LGparseDEN["results"][0]["intAwayScore"]

# Last Game Info Printout PISTONS
nuggetsHome = "Home: " + str(homeTeamDEN) + " " + str(homeScoreDEN)
nuggetsAway = "Away: " + str(awayTeamDEN) + " " + str(awayScoreDEN)

nuggetsGame = lastGameDateDEN + """
""" + nuggetsHome + """
""" + nuggetsAway + ""


# DETERMINING the WIN or LOSS
teamHome = homeTeamDEN
teamAway = awayTeamDEN

scoreHome = int(homeScoreDEN)
scoreAway = int(awayScoreDEN)

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "Denver Nuggets" and scoreHome > scoreAway:
		return "Nuggets Win"
	elif teamAway == "Denver Nuggets" and scoreAway > scoreHome:
		return "Nuggets Win"
	else:
		return "Nuggets Lose"

win()


######################################################################
# NEXT GAME

# Next Game Info Variables NUGGETS 134885
try:
	nextOppDEN = NGparseDEN["events"][0]["strEventAlternate"]
	nextHomeDEN = NGparseDEN["events"][0]["strHomeTeam"]
	nextAwayDEN = NGparseDEN["events"][0]["strAwayTeam"]
	nextOppDateDEN = NGparseDEN["events"][0]["dateEventLocal"]
except:
	nextOppDEN = 'null'
	nextHomeDEN = 'null'
	nextAwayDEN = 'null'
	nextOppDateDEN = "TBD"

#Season Suspension Variables
nextGameOpp = "No Games at the Moment"
nextGameLoc = "In the Bubble"

# DETERMINING NEXT OPPONENT

def next():
	if nextHomeDEN == "Denver Nuggets":
		return str(nextAwayDEN)
	elif nextAwayDEN == "Denver Nuggets":
		return "@" + str(nextHomeDEN)

next()


# DETERMINING WHERE NEXT OPPONENT

def where():
	if nextHomeDEN == "Denver Nuggets":
		return "@Home" + " --- " + teamStadiumDEN
	elif nextAwayDEN == "Denver Nuggets":
		return "Away"

where()
