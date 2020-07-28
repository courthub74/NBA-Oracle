import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# UTAH JAZZ

# JAZZ General Info 134879
jazzRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Utah_jazz")
# JAZZ Last Game 134879
jazzLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134889")
# JAZZ Next Game 134879
jazzNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134889")

# JAZZ General Info Parse 134879
dataUTAH = jazzRE.text
parseUTAH = json.loads(dataUTAH)

# JAZZ Last Game Parse 134879
LGdataUTAH = jazzLG.text
LGparseUTAH = json.loads(LGdataUTAH)

# JAZZ Next Game Parse 134879
NGdataUTAH  = jazzNG.text
NGparseUTAH = json.loads(NGdataUTAH)


######################################################################
# LAST GAME

# Last Game Info Variables JAZZ 134879
jazzTeam = parseUTAH["teams"][0]["strTeam"]
yearFormedUTAH = parseUTAH["teams"][0]["intFormedYear"]
teamStadiumUTAH = parseUTAH["teams"][0]["strStadium"]
teamInfoUTAH = parseUTAH["teams"][0]["strDescriptionEN"]
lastGameDateUTAH = LGparseUTAH["results"][0]["dateEventLocal"]
homeTeamUTAH = LGparseUTAH["results"][0]["strHomeTeam"]
awayTeamUTAH = LGparseUTAH["results"][0]["strAwayTeam"]
homeScoreUTAH = LGparseUTAH["results"][0]["intHomeScore"]
awayScoreUTAH = LGparseUTAH["results"][0]["intAwayScore"]

# Last Game Info Printout
jazzHome = "Home: " + str(homeTeamUTAH) + " " + str(homeScoreUTAH)
jazzAway = "Away: " + str(awayTeamUTAH) + " " + str(awayScoreUTAH)

jazzGame = lastGameDateUTAH + """
""" + jazzHome + """
""" + jazzAway + ""

# DETERMINING the WIN or LOSS
teamHome = homeTeamUTAH
teamAway = awayTeamUTAH

scoreHome = int(homeScoreUTAH)
scoreAway = int(awayScoreUTAH)

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "Utah Jazz" and scoreHome > scoreAway:
		return "Jazz Win"
	elif teamAway == "Utah Jazz" and scoreAway > scoreHome:
		return "Jazz Win"
	else:
		return "Jazz Lose"

win()


######################################################################
#NEXT GAME

#Next Game Info Variables KINGS 134869
try:
	nextOppUTAH = NGparseUTAH["events"][0]["strEventAlternate"]
	nextHomeUTAH = NGparseUTAH["events"][0]["strHomeTeam"]
	nextAwayUTAH = NGparseUTAH["events"][0]["strAwayTeam"]
	nextOppDateUTAH = NGparseUTAH["events"][0]["dateEventLocal"]
except:
	nextOppUTAH = 'null'
	nextHomeUTAH = 'null'
	nextAwayUTAH = 'null'
	nextOppDateUTAH = 'TBD'

#Season Suspension Variables
nextGameOpp = "No Games at the Moment"
nextGameLoc = "In the Bubble"


#DETERMINING NEXT OPPONENT

def next():
	if nextHomeUTAH == "Utah Jazz":
		return str(nextAwayUTAH)
	elif nextAwayUTAH == "Utah Jazz":
		return "@" + str(nextHomeUTAH)

next()


#DETERMINING WHERE NEXT OPPONENT

def where():
	if nextHomeUTAH == "Utah Jazz":
		return "@Home" + " --- " + teamStadiumUTAH
	elif nextAwayUTAH == "Utah Jazz":
		return "Away"

where()

