HomeTeam = "focusTeam"
AwayTeam = "oppTeam"
HomeScore = "123"
AwayScore = "112"

def team():
	if HomeTeam == "focusTeam":
		x = HomeScore
		print(x)

def away():
	if HomeTeam == "oppTeam":
		x = AwayScore
		print(x)
		

team()
away()

def compare():
	if HomeScore > AwayScore:
		y = "Win"
		print(y)
	elif HomeScore < AwayScore:
		y = "Loss"
		print(y)

compare()



def CountWinLoss(*args):
        outcomeOut.delete(0.0, 'end')
        outcome = compare
        outcomeOut.insert(INSERT, won)

        
TeamsVar.trace("w", CountWinLoss)
