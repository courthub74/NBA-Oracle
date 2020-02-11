import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# ATLANTA HAWKS

# ATLANTA General Info 134880
hawksRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Atlanta%20Hawks")
# ATLANTA Last Game 134880
hawksLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134880")
# ATLANTA Next Game 134880
hawksNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134880")

# ATLANTA Info Parse 134880
dataATL = hawksRE.text
parseATL = json.loads(dataATL)

# ATLANTA Last Game Parse 134880
LGdataATL = hawksLG.text
LGparseATL = json.loads(LGdataATL)

# ATLANTA Next Game Parse 134880
NGdataATL = hawksNG.text
NGparseATL = json.loads(NGdataATL)

# Info Layout for Drop Down ATLANTA 134880
hawksTeam = parseATL["teams"][0]["strTeam"]
yearFormedATL = parseATL["teams"][0]["intFormedYear"]
teamStadiumATL = parseATL["teams"][0]["strStadium"]
teamInfoATL = parseATL["teams"][0]["strDescriptionEN"]
lastGameDateATL = LGparseATL["results"][0]["dateEventLocal"]
homeTeamATL = LGparseATL["results"][0]["strHomeTeam"]
awayTeamATL = LGparseATL["results"][0]["strAwayTeam"]
homeScoreATL = LGparseATL["results"][0]["intHomeScore"]
awayScoreATL = LGparseATL["results"][0]["intAwayScore"]

# Last Game Info Printout
hawksHome = "Home: " + str(homeTeamATL) + " " + str(homeScoreATL)
hawksAway = "Away: " + str(awayTeamATL) + " " + str(awayScoreATL)

hawksGame = lastGameDateATL + """
""" + hawksHome + """
""" + hawksAway + ""

# DETERMINING the WIN or LOSS
teamHome = homeTeamATL
teamAway = awayTeamATL 

scoreHome = int(homeScoreATL)
scoreAway = int(awayScoreATL)

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "Atlanta Hawks" and scoreHome > scoreAway:
		return "Hawks Win"
	elif teamAway == "Atlanta Hawks" and scoreAway > scoreHome:
		return "Hawks Win"
	else:
		return "Hawks Lose"

win()



