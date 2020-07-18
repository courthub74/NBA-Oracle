import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# MINNESOTA TIMBERWOLVES

# T WOLVES General Info 134886
twolvesRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Minnesota%20Timberwolves")
# T-WOLVES Last Game Info
twolvesLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134886")
# T-WOLVES Next Game Info
twolvesNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134886")

# T-WOLVES General Info Parsed 134886
dataMIN = twolvesRE.text
parseMIN = json.loads(dataMIN)
# Last Game Parsed
LGdataMIN = twolvesLG.text
LGparseMIN = json.loads(LGdataMIN)
# Next Game Parsed
NGdataMIN = twolvesNG.text
NGparseMIN = json.loads(NGdataMIN)

# info Layout for the Drop Down Menu to Gather from T-WOLVES 134866
twolvesTeam = parseMIN["teams"][0]["strTeam"]
yearFormedMIN = parseMIN["teams"][0]["intFormedYear"]
teamStadiumMIN = parseMIN["teams"][0]["strStadium"]
teamInfoMIN = parseMIN["teams"][0]["strDescriptionEN"]
lastGameDateMIN = LGparseMIN["results"][0]["dateEventLocal"]
homeTeamMIN = LGparseMIN["results"][0]["strHomeTeam"]
awayTeamMIN = LGparseMIN["results"][0]["strAwayTeam"]
homeScoreMIN = LGparseMIN["results"][0]["intHomeScore"]
awayScoreMIN = LGparseMIN["results"][0]["intAwayScore"]

# Last Game Info Printout BUCKS
twolvesHome = "Home: " + str(homeTeamMIN) + " " + str(homeScoreMIN)
twolvesAway = "Away: " + str(awayTeamMIN) + " " + str(awayScoreMIN)

twolvesGame = lastGameDateMIN + """
""" + twolvesHome + """
""" + twolvesAway + ""


# DETERMINING the WIN or LOSS
teamHome = homeTeamMIN
teamAway = awayTeamMIN 

scoreHome = int(homeScoreMIN)
scoreAway = int(awayScoreMIN)   # Turned these into simple variables for my own sanity for the win()

def win():
	if scoreHome < 80 and scoreAway < 80:
		return "Game in Progress"
	elif teamHome == "Minnesota Timberwolves" and scoreHome > scoreAway:
		return "T-Wolves Win"
	elif teamAway == "Minnesota Timberwolves" and scoreAway > scoreHome:
		return "T-Wolves Win"
	else:
		return "T-Wolves Lose"

win()
