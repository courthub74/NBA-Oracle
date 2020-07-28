import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# WASHINGTON WIZARDS

# WIZARDS General Info 134884
wizzardsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Washington_Wizards")
# WIZARDS Last Game 134884
wizzardsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134884")
# WIZARDS Next Game 134884
wizzardsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134884")

# WIZARDS General Info Parse 134884
dataWAS = wizzardsRE.text
parseWAS = json.loads(dataWAS)

# WIZARDS Last Game Parse 134884
LGdataWAS = wizzardsLG.text
LGparseWAS = json.loads(LGdataWAS)

# WIZARDS Next Game Parse 134884
NGdataWAS  = wizzardsNG.text
NGparseWAS = json.loads(NGdataWAS)


######################################################################
# LAST GAME

# Last Game Info Variables WIZARDS 134884
wizzardsTeam = parseWAS["teams"][0]["strTeam"]
yearFormedWAS = parseWAS["teams"][0]["intFormedYear"]
teamStadiumWAS = parseWAS["teams"][0]["strStadium"]
teamInfoWAS = parseWAS["teams"][0]["strDescriptionEN"]
lastGameDateWAS = LGparseWAS["results"][0]["dateEventLocal"]
homeTeamWAS = LGparseWAS["results"][0]["strHomeTeam"]
awayTeamWAS = LGparseWAS["results"][0]["strAwayTeam"]
homeScoreWAS = LGparseWAS["results"][0]["intHomeScore"]
awayScoreWAS = LGparseWAS["results"][0]["intAwayScore"]

# Last Game Info Printout
wizzardsHome = "Home: " + str(homeTeamWAS) + " " + str(homeScoreWAS)
wizzardsAway = "Away: " + str(awayTeamWAS) + " " + str(awayScoreWAS)

wizzardsGame = lastGameDateWAS + """
""" + wizzardsHome + """
""" + wizzardsAway + ""

# DETERMINING the WIN or LOSS
teamHome = homeTeamWAS
teamAway = awayTeamWAS

scoreHome = int(homeScoreWAS)
scoreAway = int(awayScoreWAS)

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "Washington Wizards" and scoreHome > scoreAway:
		return "Wizards Win"
	elif teamAway == "Washington Wizards" and scoreAway > scoreHome:
		return "Wizards Win"
	else:
		return "Wizards Lose"

win()


######################################################################
#NEXT GAME

#Next Game Info Variables WIZARDS 134884
try:
	nextOppWAS = NGparseWAS["events"][0]["strEventAlternate"]
	nextHomeWAS = NGparseWAS["events"][0]["strHomeTeam"]
	nextAwayWAS = NGparseWAS["events"][0]["strAwayTeam"]
	nextOppDateWAS = NGparseWAS["events"][0]["dateEventLocal"]
except:
	nextOppWAS = 'null'
	nextHomeWAS = 'null'
	nextAwayWAS = 'null'
	nextOppDateWAS = 'TBD'

#Season Suspension Variables
nextGameOpp = "No Games at the Moment"
nextGameLoc = "In the Bubble"


#DETERMINING NEXT OPPONENT

def next():
	if nextHomeWAS == "Washington Wizards":
		return str(nextAwayWAS)
	elif nextAwayWAS == "Washington Wizards":
		return "@" + str(nextHomeWAS)

next()


#DETERMINING WHERE NEXT OPPONENT

def where():
	if nextHomeWAS == "Washington Wizards":
		return "@Home" + " --- " + teamStadiumWAS
	elif nextAwayWAS == "Washington Wizards":
		return "Away"

where()

