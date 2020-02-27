import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# MILWAUKEE BUCKS General Info 134874
bucksRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Milwaukee%20Bucks")
# Last Game info for BUCKS 134874
bucksLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134874")
# Next Game info for BUCKS 134874
bucksNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134874")

# BUCKS General Info Parsed 134874
dataMIL = bucksRE.text
parseMIL = json.loads(dataMIL)
# Last Game Parsed
LGdataMIL = bucksLG.text
LGparseMIL = json.loads(LGdataMIL)
# Next Game Parsed
NGdataMIL = bucksNG.text
NGparseMIL = json.loads(NGdataMIL)

# info Layout for the Drop Down Menu to Gather from BUCKS 134874
bucksTeam = parseMIL["teams"][0]["strTeam"]
yearFormedMIL = parseMIL["teams"][0]["intFormedYear"]
teamStadiumMIL = parseMIL["teams"][0]["strStadium"]
teamInfoMIL = parseMIL["teams"][0]["strDescriptionEN"]
lastGameDateMIL = LGparseMIL["results"][0]["dateEventLocal"]
homeTeamMIL = LGparseMIL["results"][0]["strHomeTeam"]
awayTeamMIL = LGparseMIL["results"][0]["strAwayTeam"]
homeScoreMIL = LGparseMIL["results"][0]["intHomeScore"]
awayScoreMIL = LGparseMIL["results"][0]["intAwayScore"]

# Last Game Info Printout BUCKS
bucksHome = "Home: " + str(homeTeamMIL) + " " + str(homeScoreMIL)
bucksAway = "Away: " + str(awayTeamMIL) + " " + str(awayScoreMIL)

bucksGame = lastGameDateMIL + """
""" + bucksHome + """
""" + bucksAway + ""

# DETERMINING the WIN or LOSS
teamHome = homeTeamMIL
teamAway = awayTeamMIL 

scoreHome = int(homeScoreMIL)
scoreAway = int(awayScoreMIL)   # Turned these into simple variables for my own sanity

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "Milwaukee Bucks" and scoreHome > scoreAway:
		return "Bucks Win"
	elif teamAway == "Milwaukee Bucks" and scoreAway > scoreHome:
		return "Bucks Win"
	else:
		return "Bucks Lose"

win()

