import requests
import json

# TEAM DATA API SCRAPING
###############################################################
# ATLANTA HAWKS

# ATLANTA General Info 134880
hawksRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Atlanta%20Hawks")  # Sends a URL request to API
# ATLANTA Last Game 134880
hawksLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134880")
# ATLANTA Next Game 134880
hawksNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134880")

# ATLANTA Info Parse 134880
dataATL = hawksRE.text # json data to text
parseATL = json.loads(dataATL) # converts reads or parses json as a string
									# If I try to use the .text variable it will return an error saying 
# ATLANTA Last Game Parse 134880      # It can't read the json data as a string
LGdataATL = hawksLG.text
LGparseATL = json.loads(LGdataATL)            # Done for all 3 requests

# ATLANTA Next Game Parse 134880
NGdataATL = hawksNG.text
NGparseATL = json.loads(NGdataATL)

######################################################################
# LAST GAME

# Last Game Info Variables ATLANTA 134880         # Now I can pull string data from the API
hawksTeam = parseATL["teams"][0]["strTeam"]         # I created variables for each desired data object
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
scoreAway = int(awayScoreATL)   # Turned these into simple variables for my own sanity

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

######################################################################
# NEXT GAME

# Next Game Info Variables ATLANTA 134880 
nextOppATL = NGparseATL["events"][0]["strEventAlternate"]
nextHomeATL = NGparseATL["events"][0]["strHomeTeam"]
nextAwayATL = NGparseATL["events"][0]["strAwayTeam"]

# DETERMINING NEXT OPPONENT

def next():
	if nextHomeATL == "Atlanta Hawks":
		return str(nextAwayATL)
	elif nextAwayATL == "Atlanta Hawks":
		return str(nextHomeATL)

next()


# DETERMINING WHERE NEXT OPPONENT

def where():
	if nextHomeATL == "Atlanta Hawks":
		return "Home"
	else:
		return "Away"

where()

