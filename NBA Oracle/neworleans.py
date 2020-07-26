import requests
import json

# TEAM DATA API SCRAPING
###############################################################
#NEW ORLEANS PELICANS

# PELICANS General Info 134878
pelicansRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=New%20Orleans%20Pelicans")
# PELICANS Last Game 134878
pelicansLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134878")
# PELICANS Next Game 134878
pelicansNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134878")

# PELICANS General Info Parse
dataNOP = pelicansRE.text
parseNOP = json.loads(dataNOP)
# PELICANS Last Game Parse
LGdataNOP = pelicansLG.text
LGparseNOP = json.loads(LGdataNOP)
# PELICANS Next Game Parse
NGdataNOP = pelicansNG.text
NGparseNOP = json.loads(NGdataNOP)

# Last Game Info Variables PELICANS 134878
pelicansTeam = parseNOP["teams"][0]["strTeam"]
yearFormedNOP = parseNOP["teams"][0]["intFormedYear"]
teamStadiumNOP = parseNOP["teams"][0]["strStadium"]
teamInfoNOP = parseNOP["teams"][0]["strDescriptionEN"]
lastGameDateNOP = LGparseNOP["results"][0]["dateEventLocal"]
homeTeamNOP = LGparseNOP["results"][0]["strHomeTeam"]
awayTeamNOP = LGparseNOP["results"][0]["strAwayTeam"]
homeScoreNOP = LGparseNOP["results"][0]["intHomeScore"]
awayScoreNOP = LGparseNOP["results"][0]["intAwayScore"]

# Last Game Info Printout PELICANS
pelicansHome = "Home: " + str(homeTeamNOP) + " " + str(homeScoreNOP)
pelcansAway = "Away: " + str(awayTeamNOP) + " " + str(awayScoreNOP)

pelicansGame = lastGameDateNOP + """
""" + pelicansHome + """
""" + pelcansAway + ""

# DETERMINING the WIN or LOSS
teamHome = homeTeamNOP
teamAway = awayTeamNOP

scoreHome = int(homeScoreNOP)
scoreAway = int(awayScoreNOP)

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "New Orleans Pelicans" and scoreHome > scoreAway:
		return "Pelicans Win"
	elif teamAway == "New Orleans Pelicans" and scoreAway > scoreHome:
		return "Pelicans Win"
	else:
		return "Pelicans Lose"

win()


#######################################################################################
# NEXT GAME

# Next Game Info Variables PELICANS 134878

try:
	nextOppNOP = NGparseNOP["events"][0]["strEventAlternate"]
	nextHomeNOP = NGparseNOP["events"][0]["strHomeTeam"]
	nextAwayNOP = NGparseNOP["events"][0]["strAwayTeam"]
	nextOppDateNOP = NGparseNOP["events"][0]["dateEventLocal"] 
except:
	nextOppNOP = 'null'
	nextHomeNOP = 'null'
	nextAwayNOP = 'null'
	nextOppDateNOP = "TBD" 

#Season Suspension Variables
nextGameOpp = "No Games at the Moment"
nextGameLoc = "In the Bubble"


# DETERMINING NEXT OPPONENT

def next():
	if nextHomeNOP == "New Orleans Pelicans":
		return str(nextAwayNOP)
	elif nextAwayNOP == "New Orleans Pelicans":
		return "@" + str(nextHomeNOP)

next()


# DETERMINING WHERE NEXT OPPONENT

def where():
	if nextHomeNOP == "New Orleans Pelicans":
		return "@Home"  + " --- " + teamStadiumNOP
	elif nextAwayNOP == "New Orleans Pelicans":
		return "Away"

where()

# In Case you need to review API data
# print(json.dumps(x, indent=4))