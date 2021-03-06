import requests
import json

# TEAM DATA API SCRAPING
####################################################
# CHARLOTTE HORNETS

# HORNETS General Info 134881
hornetsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Charlotte%20Hornets")
# HORNETS Last Game Info 134881
hornetsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134881")
# HORNETS Next Game Info 134881
hornetsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134881")

# General Info Parsed
dataCHA = hornetsRE.text
parseCHA = json.loads(dataCHA)

# Last Game Parsed
LGdataCHA = hornetsLG.text
LGparseCHA = json.loads(LGdataCHA)

# Next Game Parsed
NGdataCHA = hornetsNG.text
NGparseCHA = json.loads(NGdataCHA)

# Last Game Info Variables HORNETS 134881
hornetsTeam = parseCHA["teams"][0]["strTeam"]
yearFormedCHA = parseCHA["teams"][0]["intFormedYear"]
teamStadiumCHA = parseCHA["teams"][0]["strStadium"]
teamInfoCHA = parseCHA["teams"][0]["strDescriptionEN"]
lastGameDateCHA = LGparseCHA["results"][0]["dateEventLocal"]
homeTeamCHA = LGparseCHA["results"][0]["strHomeTeam"]
awayTeamCHA = LGparseCHA["results"][0]["strAwayTeam"]
homeScoreCHA = LGparseCHA["results"][0]["intHomeScore"]
awayScoreCHA = LGparseCHA["results"][0]["intAwayScore"]

# Last Game Info Printout HORNETS
hornetsHome = "Home: " + str(homeTeamCHA) + " " + str(homeScoreCHA)
hornetsAway = "Away: " + str(awayTeamCHA) + " " + str(awayScoreCHA)

hornetsGame = lastGameDateCHA + """
""" + hornetsHome + """
""" + hornetsAway + ""

# DETERMINING the WIN or LOSS
teamHome = homeTeamCHA
teamAway = awayTeamCHA

scoreHome = int(homeScoreCHA)
scoreAway = int(awayScoreCHA)

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	if teamHome == "Charlotte Hornets" and scoreHome > scoreAway:
		return "Hornets Win"
	elif teamAway == "Charlotte Hornets" and scoreAway > scoreHome:
		return "Hornets Win"
	else:
		return "Hornets Lose"

win()

######################################################################
# NEXT GAME

# Next Game Info Variables HORNETS 134881
try:
	nextOppCHA = NGparseCHA["events"][0]["strEventAlternate"]
	nextHomeCHA = NGparseCHA["events"][0]["strHomeTeam"]
	nextAwayCHA = NGparseCHA["events"][0]["strAwayTeam"]
	nextOppDateCHA = NGparseCHA["events"][0]["dateEventLocal"]
except:
	nextOppCHA = 'null'
	nextHomeCHA = 'null'
	nextAwayCHA = 'null'
	nextOppDateCHA = "TBD"

#Season Suspension Variables
nextGameOpp = "No Games at the Moment"
nextGameLoc = "In the Bubble"


# DETERMINING NEXT OPPONENT

def next():
	if nextHomeCHA == "Charlotte Hornets":
		return str(nextAwayCHA)
	elif nextAwayCHA == "Charlotte Hornets":
		return "@" + str(nextHomeCHA)

next()


# DETERMINING WHERE NEXT OPPONENT

def where():
	if nextHomeCHA == "Charlotte Hornets":
		return "@Home" + " --- " + teamStadiumCHA
	elif nextAwayCHA == "Charlotte Hornets":
		return "Away"

where()
