HomeTeam = "oppTeam"
AwayTeam = "focusTeam"
HomeScore = "123"
AwayScore = "156"

def home():
	if HomeTeam == "focusTeam":
		x = HomeScore
		print(x)

def away():
	if HomeTeam == "oppTeam":
		x = AwayScore
		print(x)
		

home()
away()

def compare():
	if HomeScore > AwayScore:
		y = "Home team Wins"
		print(y)
	elif HomeScore < AwayScore:
		y = "Home team Losses"
		print(y)

compare()



def CountWinLoss(*args):
        outcomeOut.delete(0.0, 'end')
        outcome = compare
        outcomeOut.insert(INSERT, won)

        
TeamsVar.trace("w", CountWinLoss)
