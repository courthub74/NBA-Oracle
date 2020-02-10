# BELOW is the code for determining 

# Starting with the ATL:

teamHome = homeTeamATL
teamAway = awayTeamATL 

scoreHome = homeScoreATL 
scoreAway = awayScoreATL 


def win():
	if teamHome == "Atlanta Hawks" and scoreHome > scoreAway:
		return "Hawks Win"
		
		
	elif teamAway == "Atlanta Hawks" and scoreAway > scoreHome:
		return "Hawks Win"
		#print("Hawks Win")
	else:
		return "Hawks Lose"
		#print("Hawks Lose")

win()

# Then you call it on the display side comme ca:

def callWinLoss(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		outcomeOutput.delete(0.0, END)
		hawksStanding = atlanta.win() 
		outcomeOutput.insert(INSERT, hawksStanding)
    
TeamsVar.trace("w", callWinLoss)
