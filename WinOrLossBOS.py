BOShomeTeam = homeTeamBOS
BOSoppTeam = awayTeamBOS


def BOSCallWinner():
    if str(homeScoreBOS) > str(awayScoreBOS):
        return BOShomeTeam


BOSwinner = BOSCallWinner()


# ALL THE FUNCTION ABOVE DOES IS COMPARE HOME TEAM SCORE TO AWAY TEAM

# BELOW YOU ARE USING THE OUTCOME TO LOOK FOR THE FOCUS TEAM BY
# ENTERING THE STRING OF THE 'FOCUS TEAM' COMPARING IT TO THE WINNER


def BOSCountWin(*args):
    if BOSwinner == "Boston Celtics":
        return "W"


BOSCountWin()
BOSwin = BOSCountWin()


def BOSCountLoss(*args):
    if BOSwinner != "Boston Celtics":
        return "L"
    
    
BOSCountLoss()
BOSloss = BOSCountLoss()

