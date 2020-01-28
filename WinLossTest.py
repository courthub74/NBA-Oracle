# PISTONS General Info 134872
pistonsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Detroit%20Pistons")
# PISTONS Last Game 134872
pistonsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134872")
# PISTONS Next Game 134872
pistonsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134872")

# General Info Parsed
dataDET = pistonsRE.text
parseDET = json.loads(dataDET)
# For the Test
# print(pistonsRE.status_code)
# print(json.dumps(parseDET, indent=4))

# Last Game Parsed
LGdataDET = pistonsLG.text
LGparseDET = json.loads(LGdataDET)

# Next Game Parsed
NGdataDET = pistonsNG.text
NGparseDET = json.loads(NGdataDET)

homeTeamDET = LGparseDET["results"][0]["strHomeTeam"]
awayTeamDET = LGparseDET["results"][0]["strAwayTeam"]
homeScoreDET = LGparseDET["results"][0]["intHomeScore"]
awayScoreDET = LGparseDET["results"][0]["intAwayScore"]

#####################################################################
pistonsHome = str(homeTeamDET) + str(homeScoreDET)
pistonsAway = str(awayTeamDET) + str(awayScoreDET)

print(pistonsHome)
print(pistonsAway)

# THE ISSUE IS IN THIS QUADRANT.  YOU NEED TO FIGURE OUT HOW TO DETERMINE
# WHICH TEAM IS WHICH IN YOUR CODE BY STRING
# CREATE A VARIABLE THAT STATES WINNING TEAM
# AND THEN MATCH THAT STRING TO THE CALL WIN CALL LOSS FUNCTIONS
######################################################################

def CallWinnerDET():
    if str(pistonsHome) > str(pistonsAway):
        return pistonsHome


winner2 = CallWinnerDET()


def CountWinDET():
    if winner2 == "Detroit Pistons":
        print("W")


CountWinDET()


def CountLossDET():
    if winner2 != "Detroit Pistons":
        print("L")


CountLossDET()
