import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# PHOENIX SUNS

# SUNS General Info 134868
sunsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Phoenix_Suns")
# SUNS Last Game 134868
sunsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134868")
# SUNS Next Game 134868
sunsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134868")

# SUNS General Info Parse 134868
dataPHO = sunsRE.text
parsePHO = json.loads(dataPHO)

# SUNS Last Game Parse 134868
LGdataPHO = sunsLG.text
LGparsePHO = json.loads(LGdataPHO)

# SUNS Next Game Parse 134868
NGdataPHO = sunsNG.text
NGparsePHO = json.loads(NGdataPHO)


######################################################################
# LAST GAME

# Last Game Info Variables MAGIC 134883
sunsTeam = parsePHO["teams"][0]["strTeam"]
yearFormedPHO = parsePHO["teams"][0]["intFormedYear"]
teamStadiumPHO = parsePHO["teams"][0]["strStadium"]
teamInfoPHO = parsePHO["teams"][0]["strDescriptionEN"]
lastGameDatePHO = LGparsePHO["results"][0]["dateEventLocal"]
homeTeamPHO = LGparsePHO["results"][0]["strHomeTeam"]
awayTeamPHO = LGparsePHO["results"][0]["strAwayTeam"]
homeScorePHO = LGparsePHO["results"][0]["intHomeScore"]
awayScorePHO = LGparsePHO["results"][0]["intAwayScore"]

# Last Game Info Printout
sunsHome = "Home: " + str(homeTeamPHO) + " " + str(homeScorePHO)
sunsAway = "Away: " + str(awayTeamPHO) + " " + str(awayScorePHO)

sunsGame = lastGameDatePHO + """
""" + sunsHome + """
""" + sunsAway + ""

# DETERMINING the WIN or LOSS
teamHome = homeTeamPHO
teamAway = awayTeamPHO

scoreHome = int(homeScorePHO)
scoreAway = int(awayScorePHO)

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "Phoenix Suns" and scoreHome > scoreAway:
		return "Suns Win"
	elif teamAway == "Phoenix Suns" and scoreAway > scoreHome:
		return "Suns Win"
	else:
		return "Suns Lose"

win()


######################################################################
#NEXT GAME

#Next Game Info Variables SUNS 134868
try:
	nextOppPHO = NGparsePHO["events"][0]["strEventAlternate"]
	nextHomePHO = NGparsePHO["events"][0]["strHomeTeam"]
	nextAwayPHO = NGparsePHO["events"][0]["strAwayTeam"]
	nextOppDatePHO = NGparsePHO["events"][0]["dateEventLocal"]
except:
	nextOppPHO = 'null'
	nextHomePHO = 'null'
	nextAwayPHO = 'null'
	nextOppDatePHO = 'TBD'

#Season Suspension Variables
nextGameOpp = "No Games at the Moment"
nextGameLoc = "In the Bubble"


#DETERMINING NEXT OPPONENT

def next():
	if nextHomePHO == "Phoenix Suns":
		return str(nextAwayPHO)
	elif nextAwayPHO == "Phoenix Suns":
		return "@" + str(nextHomePHO)

next()


#DETERMINING WHERE NEXT OPPONENT

def where():
	if nextHomePHO == "Phoenix Suns":
		return "@Home" + " --- " + teamStadiumPHO
	elif nextAwayPHO == "Phoenix Suns":
		return "Away"

where()
