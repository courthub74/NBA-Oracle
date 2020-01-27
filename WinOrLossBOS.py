BOShomeTeam = homeTeamBOS
BOSoppTeam = awayTeamBOS


def BOSCallWinner():
    if str(homeScoreBOS) > str(awayScoreBOS):
        return BOShomeTeam


BOSwinner = BOSCallWinner()


def BOSCountWin(*args):
    if BOSwinner == "Boston Celtics":
        outcomeOut.delete(0.0, 'end')
        won = "W"
        outcomeOut.insert(INSERT, won)


def BOSCountLoss(*args):
    if BOSwinner != "Boston Celtics":
        outcomeOut.delete(0.0, 'end')
        loss = "L"
        outcomeOut.insert(INSERT, loss)
