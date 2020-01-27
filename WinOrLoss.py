ATLhomeTeam = homeTeamATL
oppTeam = awayTeamATL


def CallWinner():
    if str(homeScoreATL) > str(awayScoreATL):
        return ATLhomeTeam


winner = CallWinner()


# ALL THE FUNCTION ABOVE DOES IS COMPARE HOME TEAM SCORE TO AWAY TEAM

# BELOW YOU ARE USING THE OUTCOME TO LOOK FOR THE FOCUS TEAM BY
# ENTERING THE STRING OF THE 'FOCUS TEAM' COMPARING IT TO THE WINNER


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
