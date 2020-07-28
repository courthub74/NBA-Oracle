import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# SACRAMENTO KINGS

# KINGS General Info 134869
sacramentoRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Sacramento_Kings")
# KINGS Last Game 134869
sacramentoLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134869")
# KINGS Next Game 134869
sacramentoNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134869")

# KINGS General Info Parse 134869
dataSAC = sacramentoRE.text
parseSAC = json.loads(dataSAC)

# KINGS Last Game Parse 134869
LGdataSAC = sacramentoLG.text
LGparseSAC = json.loads(LGdataSAC)

# KINGS Next Game Parse 134869
NGdataSAC  = sacramentoNG.text
NGparseSAC = json.loads(NGdataSAC)


######################################################################
# LAST GAME

# Last Game Info Variables KINGS 134869
kingsTeam = parseSAC["teams"][0]["strTeam"]
yearFormedSAC = parseSAC["teams"][0]["intFormedYear"]
teamStadiumSAC = parseSAC["teams"][0]["strStadium"]
teamInfoSAC = parseSAC["teams"][0]["strDescriptionEN"]
lastGameDateSAC = LGparseSAC["results"][0]["dateEventLocal"]
homeTeamSAC = LGparseSAC["results"][0]["strHomeTeam"]
awayTeamSAC = LGparseSAC["results"][0]["strAwayTeam"]
homeScoreSAC = LGparseSAC["results"][0]["intHomeScore"]
awayScoreSAC = LGparseSAC["results"][0]["intAwayScore"]

# Last Game Info Printout
kingsHome = "Home: " + str(homeTeamSAC) + " " + str(homeScoreSAC)
kingsAway = "Away: " + str(awayTeamSAC) + " " + str(awayScoreSAC)

kingsGame = lastGameDateSAC + """
""" + kingsHome + """
""" + kingsAway + ""

# DETERMINING the WIN or LOSS
teamHome = homeTeamSAC
teamAway = awayTeamSAC

scoreHome = int(homeScoreSAC)
scoreAway = int(awayScoreSAC)

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "Sacramento Kings" and scoreHome > scoreAway:
		return "Kings Win"
	elif teamAway == "Sacramento Kings" and scoreAway > scoreHome:
		return "Kings Win"
	else:
		return "Kings Lose"

win()


######################################################################
#NEXT GAME

#Next Game Info Variables KINGS 134869
try:
	nextOppSAC = NGparseSAC["events"][0]["strEventAlternate"]
	nextHomeSAC = NGparseSAC["events"][0]["strHomeTeam"]
	nextAwaySAC = NGparseSAC["events"][0]["strAwayTeam"]
	nextOppDateSAC = NGparseSAC["events"][0]["dateEventLocal"]
except:
	nextOppSAC = 'null'
	nextHomeSAC = 'null'
	nextAwaySAC = 'null'
	nextOppDateSAC = 'TBD'

#Season Suspension Variables
nextGameOpp = "No Games at the Moment"
nextGameLoc = "In the Bubble"


#DETERMINING NEXT OPPONENT

def next():
	if nextHomeSAC == "Sacramento Kings":
		return str(nextAwaySAC)
	elif nextAwaySAC == "Sacramento Kings":
		return "@" + str(nextHomeSAC)

next()


#DETERMINING WHERE NEXT OPPONENT

def where():
	if nextHomeSAC == "Sacramento Kings":
		return "@Home" + " --- " + teamStadiumSAC
	elif nextAwaySAC == "Sacramento Kings":
		return "Away"

where()

