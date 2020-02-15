# BELOW is the code for determining WIN | LOSS | IN PROGRESS

# Starting with the ATL:

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


# Then you call it on the display side comme ca:

def callWinLoss(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		outcomeOutput.delete(0.0, END)
		hawksStanding = atlanta.win() 
		outcomeOutput.insert(INSERT, hawksStanding)
    
TeamsVar.trace("w", callWinLoss)
