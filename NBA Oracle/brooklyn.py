import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# BROOKLYN NETS

# NETS General Info 134861
netsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Brooklyn%20Nets")
# NETS Last Game 134861
netsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134861")
# NETS Next Game 134861
netsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134861")

# General Info Parsed
dataBKN = netsRE.text
parseBKN = json.loads(dataBKN)

# Last Game Parsed
LGdataBKN = netsLG.text
LGparseBKN = json.loads(LGdataBKN)

# Next Game Parsed
NGdataBKN = netsNG.text
NGparseBKN = json.loads(NGdataBKN)

# info Layout for the Drop Down Menu to Gather from NETS 134861
netsTeam = parseBKN["teams"][0]["strTeam"]
yearFormedBKN = parseBKN["teams"][0]["intFormedYear"]
teamStadiumBKN = parseBKN["teams"][0]["strStadium"]
teamInfoBKN = parseBKN["teams"][0]["strDescriptionEN"]
lastGameDateBKN = LGparseBKN["results"][0]["dateEventLocal"]
homeTeamBKN = LGparseBKN["results"][0]["strHomeTeam"]
awayTeamBKN = LGparseBKN["results"][0]["strAwayTeam"]
homeScoreBKN = LGparseBKN["results"][0]["intHomeScore"]
awayScoreBKN = LGparseBKN["results"][0]["intAwayScore"]

# Last Game Info Printout NETS
netsHome = "Home: " + str(homeTeamBKN) + " " + str(homeScoreBKN)
netsAway = "Away: " + str(awayTeamBKN) + " " + str(awayScoreBKN)

netsGame = lastGameDateBKN + """
""" + netsHome + """
""" + netsAway + ""

# DETERMINING the WIN or LOSS
teamHome = homeTeamBKN
teamAway = awayTeamBKN 

scoreHome = int(homeScoreBKN) 
scoreAway = int(awayScoreBKN)

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "Brooklyn Nets" and scoreHome > scoreAway:
		return "Nets Win"
	elif teamAway == "Brooklyn Nets" and scoreAway > scoreHome:
		return "Nets Win"
	else:
		return "Nets Lose"

win()
