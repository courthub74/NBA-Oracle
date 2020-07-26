import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# OKLAHOMA CITY THUNDER

# OKLAHOMA General Info 134887
thunderRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Oklahoma_City_Thunder")
# OKLAHOMA Last Game 134887
thunderLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134887")
# OKLAHOMA Next Game 134887
thunderNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134887")

# OKLAHOMA Info Parse 134887
dataOKC = thunderRE.text
parseOKC = json.loads(dataOKC)

# OKLAHOMA Last Game Parse 134887
LGdataOKC = thunderLG.text
LGparseOKC = json.loads(LGdataOKC)

# OKLAHOMA Next Game Parse 134887
NGdataOKC = thunderNG.text
NGparseOKC = json.loads(NGdataOKC)


######################################################################
# LAST GAME

# Last Game Info Variables OKLAHOMA 134887
thunderTeam = parseOKC["teams"][0]["strTeam"]
yearFormedOKC = parseOKC["teams"][0]["intFormedYear"]
teamStadiumOKC = parseOKC["teams"][0]["strStadium"]
teamInfoOKC = parseOKC["teams"][0]["strDescriptionEN"]
lastGameDateOKC = LGparseOKC["results"][0]["dateEventLocal"]
homeTeamOKC = LGparseOKC["results"][0]["strHomeTeam"]
awayTeamOKC = LGparseOKC["results"][0]["strAwayTeam"]
homeScoreOKC = LGparseOKC["results"][0]["intHomeScore"]
awayScoreOKC = LGparseOKC["results"][0]["intAwayScore"]

# Last Game Info Printout
thunderHome = "Home: " + str(homeTeamOKC) + " " + str(homeScoreOKC)
thunderAway = "Away: " + str(awayTeamOKC) + " " + str(awayScoreOKC)

thunderGame = lastGameDateOKC + """
""" + thunderHome + """
""" + thunderAway + ""

# DETERMINING the WIN or LOSS
teamHome = homeTeamOKC
teamAway = awayTeamOKC

scoreHome = int(homeScoreOKC)
scoreAway = int(awayScoreOKC)

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "Oklahoma City Thunder" and scoreHome > scoreAway:
		return "Thunder Win"
	elif teamAway == "Oklahoma City Thunder" and scoreAway > scoreHome:
		return "Thunder Win"
	else:
		return "Thunder Lose"

win()


######################################################################
#NEXT GAME

#Next Game Info Variables OKLAHOMA 134887
try:
	nextOppOKC = NGparseOKC["events"][0]["strEventAlternate"]
	nextHomeOKC = NGparseOKC["events"][0]["strHomeTeam"]
	nextAwayOKC = NGparseOKC["events"][0]["strAwayTeam"]
	nextOppDateOKC = NGparseOKC["events"][0]["dateEventLocal"]
except:
	nextOppOKC = 'null'
	nextHomeOKC = 'null'
	nextAwayOKC = 'null'
	nextOppDateOKC = 'TBD'

#Season Suspension Variables
nextGameOpp = "No Games at the Moment"
nextGameLoc = "In the Bubble"


#DETERMINING NEXT OPPONENT

def next():
	if nextHomeOKC == "Oklahoma City Thunder":
		return str(nextAwayOKC)
	elif nextAwayOKC == "Oklahoma City Thunder":
		return "@" + str(nextHomeOKC)

next()


#DETERMINING WHERE NEXT OPPONENT

def where():
	if nextHomeOKC == "Oklahoma City Thunder":
		return "@Home" + " --- " + teamStadiumOKC
	elif nextAwayOKC == "Oklahoma City Thunder":
		return "Away"

where()


# DETERMINE THE STADIUM

'''you would have to trace the oppteam string to their stadium string'''



# In Case you need to review API data
# print(json.dumps(LGparseATL, indent=4))
