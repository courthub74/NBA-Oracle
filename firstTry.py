import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# DENVER NUGGETS


# NUGGETS Info Parsed 134885
nuggetsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Denver%20Nuggets")
# NUGGETS Last Game 134885
nuggetsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134885")
# NUGGETS Next Game 134885
nuggetsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134885")

# General Info Parsed
dataDEN = nuggetsRE.text
parseDEN = json.loads(dataDEN)

# Last Game Parsed
LGdataDEN = nuggetsLG.text
LGparseDEN = json.loads(LGdataDEN)

# Next Game Parsed
NGdataDEN = nuggetsNG.text
NGparseDEN = json.loads(NGdataDEN)

# info Layout for the Drop Down Menu to Gather from NUGGETS 134885
nuggetsTeam = parseDEN["teams"][0]["strTeam"]
yearFormedDEN = parseDEN["teams"][0]["intFormedYear"]
teamStadiumDEN = parseDEN["teams"][0]["strStadium"]
teamInfoDEN = parseDEN["teams"][0]["strDescriptionEN"]
lastGameDateDEN = LGparseDEN["results"][0]["dateEventLocal"]
homeTeamDEN = LGparseDEN["results"][0]["strHomeTeam"]
awayTeamDEN = LGparseDEN["results"][0]["strAwayTeam"]
homeScoreDEN = LGparseDEN["results"][0]["intHomeScore"]
awayScoreDEN = LGparseDEN["results"][0]["intAwayScore"]

# Last Game Info Printout PISTONS
nuggetsHome = "Home: " + str(homeTeamDEN) + " " + str(homeScoreDEN)
nuggetsAway = "Away: " + str(awayTeamDEN) + " " + str(awayScoreDEN)

nuggetsGame = lastGameDateDEN + """
""" + nuggetsHome + """
""" + nuggetsAway + ""


# DETERMINING the WIN or LOSS
team1 = homeTeamDEN
team2 = awayTeamDEN

scoreHome = homeScoreDEN
scoreAway = awayScoreDEN

def home():
	if team1 == "Denver Nuggets":
		print(nuggetsTeam + " at home")

def homeWin():
	if scoreHome > scoreAway:
		print("Nuggets win")
		

def away():
	if team2 == "Denver Nuggets":
		print(nuggetsTeam + " away")

def awayWin():
	if scoreAway > scoreHome:
		print("Nuggets Lose")
		
		
home()
away()
awayWin()
homeWin()


def win():
	if team1 == "Denver Nuggets" and scoreHome > scoreAway:
		print("Nuggets Win")
	elif team2 == "Denver Nuggets" and scoreAway > scoreHome:
		print("Nuggets Win")
	else:
		print("Nuggets Lose")

win()


# NOW we just need to count the wins or losses



