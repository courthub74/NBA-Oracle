focusTeam = homeTeamBOS
oppTeam = awayTeamBOS


def callWinner():
    if str(homeScoreBOS) > str(awayScoreBOS):
        return focusTeam


winner = callWinner()
# print(callWinner())
print(winner)


def countWin1():
    if winner == "Boston Celtics":
        print("W")


countWin1()


def countLoss1():
    if winner != "Boston Celtics":
        print("L")


countLoss1()
