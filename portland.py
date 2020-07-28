import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# PORTLAND TRAILBLAZERS

# PORTLAND General Info 134888
portlandRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Portland_Trail_Blazers")
# PORTLAND Last Game 134888
portlandLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134888")
# PORTLAND Next Game 134888
portlandNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134888")

# PORTLAND General Info Parse 134888
dataPOR = portlandRE.text
parsePOR = json.loads(dataPOR)

# PORTLAND Last Game Parse 134888
LGdataPOR = portlandLG.text
LGparsePOR = json.loads(LGdataPOR)

# PORTLAND Next Game Parse 134888
NGdataPOR = portlandNG.text
NGparsePOR = json.loads(NGdataPOR)


######################################################################
# LAST GAME

# Last Game Info Variables PORTLAND 134888
blazersTeam = parsePOR["teams"][0]["strTeam"]
yearFormedPOR = parsePOR["teams"][0]["intFormedYear"]
teamStadiumPOR = parsePOR["teams"][0]["strStadium"]
teamInfoPOR = parsePOR["teams"][0]["strDescriptionEN"]
lastGameDatePOR = LGparsePOR["results"][0]["dateEventLocal"]
homeTeamPOR = LGparsePOR["results"][0]["strHomeTeam"]
awayTeamPOR = LGparsePOR["results"][0]["strAwayTeam"]
homeScorePOR = LGparsePOR["results"][0]["intHomeScore"]
awayScorePOR = LGparsePOR["results"][0]["intAwayScore"]

# Last Game Info Printout
blazersHome = "Home: " + str(homeTeamPOR) + " " + str(homeScorePOR)
blazersAway = "Away: " + str(awayTeamPOR) + " " + str(awayScorePOR)

blazersGame = lastGameDatePOR + """
""" + blazersHome + """
""" + blazersAway + ""

# DETERMINING the WIN or LOSS
teamHome = homeTeamPOR
teamAway = awayTeamPOR

scoreHome = int(homeScorePOR)
scoreAway = int(awayScorePOR)

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "Portland Trail Blazers" and scoreHome > scoreAway:
		return "Blazers Win"
	elif teamAway == "Portland Trail Blazers" and scoreAway > scoreHome:
		return "Blazers Win"
	else:
		return "Blazers Lose"

win()


######################################################################
#NEXT GAME

#Next Game Info Variables PORTLAND 134888
try:
	nextOppPOR = NGparsePOR["events"][0]["strEventAlternate"]
	nextHomePOR = NGparsePOR["events"][0]["strHomeTeam"]
	nextAwayPOR = NGparsePOR["events"][0]["strAwayTeam"]
	nextOppDatePOR = NGparsePOR["events"][0]["dateEventLocal"]
except:
	nextOppPOR = 'null'
	nextHomePOR = 'null'
	nextAwayPOR = 'null'
	nextOppDatePOR = 'TBD'

#Season Suspension Variables
nextGameOpp = "No Games at the Moment"
nextGameLoc = "In the Bubble"


#DETERMINING NEXT OPPONENT

def next():
	if nextHomePOR == "Portland Trail Blazers":
		return str(nextAwayPOR)
	elif nextAwayPOR == "Portland Trail Blazers":
		return "@" + str(nextHomePOR)

next()


#DETERMINING WHERE NEXT OPPONENT

def where():
	if nextHomePOR == "Portland Trail Blazers":
		return "@Home" + " --- " + teamStadiumPOR
	elif nextAwayPOR == "Portland Trail Blazers":
		return "Away"

where()


