import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# PHILADELPHIA 76ERS

#SIXERS General Info 134863
sixersRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=philadelphia_76ers")
#SIXERS Last Game 134863
sixersLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134863")
#SIXERS Next Game 134863
sixersNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134863")

#SIXERS General Info Parse 134863
dataPHI = sixersRE.text
parsePHI = json.loads(dataPHI)

#SIXERS Last Game Parse 134863
LGdataPHI = sixersLG.text
LGparsePHI = json.loads(LGdataPHI)

#SIXERS Next Game Parse 134863
NGdataPHI = sixersNG.text
NGparsePHI = json.loads(NGdataPHI)


######################################################################
# LAST GAME

# Last Game Info Variables SIXERS 134863
sixersTeam = parsePHI["teams"][0]["strTeam"]
yearFormedPHI = parsePHI["teams"][0]["intFormedYear"]
teamStadiumPHI = parsePHI["teams"][0]["strStadium"]
teamInfoPHI = parsePHI["teams"][0]["strDescriptionEN"]
lastGameDatePHI = LGparsePHI["results"][0]["dateEventLocal"]
homeTeamPHI = LGparsePHI["results"][0]["strHomeTeam"]
awayTeamPHI = LGparsePHI["results"][0]["strAwayTeam"]
homeScorePHI = LGparsePHI["results"][0]["intHomeScore"]
awayScorePHI = LGparsePHI["results"][0]["intAwayScore"]

# Last Game Info Printout
sixersHome = "Home: " + str(homeTeamPHI) + " " + str(homeScorePHI)
sixersAway = "Away: " + str(awayTeamPHI) + " " + str(awayScorePHI)

sixersGame = lastGameDatePHI + """
""" + sixersHome + """
""" + sixersAway + ""

# DETERMINING the WIN or LOSS
teamHome = homeTeamPHI
teamAway = awayTeamPHI

scoreHome = int(homeScorePHI)
scoreAway = int(awayScorePHI)

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game In Progress"
	elif teamHome == "Philadelphia 76ers" and scoreHome > scoreAway:
		return "76ers Win"
	elif teamAway == "Philadelphia 76ers" and scoreAway > scoreHome:
		return "76ers Win"
	else:
		return "76ers Lose"

win()

######################################################################
#NEXT GAME

#Next Game Info Variables MAGIC 134883
try:
	nextOppPHI = NGparsePHI["events"][0]["strEventAlternate"]
	nextHomePHI = NGparsePHI["events"][0]["strHomeTeam"]
	nextAwayPHI = NGparsePHI["events"][0]["strAwayTeam"]
	nextOppDatePHI = NGparsePHI["events"][0]["dateEventLocal"]
except:
	nextOppPHI = 'null'
	nextHomePHI = 'null'
	nextAwayPHI = 'null'
	nextOppDatePHI = 'TBD'

#Season Suspension Variables
nextGameOpp = "No Games at the Moment"
nextGameLoc = "In the Bubble"


#DETERMINING NEXT OPPONENT

def next():
	if nextHomePHI == "Philadelphia 76ers":
		return str(nextAwayPHI)
	elif nextAwayPHI == "Philadelphia 76ers":
		return "@" + str(nextHomePHI)

next()


#DETERMINING WHERE NEXT OPPONENT

def where():
	if nextHomePHI == "Philadelphia 76ers":
		return "@Home" + " --- " + teamStadiumPHI
	elif nextAwayPHI == "Philadelphia 76ers":
		return "Away"

where()
