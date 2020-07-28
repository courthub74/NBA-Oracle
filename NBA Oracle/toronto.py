import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# TORONTO RAPTORS

# RAPTORS General Info 134864
torontoRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Toronto_Raptors")
# RAPTORS Last Game 134864
torontoLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134864")
# RAPTORS Next Game 134864
torontoNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134864")

# RAPTORS General Info Parse 134864
dataTOR = torontoRE.text
parseTOR = json.loads(dataTOR)

# RAPTORS Last Game Parse 134864
LGdataTOR = torontoLG.text
LGparseTOR = json.loads(LGdataTOR)

# RAPTORS Next Game Parse 134864
NGdataTOR  = torontoNG.text
NGparseTOR = json.loads(NGdataTOR)


######################################################################
# LAST GAME

# Last Game Info Variables RAPTORS 134864
raptorsTeam = parseTOR["teams"][0]["strTeam"]
yearFormedTOR = parseTOR["teams"][0]["intFormedYear"]
teamStadiumTOR = parseTOR["teams"][0]["strStadium"]
teamInfoTOR = parseTOR["teams"][0]["strDescriptionEN"]
lastGameDateTOR = LGparseTOR["results"][0]["dateEventLocal"]
homeTeamTOR = LGparseTOR["results"][0]["strHomeTeam"]
awayTeamTOR = LGparseTOR["results"][0]["strAwayTeam"]
homeScoreTOR = LGparseTOR["results"][0]["intHomeScore"]
awayScoreTOR = LGparseTOR["results"][0]["intAwayScore"]

# Last Game Info Printout
raptorsHome = "Home: " + str(homeTeamTOR) + " " + str(homeScoreTOR)
raptorsAway = "Away: " + str(awayTeamTOR) + " " + str(awayScoreTOR)

raptorsGame = lastGameDateTOR + """
""" + raptorsHome + """
""" + raptorsAway + ""

# DETERMINING the WIN or LOSS
teamHome = homeTeamTOR
teamAway = awayTeamTOR

scoreHome = int(homeScoreTOR)
scoreAway = int(awayScoreTOR)

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "Toronto Raptors" and scoreHome > scoreAway:
		return "Raptors Win"
	elif teamAway == "Toronto Raptors" and scoreAway > scoreHome:
		return "Raptors Win"
	else:
		return "Raptors Lose"

win()


######################################################################
#NEXT GAME

#Next Game Info Variables RAPTORS 134864
try:
	nextOppTOR = NGparseTOR["events"][0]["strEventAlternate"]
	nextHomeTOR = NGparseTOR["events"][0]["strHomeTeam"]
	nextAwayTOR = NGparseTOR["events"][0]["strAwayTeam"]
	nextOppDateTOR = NGparseTOR["events"][0]["dateEventLocal"]
except:
	nextOppTOR = 'null'
	nextHomeTOR = 'null'
	nextAwayTOR = 'null'
	nextOppDateTOR = 'TBD'

#Season Suspension Variables
nextGameOpp = "No Games at the Moment"
nextGameLoc = "In the Bubble"


#DETERMINING NEXT OPPONENT

def next():
	if nextHomeTOR == "Toronto Raptors":
		return str(nextAwayTOR)
	elif nextAwayTOR == "Toronto Raptors":
		return "@" + str(nextHomeTOR)

next()


#DETERMINING WHERE NEXT OPPONENT

def where():
	if nextHomeTOR == "Toronto Raptors":
		return "@Home" + " --- " + teamStadiumTOR
	elif nextAwayTOR == "Toronto Raptors":
		return "Away"

where()

