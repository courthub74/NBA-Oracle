import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# DALLAS MAVERICKS

# MAVERICKS General Info 134875
mavsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Dallas%20Mavericks")
# MAVERICKS Last Game 134875
mavsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134875")
# MAVERICKS Next Game 134875
mavsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134875")

# General Info Parsed
dataDAL = mavsRE.text
parseDAL = json.loads(dataDAL)

# Last Game Parsed
LGdataDAL = mavsLG.text
LGparseDAL = json.loads(LGdataDAL)

# Next Game Parsed
NGdataDAL = mavsNG.text
NGparseDAL = json.loads(NGdataDAL)

# info Layout for the Drop Down Menu to Gather from MAVERICKS 134875
mavsTeam = parseDAL["teams"][0]["strTeam"]
yearFormedDAL = parseDAL["teams"][0]["intFormedYear"]
teamStadiumDAL = parseDAL["teams"][0]["strStadium"]
teamInfoDAL = parseDAL["teams"][0]["strDescriptionEN"]
lastGameDateDAL = LGparseDAL["results"][0]["dateEventLocal"]
homeTeamDAL = LGparseDAL["results"][0]["strHomeTeam"]
awayTeamDAL = LGparseDAL["results"][0]["strAwayTeam"]
homeScoreDAL = LGparseDAL["results"][0]["intHomeScore"]
awayScoreDAL = LGparseDAL["results"][0]["intAwayScore"]

# Last Game Info Printout MAVERICKS
mavsHome = "Home: " + str(homeTeamDAL) + " " + str(homeScoreDAL)
mavsAway = "Away: " + str(awayTeamDAL) + " " + str(awayScoreDAL)

mavsGame = lastGameDateDAL + """
""" + mavsHome + """
""" + mavsAway + ""

# DETERMINING the WIN or LOSS
teamHome = homeTeamDAL
teamAway = awayTeamDAL

scoreHome = int(homeScoreDAL)
scoreAway = int(awayScoreDAL)

def win():
	if int(scoreHome) < 80 and int(scoreAway) < 80:
		return "Game in Progress"
	elif teamHome == "Dallas Mavericks" and scoreHome > scoreAway:
		return "Mavs Win"
	elif teamAway == "Dallas Mavericks" and scoreAway > scoreHome:
		return "Mavs Win"
	else:
		return "Mavs Lose"

win()


######################################################################
# NEXT GAME

# Next Game Info Variables MAVERICKS 134875
try:
	nextOppDAL = NGparseDAL["events"][0]["strEventAlternate"]
	nextHomeDAL = NGparseDAL["events"][0]["strHomeTeam"]
	nextAwayDAL = NGparseDAL["events"][0]["strAwayTeam"]
	nextOppDateDAL = NGparseDAL["events"][0]["dateEventLocal"]
except:
	nextOppDAL = 'null'
	nextHomeDAL = 'null'
	nextAwayDAL = 'null'
	nextOppDateDAL = "TBD"


#Season Suspension Variables
nextGameOpp = "No Games at the Moment"
nextGameLoc = "In the Bubble"
	

# DETERMINING NEXT OPPONENT

def next():
	if nextHomeDAL == "Dallas Mavericks":
		return str(nextAwayDAL)
	elif nextAwayDAL == "Dallas Mavericks":
		return "@" + str(nextHomeDAL)

next()


# DETERMINING WHERE NEXT OPPONENT

def where():
	if nextHomeDAL == "Dallas Mavericks":
		return "@Home" + " --- " + teamStadiumDAL
	elif nextAwayDAL == "Dallas Mavericks":
		return "Away"

where()
