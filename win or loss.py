# FOR ATLANTA

homeTeam = homeTeamATL
oppTeam = awayTeamATL


def CallWinner():
    if str(homeScoreATL) > str(awayScoreATL):
        return homeTeam


winner = CallWinner()


# ALL THE FUNCTION ABOVE DOES IS COMPARE HOME TEAM SCORE TO AWAY TEAM SCORE AND RETURN OPP TEAM IF LOSS

# BELOW YOU ARE USING THE OUTCOME TO LOOK FOR THE FOCUS TEAM AND IF THEY WON OR NOT


def CountWin(*args):
    if winner == "Atlanta Hawks":
        outcomeOut.delete(0.0, 'end')
        won = "W"
        outcomeOut.insert(INSERT, won)


def CountLoss(*args):
    if winner != "Atlanta Hawks":
        outcomeOut.delete(0.0, 'end')
        loss = "L"
        outcomeOut.insert(INSERT, loss)
        

TeamsVar.trace("w", CountWin)
TeamsVar.trace("w", CountLoss)
