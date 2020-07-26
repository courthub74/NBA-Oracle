import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# ORLANDO MAGIC

# MAGIC General Info 134883
magicRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Orlando_Magic")
# MAGIC Last Game 134883
magicLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134883")
# MAGIC Next Game 134883
magicNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134883")

# MAGIC General Info Parse 134883
dataORL = magicRE.text
parseORL = json.loads(dataORL)

# MAGIC Last Game Parse 134883
LGdataORL = magicLG.text
LGparseORL = json.loads(LGdataORL)

# MAGIC Next Game Parse 134883
NGdataORL = magicNG.text
NGparseORL = json.loads(NGdataORL)


######################################################################
# LAST GAME

# Last Game Info Variables MAGIC 134883
magicTeam = parseORL["teams"][0]["strTeam"]
yearFormedORL = parseORL["teams"][0]["intFormedYear"]
teamStadiumORL = parseORL["teams"][0]["strStadium"]
teamInfoORL = parseORL["teams"][0]["strDescriptionEN"]
lastGameDateORL = LGparseORL["results"][0]["dateEventLocal"]
homeTeamORL = LGparseORL["results"][0]["strHomeTeam"]
awayTeamORL = LGparseORL["results"][0]["strAwayTeam"]
homeScoreORL = LGparseORL["results"][0]["intHomeScore"]
awayScoreORL = LGparseORL["results"][0]["intAwayScore"]

# Last Game Info Printout
magicHome = "Home: " + str(homeTeamORL) + " " + str(homeScoreORL)
magicAway = "Away: " + str(awayTeamORL) + " " + str(awayScoreORL)

magicGame = lastGameDateORL + """
""" + magicHome + """
""" + magicAway + ""

# DETERMINING the WIN or LOSS
teamHome = homeTeamORL
teamAway = awayTeamORL

scoreHome = int(homeScoreORL)
scoreAway = int(awayScoreORL)

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "Orlando Magic" and scoreHome > scoreAway:
		return "Magic Win"
	elif teamAway == "Orlando Magic" and scoreAway > scoreHome:
		return "Magic Win"
	else:
		return "Magic Lose"

win()


######################################################################
#NEXT GAME

#Next Game Info Variables MAGIC 134883
try:
	nextOppORL = NGparseORL["events"][0]["strEventAlternate"]
	nextHomeORL = NGparseORL["events"][0]["strHomeTeam"]
	nextAwayORL = NGparseORL["events"][0]["strAwayTeam"]
	nextOppDateORL = NGparseORL["events"][0]["dateEventLocal"]
except:
	nextOppORL = 'null'
	nextHomeORL = 'null'
	nextAwayORL = 'null'
	nextOppDateORL = 'TBD'

#Season Suspension Variables
nextGameOpp = "No Games at the Moment"
nextGameLoc = "In the Bubble"


#DETERMINING NEXT OPPONENT

def next():
	if nextHomeORL == "Orlando Magic":
		return str(nextAwayORL)
	elif nextAwayORL == "Orlando Magic":
		return "@" + str(nextHomeORL)

next()


#DETERMINING WHERE NEXT OPPONENT

def where():
	if nextHomeORL == "Orlando Magic":
		return "@Home" + " --- " + teamStadiumORL
	elif nextAwayORL == "Orlando Magic":
		return "Away"

where()

