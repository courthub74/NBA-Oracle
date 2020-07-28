import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# SAN ANTONIO SPURS

# SPURS General Info 134879
sanantonioRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=San_Antonio_Spurs")
# SPURS Last Game 134879
sanantonioLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134879")
# SPURS Next Game 134879
sanantonioNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134879")

# SPURS General Info Parse 134879
dataSAS = sanantonioRE.text
parseSAS = json.loads(dataSAS)

# SPURS Last Game Parse 134879
LGdataSAS = sanantonioLG.text
LGparseSAS = json.loads(LGdataSAS)

# SPURS Next Game Parse 134879
NGdataSAS  = sanantonioNG.text
NGparseSAS = json.loads(NGdataSAS)


######################################################################
# LAST GAME

# Last Game Info Variables SACRAMENTO 134879
spursTeam = parseSAS["teams"][0]["strTeam"]
yearFormedSAS = parseSAS["teams"][0]["intFormedYear"]
teamStadiumSAS = parseSAS["teams"][0]["strStadium"]
teamInfoSAS = parseSAS["teams"][0]["strDescriptionEN"]
lastGameDateSAS = LGparseSAS["results"][0]["dateEventLocal"]
homeTeamSAS = LGparseSAS["results"][0]["strHomeTeam"]
awayTeamSAS = LGparseSAS["results"][0]["strAwayTeam"]
homeScoreSAS = LGparseSAS["results"][0]["intHomeScore"]
awayScoreSAS = LGparseSAS["results"][0]["intAwayScore"]

# Last Game Info Printout
spursHome = "Home: " + str(homeTeamSAS) + " " + str(homeScoreSAS)
spursAway = "Away: " + str(awayTeamSAS) + " " + str(awayScoreSAS)

spursGame = lastGameDateSAS + """
""" + spursHome + """
""" + spursAway + ""

# DETERMINING the WIN or LOSS
teamHome = homeTeamSAS
teamAway = awayTeamSAS

scoreHome = int(homeScoreSAS)
scoreAway = int(awayScoreSAS)

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "San Antonio Spurs" and scoreHome > scoreAway:
		return "Spurs Win"
	elif teamAway == "San Antonio Spurs" and scoreAway > scoreHome:
		return "Spurs Win"
	else:
		return "Spurs Lose"

win()


######################################################################
#NEXT GAME

#Next Game Info Variables SPURS 134879
try:
	nextOppSAS = NGparseSAS["events"][0]["strEventAlternate"]
	nextHomeSAS = NGparseSAS["events"][0]["strHomeTeam"]
	nextAwaySAS = NGparseSAS["events"][0]["strAwayTeam"]
	nextOppDateSAS = NGparseSAS["events"][0]["dateEventLocal"]
except:
	nextOppSAS = 'null'
	nextHomeSAS = 'null'
	nextAwaySAS = 'null'
	nextOppDateSAS = 'TBD'

#Season Suspension Variables
nextGameOpp = "No Games at the Moment"
nextGameLoc = "In the Bubble"


#DETERMINING NEXT OPPONENT

def next():
	if nextHomeSAS == "San Antonio Spurs":
		return str(nextAwaySAS)
	elif nextAwaySAS == "San Antonio Spurs":
		return "@" + str(nextHomeSAS)

next()


#DETERMINING WHERE NEXT OPPONENT

def where():
	if nextHomeSAS == "San Antonio Spurs":
		return "@Home" + " --- " + teamStadiumSAS
	elif nextAwaySAS == "San Antonio Spurs":
		return "Away"

where()

