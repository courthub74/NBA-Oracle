from tkinter import *
import teamslist
import atlanta
import boston
import brooklyn
import charlotte
import chicago
import cleveland
import dallas
import denver
import detroit
import goldenstate
import houston
import indiana
import losangelesC
import losangelesL
import memphis
import miami
import milwaukee
import minnesota
import neworleans
import newyork


# WINDOW
window = Tk()
window.geometry("1000x800")
window.iconbitmap("icon/NBAclear.ico")
window.title("NBA Oracle")
window.configure(background="Darkblue")

# HEADER
logo = PhotoImage(file="header/NBAclear.png")
logoNBA = Label(window, image=logo, bg="Darkblue")
resizeLogo = logo.subsample(1, 1)
logoNBA.config(image=resizeLogo)
logoNBA.grid(row=0,column=1,sticky=W)

# DROP DOWN MENU
TeamsVar = StringVar()  # Created a string variable for the drop down menu
TeamsVar.set(teamslist.TeamsList[0])
droplist = OptionMenu(window, TeamsVar, *teamslist.TeamsList)
droplist.config(width=45, height=1, fg="Darkblue")
droplist.grid(row=1,column=1,sticky=W)

# TEAM SELECTED
teamSelected = Label(window, text="Team Selected:", bg="Darkblue", fg="White", font="Helvetica 10 bold")
teamSelected.grid(row=2,column=0)
teamSelectedOutput = Text(window, width=40, height=1, bg="Black", fg="White")
teamSelectedOutput.grid(row=3,column=1,sticky=W)

# YEAR FORMED
yearFormed = Label(window, text="Year Formed:", bg="Darkblue", fg="White", font="Helvetica 10 bold")
yearFormed.grid(row=4,column=0)
yearFormedOutput = Text(window, width=20, height=1, bg="Black", fg="White")
yearFormedOutput.grid(row=5,column=1,sticky=W)

# TEAM STADIUM
teamStadium = Label(window, text="Team Stadium:", bg="Darkblue", fg="White", font="Helvetica 10 bold")
teamStadium.grid(row=6,column=0)
teamStadiumOutput = Text(window, width=40, height=1, bg="Black", fg="White")
teamStadiumOutput.grid(row=7,column=1,sticky=W)

# TEAM INFO
teamInfo = Label(window, text="Team Info:", bg="Darkblue", fg="White", font="Helvetica 10 bold")
teamInfo.grid(row=8,column=0)
teamInfoOutput = Text(window, width=55, height=5, wrap=WORD, bg="Black", fg="White")
teamInfoOutput.grid(row=9,column=1,sticky=W)

# LAST GAME
lastGame = Label(window, text="Last Game Played:", bg="Darkblue", fg="White", font="Helvetica 10 bold")
lastGame.grid(row=10,column=0)
lastGameOutput = Text(window, width=40, height=4, bg="Black", fg="White")
lastGameOutput.grid(row=11,column=1,sticky=W)

# WIN LOSS 
outcome = Label(window, text="Last Game Win/Loss:", bg="Darkblue", fg="White", font="Helvetica 10 bold")
outcome.grid(row=12,column=0)
outcomeOutput = Text(window, width=20, height=1, bg="Black", fg="White")
outcomeOutput.grid(row=13,column=1,sticky=W)

# WIN STREAK
streak = Label(window, text="Win Streak:", bg="Darkblue", fg="White", font="Helvetica 10 bold")
streak.grid(row=14,column=0)
streakOutput = Text(window, width=20, height=1, bg="Black", fg="White")
streakOutput.grid(row=15,column=1,sticky=W)

# NEXT OPPONENT
nextOpp = Label(window, text="Next Opponent:", bg="Darkblue", fg="White", font="Helvetica 10 bold")
nextOpp.grid(row=16,column=0)
nextOppOutput = Text(window, width=40, height=1, bg="Black", fg="White")
nextOppOutput.grid(row=17,column=1,sticky=W)

# NEXT GAME LOCATION
locNext = Label(window, text="Where:", bg="Darkblue", fg="White", font="Helvetica 10 bold")
locNext.grid(row=18,column=0)
locNextOutput = Text(window, width=40, height=1, bg="Black", fg="White")
locNextOutput.grid(row=19,column=1,sticky=W)

# NEXT GAME DATE 
nextDate = Label(window, text="Date:", bg="Darkblue", fg="White", font="Helvetica 10 bold")
nextDate.grid(row=20, column=0)
nextDateOutput = Text(window, width=20, height=1, bg="Black", fg="White")
nextDateOutput.grid(row=21, column=1,sticky=W)

# LOGO
LogoCanvas = Canvas(height=400, width=500, borderwidth=0, highlightthickness=0, bg="Darkblue", bd=0)
LogoCanvas.grid(row=2,column=6, rowspan=15, sticky=W)

# SPACE
space = Canvas(height=1, width=50, borderwidth=0, highlightthickness=0, bg="Darkblue", bd=0)
space.grid(row=4,column=2)

# LOGO LABEL
LabelCanvas = Text(window, height=1, width=10, borderwidth=0, highlightthickness=0, bg="Darkblue", fg="White", font="Denmark 15", bd=0)
LabelCanvas.grid(row=1,column=6,sticky=SW)



# FUNCTIONALITY
#############################################################
# CALL TEAM SELECTED 
def callTeamSelected(*args):
	if TeamsVar.get() == "Atlanta Hawks":  # If StringVar matches selected Var then proceed with this if state
		teamSelectedOutput.delete(0.0, END)  # Clear previous data from field 
		teamSelectedOutput.insert(INSERT, atlanta.hawksTeam)  # insert method to insert called variable into textfield. Variable is desired str parsed from API
	if TeamsVar.get() == "Boston Celtics":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, boston.celticsTeam)
	if TeamsVar.get() == "Brooklyn Nets":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, brooklyn.netsTeam)
	if TeamsVar.get() == "Charlotte Hornets":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, charlotte.hornetsTeam)
	if TeamsVar.get() == "Chicago Bulls":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, chicago.bullsTeam)
	if TeamsVar.get() == "Cleveland Cavaliers":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, cleveland.cavsTeam)
	if TeamsVar.get() == "Dallas Mavericks":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, dallas.mavsTeam)
	if TeamsVar.get() == "Denver Nuggets":
		teamSelectedOutput.delete(0.0, END) 
		teamSelectedOutput.insert(INSERT, denver.nuggetsTeam) 
	if TeamsVar.get() == "Detroit Pistons":
		teamSelectedOutput.delete(0.0, END) 
		teamSelectedOutput.insert(INSERT, detroit.pistonsTeam)
	if TeamsVar.get() == "Golden State Warriors":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, goldenstate.warriorsTeam)
	if TeamsVar.get() == "Houston Rockets":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, houston.rocketsTeam)
	if TeamsVar.get() == "Indiana Pacers":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, indiana.pacersTeam)
	if TeamsVar.get() == "Los Angeles Clippers":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, losangelesC.clippersTeam)
	if TeamsVar.get() == "Los Angeles Lakers":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, losangelesL.lakersTeam)
	if TeamsVar.get() == "Memphis Grizzlies":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, memphis.grizzTeam)
	if TeamsVar.get() == "Miami Heat":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, miami.heatTeam)
	if TeamsVar.get() == "Milwaukee Bucks":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, milwaukee.bucksTeam)
	if TeamsVar.get() == "Minnesota Timberwolves":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, minnesota.twolvesTeam)
	if TeamsVar.get() == "New Orleans Pelicans":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, neworleans.pelicansTeam)
	if TeamsVar.get() == "New York Knicks":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, newyork.knicksTeam)
	if TeamsVar.get() == "Oklahoma City Thunder":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, oklahoma.thunderTeam)

TeamsVar.trace("w", callTeamSelected) #Using the TRACE method associated with the TeamsVar string variable 
											# I directly called the function callTeamSelected 'w' for write writing to textfield
# CALL YEAR FORMED
def callYearFormed(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, atlanta.yearFormedATL)
	if TeamsVar.get() == "Boston Celtics":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, boston.yearFormedBOS)
	if TeamsVar.get() == "Brooklyn Nets":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, brooklyn.yearFormedBKN)
	if TeamsVar.get() == "Charlotte Hornets":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, charlotte.yearFormedCHA)
	if TeamsVar.get() == "Chicago Bulls":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, chicago.yearFormedCHI)
	if TeamsVar.get() == "Cleveland Cavaliers":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, cleveland.yearFormedCLE)
	if TeamsVar.get() == "Dallas Mavericks":
		yearFormedOutput.delete(0.0, END)
		dallas.yearFormedDAL
		yearFormedOutput.insert(INSERT, dallas.yearFormedDAL)
	if TeamsVar.get() == "Denver Nuggets":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, denver.yearFormedDEN)
	if TeamsVar.get() == "Detroit Pistons":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, detroit.yearFormedDET)
	if TeamsVar.get() == "Golden State Warriors":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, goldenstate.yearFormedGS)
	if TeamsVar.get() == "Houston Rockets":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, houston.yearFormedHOU)
	if TeamsVar.get() == "Indiana Pacers":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, indiana.yearFormedIND)
	if TeamsVar.get() == "Los Angeles Clippers":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, losangelesC.yearFormedLAC)
	if TeamsVar.get() == "Los Angeles Lakers":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, losangelesL.yearFormedLAL)
	if TeamsVar.get() == "Memphis Grizzlies":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, memphis.yearFormedMEM)
	if TeamsVar.get() == "Miami Heat":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, miami.yearFormedMIA)
	if TeamsVar.get() == "Milwaukee Bucks":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, milwaukee.yearFormedMIL)
	if TeamsVar.get() == "Minnesota Timberwolves":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, minnesota.yearFormedMIN)
	if TeamsVar.get() == "New Orleans Pelicans":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, neworleans.yearFormedNOP)
	if TeamsVar.get() == "New York Knicks":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, newyork.yearFormedNYK)
	if TeamsVar.get() == "Oklahoma City Thunder":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, thunder.yearFormedOKC)


TeamsVar.trace("w", callYearFormed)


# CALL TEAM STADIUM
def callTeamStadium(*args):
	if TeamsVar.get() == "Atlanta Hawks":  
		teamStadiumOutput.delete(0.0, END)  
		atlanta.teamStadiumATL
		teamStadiumOutput.insert(INSERT, atlanta.teamStadiumATL)
	if TeamsVar.get() == "Boston Celtics":
		teamStadiumOutput.delete(0.0, END)
		boston.teamStadiumBOS
		teamStadiumOutput.insert(INSERT, boston.teamStadiumBOS)
	if TeamsVar.get() == "Brooklyn Nets":
		teamStadiumOutput.delete(0.0, END)
		brooklyn.teamStadiumBKN
		teamStadiumOutput.insert(INSERT, brooklyn.teamStadiumBKN)
	if TeamsVar.get() == "Charlotte Hornets":
		teamStadiumOutput.delete(0.0, END)
		charlotte.teamStadiumCHA
		teamStadiumOutput.insert(INSERT, charlotte.teamStadiumCHA)
	if TeamsVar.get() == "Chicago Bulls": 
		teamStadiumOutput.delete(0.0, END)
		chicago.teamStadiumCHI
		teamStadiumOutput.insert(INSERT, chicago.teamStadiumCHI)
	if TeamsVar.get() == "Cleveland Cavaliers": 
		teamStadiumOutput.delete(0.0, END)
		cleveland.teamStadiumCLE
		teamStadiumOutput.insert(INSERT, cleveland.teamStadiumCLE)
	if TeamsVar.get() == "Dallas Mavericks":
		teamStadiumOutput.delete(0.0, END)
		dallas.teamStadiumDAL
		teamStadiumOutput.insert(INSERT, dallas.teamStadiumDAL)
	if TeamsVar.get() == "Denver Nuggets":
		teamStadiumOutput.delete(0.0, END)
		denver.teamStadiumDEN
		teamStadiumOutput.insert(INSERT, denver.teamStadiumDEN)
	if TeamsVar.get() == "Detroit Pistons":
		teamStadiumOutput.delete(0.0, END)
		detroit.teamStadiumDET
		teamStadiumOutput.insert(INSERT, detroit.teamStadiumDET)
	if TeamsVar.get() == "Golden State Warriors":
		teamStadiumOutput.delete(0.0, END)
		goldenstate.teamStadiumGS
		teamStadiumOutput.insert(INSERT, goldenstate.teamStadiumGS)
	if TeamsVar.get() == "Houston Rockets":
		teamStadiumOutput.delete(0.0, END)
		houston.teamStadiumHOU
		teamStadiumOutput.insert(INSERT, houston.teamStadiumHOU)
	if TeamsVar.get() == "Indiana Pacers":
		teamStadiumOutput.delete(0.0, END)
		indiana.teamStadiumIND
		teamStadiumOutput.insert(INSERT, indiana.teamStadiumIND)
	if TeamsVar.get() == "Los Angeles Clippers":
		teamStadiumOutput.delete(0.0, END)
		losangelesC.teamStadiumLAC
		teamStadiumOutput.insert(INSERT, losangelesC.teamStadiumLAC)
	if TeamsVar.get() == "Los Angeles Lakers":
		teamStadiumOutput.delete(0.0, END)
		losangelesL.teamStadiumLAL
		teamStadiumOutput.insert(INSERT, losangelesL.teamStadiumLAL)
	if TeamsVar.get() == "Memphis Grizzlies":
		teamStadiumOutput.delete(0.0, END)
		memphis.teamStadiumMEM
		teamStadiumOutput.insert(INSERT, memphis.teamStadiumMEM)
	if TeamsVar.get() == "Miami Heat":
		teamStadiumOutput.delete(0.0, END)
		miami.teamStadiumMIA
		teamStadiumOutput.insert(INSERT, miami.teamStadiumMIA)
	if TeamsVar.get() == "Milwaukee Bucks":
		teamStadiumOutput.delete(0.0, END)
		milwaukee.teamStadiumMIL
		teamStadiumOutput.insert(INSERT, milwaukee.teamStadiumMIL)
	if TeamsVar.get() == "Minnesota Timberwolves":
		teamStadiumOutput.delete(0.0, END)
		teamStadiumOutput.insert(INSERT, minnesota.teamStadiumMIN)
	if TeamsVar.get() == "New Orleans Pelicans":
		teamStadiumOutput.delete(0.0, END)
		teamStadiumOutput.insert(INSERT, neworleans.teamStadiumNOP)
	if TeamsVar.get() == "New York Knicks":
		teamStadiumOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, newyork.teamstadiumNYK)
	if TeamsVar.get() == "Oklahoma City Thunder":
		teamStadiumOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, thunder.teamstadiumOKC)
		
TeamsVar.trace("w", callTeamStadium)


# CALL TEAM INFO
def callTeamInfo(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		teamInfoOutput.delete(0.0, END)
		atlanta.teamInfoATL
		teamInfoOutput.insert(INSERT, atlanta.teamInfoATL)
	if TeamsVar.get() == "Boston Celtics":
		teamInfoOutput.delete(0.0, END)
		boston.teamInfoBOS
		teamInfoOutput.insert(INSERT, boston.teamInfoBOS)
	if TeamsVar.get() == "Brooklyn Nets":
		teamInfoOutput.delete(0.0, END)
		brooklyn.teamInfoBKN
		teamInfoOutput.insert(INSERT, brooklyn.teamInfoBKN)
	if TeamsVar.get() == "Charlotte Hornets":
		teamInfoOutput.delete(0.0, END)
		charlotte.teamInfoCHA
		teamInfoOutput.insert(INSERT, charlotte.teamInfoCHA)
	if TeamsVar.get() == "Chicago Bulls":
		teamInfoOutput.delete(0.0, END)
		chicago.teamInfoCHI
		teamInfoOutput.insert(INSERT, chicago.teamInfoCHI)
	if TeamsVar.get() == "Cleveland Cavaliers":
		teamInfoOutput.delete(0.0, END)
		cleveland.teamInfoCLE
		teamInfoOutput.insert(INSERT, cleveland.teamInfoCLE)
	if TeamsVar.get() == "Dallas Mavericks":
		teamInfoOutput.delete(0.0, END)
		dallas.teamInfoDAL
		teamInfoOutput.insert(INSERT, dallas.teamInfoDAL)
	if TeamsVar.get() == "Denver Nuggets":
		teamInfoOutput.delete(0.0, END)
		denver.teamInfoDEN
		teamInfoOutput.insert(INSERT, denver.teamInfoDEN)
	if TeamsVar.get() == "Detroit Pistons":
		teamInfoOutput.delete(0.0, END)
		detroit.teamInfoDET
		teamInfoOutput.insert(INSERT, detroit.teamInfoDET)
	if TeamsVar.get() == "Golden State Warriors":
		teamInfoOutput.delete(0.0, END)
		goldenstate.teamInfoGS
		teamInfoOutput.insert(INSERT, goldenstate.teamInfoGS)
	if TeamsVar.get() == "Houston Rockets":
		teamInfoOutput.delete(0.0, END)
		houston.teamInfoHOU
		teamInfoOutput.insert(INSERT, houston.teamInfoHOU)
	if TeamsVar.get() == "Indiana Pacers":
		teamInfoOutput.delete(0.0, END)
		indiana.teamInfoIND
		teamInfoOutput.insert(INSERT, indiana.teamInfoIND)
	if TeamsVar.get() == "Los Angeles Clippers":
		teamInfoOutput.delete(0.0, END)
		losangelesC.teamInfoLAC
		teamInfoOutput.insert(INSERT, losangelesC.teamInfoLAC)
	if TeamsVar.get() == "Los Angeles Lakers":
		teamInfoOutput.delete(0.0, END)
		losangelesL.teamInfoLAL
		teamInfoOutput.insert(INSERT, losangelesL.teamInfoLAL)
	if TeamsVar.get() == "Memphis Grizzlies":
		teamInfoOutput.delete(0.0, END)
		memphis.teamInfoMEM
		teamInfoOutput.insert(INSERT, memphis.teamInfoMEM)
	if TeamsVar.get() == "Miami Heat":
		teamInfoOutput.delete(0.0, END)
		miami.teamInfoMIA
		teamInfoOutput.insert(INSERT, miami.teamInfoMIA)
	if TeamsVar.get() == "Milwaukee Bucks":
		teamInfoOutput.delete(0.0, END)
		teamInfoOutput.insert(INSERT, milwaukee.teamInfoMIL)
	if TeamsVar.get() == "Minnesota Timberwolves":
		teamInfoOutput.delete(0.0, END)
		teamInfoOutput.insert(INSERT, minnesota.teamInfoMIN)
	if TeamsVar.get() == "New Orleans Pelicans":
		teamInfoOutput.delete(0.0, END)
		teamInfoOutput.insert(INSERT, neworleans.teamInfoNOP)
	if TeamsVar.get() == "New York Knicks":
		teamInfoOutput.delete(0.0, END)
		teamInfoOutput.insert(INSERT, newyork.teamInfoNYK)
	if TeamsVar.get() == "Oklahoma City Thunder":
		teamInfoOutput.delete(0.0, END)
		teamInfoOutput.insert(INSERT, oklahoma.teamInfoOKC)

TeamsVar.trace("w", callTeamInfo)

# CALL LAST GAME
def callLastGame(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		lastGameOutput.delete(0.0, END)
		atlanta.hawksGame 
		lastGameOutput.insert(INSERT, atlanta.hawksGame)
	if TeamsVar.get() == "Boston Celtics":
		lastGameOutput.delete(0.0, END)
		boston.celticsGame 
		lastGameOutput.insert(INSERT, boston.celticsGame)
	if TeamsVar.get() == "Brooklyn Nets":
		lastGameOutput.delete(0.0, END)
		brooklyn.netsGame 
		lastGameOutput.insert(INSERT, brooklyn.netsGame)
	if TeamsVar.get() == "Charlotte Hornets":
		lastGameOutput.delete(0.0, END)
		charlotte.hornetsGame 
		lastGameOutput.insert(INSERT, charlotte.hornetsGame)
	if TeamsVar.get() == "Chicago Bulls":
		lastGameOutput.delete(0.0, END)
		chicago.bullsGame
		lastGameOutput.insert(INSERT, chicago.bullsGame)
	if TeamsVar.get() == "Cleveland Cavaliers":
		lastGameOutput.delete(0.0, END)
		cleveland.cavsGame
		lastGameOutput.insert(INSERT, cleveland.cavsGame)
	if TeamsVar.get() == "Dallas Mavericks":
		lastGameOutput.delete(0.0, END)
		dallas.mavsGame 
		lastGameOutput.insert(INSERT, dallas.mavsGame)
	if TeamsVar.get() == "Denver Nuggets":
		lastGameOutput.delete(0.0, END)
		denver.nuggetsGame 
		lastGameOutput.insert(INSERT, denver.nuggetsGame)
	if TeamsVar.get() == "Detroit Pistons":
		lastGameOutput.delete(0.0, END)
		detroit.pistonsGame 
		lastGameOutput.insert(INSERT, detroit.pistonsGame)
	if TeamsVar.get() == "Golden State Warriors":
		lastGameOutput.delete(0.0, END)
		goldenstate.warriorsGame 
		lastGameOutput.insert(INSERT, goldenstate.warriorsGame)
	if TeamsVar.get() == "Houston Rockets":
		lastGameOutput.delete(0.0, END)
		houston.rocketsGame 
		lastGameOutput.insert(INSERT, houston.rocketsGame)
	if TeamsVar.get() == "Indiana Pacers":
		lastGameOutput.delete(0.0, END)
		indiana.pacersGame
		lastGameOutput.insert(INSERT, indiana.pacersGame)
	if TeamsVar.get() == "Los Angeles Clippers":
		lastGameOutput.delete(0.0, END)
		losangelesC.clippersGame 
		lastGameOutput.insert(INSERT, losangelesC.clippersGame)
	if TeamsVar.get() == "Los Angeles Lakers":
		lastGameOutput.delete(0.0, END)
		losangelesL.lakersGame 
		lastGameOutput.insert(INSERT, losangelesL.lakersGame)
	if TeamsVar.get() == "Memphis Grizzlies":
		lastGameOutput.delete(0.0, END)
		memphis.grizzGame 
		lastGameOutput.insert(INSERT, memphis.grizzGame)
	if TeamsVar.get() == "Miami Heat":
		lastGameOutput.delete(0.0, END)
		miami.heatGame
		lastGameOutput.insert(INSERT, miami.heatGame)
	if TeamsVar.get() == "Milwaukee Bucks":
		lastGameOutput.delete(0.0, END)
		milwaukee.bucksGame
		lastGameOutput.insert(INSERT, milwaukee.bucksGame)
	if TeamsVar.get() == "Minnesota Timberwolves":
		lastGameOutput.delete(0.0, END)
		lastGameOutput.insert(INSERT, minnesota.twolvesGame)
	if TeamsVar.get() == "New Orleans Pelicans":
		lastGameOutput.delete(0.0, END)
		lastGameOutput.insert(INSERT, neworleans.pelicansGame)
	if TeamsVar.get() == "New York Knicks":
		lastGameOutput.delete(0.0, END)
		lastGameOutput.insert(INSERT, newyork.knicksGame)
	if TeamsVar.get() == "Oklahoma City Thunder":
		lastGameOutput.delete(0.0, END)
		lastGameOutput.insert(INSERT, oklahoma.thunderGame)

TeamsVar.trace("w", callLastGame)

# WIN or LOSS
def callWinLoss(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		outcomeOutput.delete(0.0, END)
		hawksStanding = atlanta.win() 
		outcomeOutput.insert(INSERT, hawksStanding)
	if TeamsVar.get() == "Boston Celtics":
		outcomeOutput.delete(0.0, END)
		celticsStanding = boston.win()
		outcomeOutput.insert(INSERT, celticsStanding)
	if TeamsVar.get() == "Brooklyn Nets":
		outcomeOutput.delete(0.0, END)
		netsStanding = brooklyn.win()
		outcomeOutput.insert(INSERT, netsStanding)
	if TeamsVar.get() == "Charlotte Hornets":
		outcomeOutput.delete(0.0, END)
		hornetsStanding = charlotte.win()
		outcomeOutput.insert(INSERT, hornetsStanding)
	if TeamsVar.get() == "Chicago Bulls":
		outcomeOutput.delete(0.0, END)
		bullsStanding = chicago.win()
		outcomeOutput.insert(INSERT, bullsStanding)
	if TeamsVar.get() == "Cleveland Cavaliers":
		outcomeOutput.delete(0.0, END)
		cavsStanding = cleveland.win()
		outcomeOutput.insert(INSERT, cavsStanding)
	if TeamsVar.get() == "Dallas Mavericks":
		outcomeOutput.delete(0.0, END)
		mavsStanding = dallas.win()
		outcomeOutput.insert(INSERT, mavsStanding)
	if TeamsVar.get() == "Denver Nuggets":
		outcomeOutput.delete(0.0, END)
		nuggetsStanding = denver.win()
		outcomeOutput.insert(INSERT, nuggetsStanding)
	if TeamsVar.get() == "Detroit Pistons":
		outcomeOutput.delete(0.0, END)
		pistonsStanding = detroit.win()
		outcomeOutput.insert(INSERT, pistonsStanding)
	if TeamsVar.get() == "Golden State Warriors":
		outcomeOutput.delete(0.0, END)
		warriorsStanding = goldenstate.win()
		outcomeOutput.insert(INSERT, warriorsStanding)
	if TeamsVar.get() == "Houston Rockets":
		outcomeOutput.delete(0.0, END)
		rocketsStanding = houston.win()
		outcomeOutput.insert(INSERT, rocketsStanding)
	if TeamsVar.get() == "Indiana Pacers":
		outcomeOutput.delete(0.0, END)
		pacersStanding = indiana.win()
		outcomeOutput.insert(INSERT, pacersStanding)
	if TeamsVar.get() == "Los Angeles Clippers":
		outcomeOutput.delete(0.0, END) 
		outcomeOutput.insert(INSERT, losangelesC.win())
	if TeamsVar.get() == "Los Angeles Lakers":
		outcomeOutput.delete(0.0, END) 
		outcomeOutput.insert(INSERT, losangelesL.win())
	if TeamsVar.get() == "Memphis Grizzlies":
		outcomeOutput.delete(0.0, END) 
		outcomeOutput.insert(INSERT, memphis.win())
	if TeamsVar.get() == "Miami Heat":
		outcomeOutput.delete(0.0, END)
		outcomeOutput.insert(INSERT, miami.win())
	if TeamsVar.get() == "Milwaukee Bucks":
		outcomeOutput.delete(0.0, END)
		outcomeOutput.insert(INSERT, milwaukee.win())
	if TeamsVar.get() == "Minnesota Timberwolves":
		outcomeOutput.delete(0.0, END)
		outcomeOutput.insert(INSERT, minnesota.win())
	if TeamsVar.get() == "New Orleans Pelicans":
		outcomeOutput.delete(0.0, END)
		outcomeOutput.insert(INSERT, neworleans.win())
	if TeamsVar.get() == "New York Knicks":
		outcomeOutput.delete(0.0, END)
		outcomeOutput.insert(INSERT, newyork.win())
	if TeamsVar.get() == "Oklahoma City Thunder":
		outcomeOutput.delete(0.0, END)
		outcomeOutput.insert(INSERT, oklahoma.win())

TeamsVar.trace("w", callWinLoss)

# CALL NEXT OPPONENT
def callNextOpp(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, atlanta.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, atlanta.nextGameOpp)

	if TeamsVar.get() == "Boston Celtics":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, boston.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, boston.nextGameOpp)
	
	if TeamsVar.get() == "Brooklyn Nets":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, brooklyn.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, brooklyn.nextGameOpp)

	if TeamsVar.get() == "Charlotte Hornets":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, charlotte.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, charlotte.nextGameOpp)

	if TeamsVar.get() == "Chicago Bulls":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, chicago.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, chicago.nextGameOppCHI)

	if TeamsVar.get() == "Cleveland Cavaliers":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, cleveland.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, cleveland.nextGameOpp)

	if TeamsVar.get() == "Dallas Mavericks":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, dallas.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, dallas.nextGameOpp)

	if TeamsVar.get() == "Denver Nuggets":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, denver.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, denver.nextGameOpp)

	if TeamsVar.get() == "Detroit Pistons":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, detroit.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, detroit.nextGameOpp)

	if TeamsVar.get() == "Golden State Warriors":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, goldenstate.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, goldenstate.nextGameOpp)

	if TeamsVar.get() == "Houston Rockets":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, houston.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, houston.nextGameOpp)

	if TeamsVar.get() == "Indiana Pacers":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, indiana.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, indiana.nextGameOpp)

	if TeamsVar.get() == "Los Angeles Clippers":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, losangelesC.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, losangelesC.nextGameOpp)

	if TeamsVar.get() == "Los Angeles Lakers":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, losangelesL.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, losangelesL.nextGameOpp)

	if TeamsVar.get() == "Memphis Grizzlies":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, memphis.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, memphis.nextGameOpp)

	if TeamsVar.get() == "Miami Heat":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, miami.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, miami.nextGameOpp)

	if TeamsVar.get() == "Milwaukee Bucks":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, milwaukee.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, milwaukee.nextGameOpp)

	if TeamsVar.get() == "Minnesota Timberwolves":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, minnesota.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, minnesota.nextGameOpp)

	if TeamsVar.get() == "New Orleans Pelicans":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, neworleans.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, neworleans.nextGameOpp)

	if TeamsVar.get() == "New York Knicks":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, newyork.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, newyork.nextGameOpp)

	if TeamsVar.get() == "Oklahoma City Thunder":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, oklahoma.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, oklahoma.nextGameOpp)

TeamsVar.trace("w", callNextOpp)


# CALL NEXT LOCATION
def callNextLoc(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, atlanta.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, atlanta.nextGameLoc)

	if TeamsVar.get() == "Boston Celtics":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, boston.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, boston.nextGameLoc)

	if TeamsVar.get() == "Brooklyn Nets":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, brooklyn.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, brooklyn.nextGameLoc)

	if TeamsVar.get() == "Charlotte Hornets":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, charlotte.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, charlotte.nextGameLoc)

	if TeamsVar.get() == "Chicago Bulls":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, chicago.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, chicago.nextGameLoc)

	if TeamsVar.get() == "Cleveland Cavaliers":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, cleveland.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, cleveland.nextGameLoc)

	if TeamsVar.get() == "Dallas Mavericks":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, dallas.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, dallas.nextGameLoc)

	if TeamsVar.get() == "Denver Nuggets":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, denver.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, denver.nextGameLoc)

	if TeamsVar.get() == "Detroit Pistons":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, detroit.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, detroit.nextGameLoc)

	if TeamsVar.get() == "Golden State Warriors":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, goldenstate.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, goldenstate.nextGameLoc)

	if TeamsVar.get() == "Houston Rockets":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, houston.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, houston.nextGameLoc)

	if TeamsVar.get() == "Indiana Pacers":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, indiana.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, indiana.nextGameLoc)

	if TeamsVar.get() == "Los Angeles Clippers":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, losangelesC.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, losangelesC.nextGameLoc)


	if TeamsVar.get() == "Los Angeles Lakers":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, losangelesL.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, losangelesL.nextGameLoc)

	if TeamsVar.get() == "Memphis Grizzlies":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, memphis.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, memphis.nextGameLoc)

	if TeamsVar.get() == "Miami Heat":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, miami.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, miami.nextGameLoc)

	if TeamsVar.get() == "Milwaukee Bucks":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, milwaukee.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, milwaukee.nextGameLoc)

	if TeamsVar.get() == "Minnesota Timberwolves":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, minnesota.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, minnesota.nextGameLoc)

	if TeamsVar.get() == "New Orleans Pelicans":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, neworleans.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, neworleans.nextGameLoc)

	if TeamsVar.get() == "New York Knicks":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, newyork.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, newyork.nextGameLoc)

	if TeamsVar.get() == "Oklahoma City Thunder":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, oklahoma.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, oklahoma.nextGameLoc)



TeamsVar.trace("w", callNextLoc)


# CALL NEXT DATE
def callNextDate(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, atlanta.nextOppDateATL)
	if TeamsVar.get() == "Boston Celtics":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, boston.nextOppDateBOS)
	if TeamsVar.get() == "Brooklyn Nets":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, brooklyn.nextOppDateBKN)
	if TeamsVar.get() == "Charlotte Hornets":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, charlotte.nextOppDateCHA)
	if TeamsVar.get() == "Chicago Bulls":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, chicago.nextOppDateCHI)
	if TeamsVar.get() == "Cleveland Cavaliers":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, cleveland.nextOppDateCLE)
	if TeamsVar.get() == "Dallas Mavericks":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, dallas.nextOppDateDAL)
	if TeamsVar.get() == "Detroit Pistons":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, detroit.nextOppDateDET)
	if TeamsVar.get() == "Golden State Warriors":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, goldenstate.nextOppDateGS)
	if TeamsVar.get() == "Houston Rockets":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, houston.nextOppDateHOU)
	if TeamsVar.get() == "Indiana Pacers":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, indiana.nextOppDateIND)
	if TeamsVar.get() == "Los Angeles Clippers":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, losangelesC.nextOppDateLAC)
	if TeamsVar.get() == "Los Angeles Lakers":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, losangelesL.nextOppDateLAL)
	if TeamsVar.get() == "Memphis Grizzlies":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, memphis.nextOppDateMEM)
	if TeamsVar.get() == "Miami Heat":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, miami.nextOppDateMIA)
	if TeamsVar.get() == "Milwaukee Bucks":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, milwaukee.nextOppDateMIL)
	if TeamsVar.get() == "Minnesota Timberwolves":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, minnesota.nextOppDateMIN)
	if TeamsVar.get() == "New Orleans Pelicans":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, neworleans.nextOppDateNOP)
	if TeamsVar.get() == "New York Knicks":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, newyork.nextOppDateNYK)
	if TeamsVar.get() == "Oklahoma City Thunder":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, oklahoma.nextOppDateOKC)

TeamsVar.trace("w", callNextDate)

# CALL TEAM LOGO
def callTeamLogo(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		LogoCanvas.delete("all")  # Deletes previous
		hawksLogo = PhotoImage(file="logos/Hawks300.png") # Creates the actual image
		LogoCanvas.image = hawksLogo  # Associates image with the canvas
		LogoCanvas.create_image(0, 0, anchor='nw', image=hawksLogo) # Creates the appearance of the image upon selection of StringVar with .trace 
	if TeamsVar.get() == "Boston Celtics":
		LogoCanvas.delete("all")
		celticsLogo = PhotoImage(file="logos/Celtics300.png")
		LogoCanvas.image = celticsLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=celticsLogo)
	if TeamsVar.get() == "Brooklyn Nets":
		LogoCanvas.delete("all")
		netsLogo = PhotoImage(file="logos/Nets300.png")
		LogoCanvas.image = netsLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=netsLogo)
	if TeamsVar.get() == "Charlotte Hornets":
		LogoCanvas.delete("all")
		hornetsLogo = PhotoImage(file="logos/Hornets300.png")
		LogoCanvas.image = hornetsLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=hornetsLogo)
	if TeamsVar.get() == "Chicago Bulls":
		LogoCanvas.delete("all")
		bullsLogo = PhotoImage(file="logos/Bulls300.png")
		LogoCanvas.image = bullsLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=bullsLogo)
	if TeamsVar.get() == "Cleveland Cavaliers":
		LogoCanvas.delete("all")
		cavsLogo = PhotoImage(file="logos/Cavs300.png")
		LogoCanvas.image = cavsLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=cavsLogo)
	if TeamsVar.get() == "Dallas Mavericks":
		LogoCanvas.delete("all")
		mavsLogo = PhotoImage(file="logos/Mavs300.png")
		LogoCanvas.image = mavsLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=mavsLogo)
	if TeamsVar.get() == "Denver Nuggets":
		LogoCanvas.delete("all")
		nuggetsLogo = PhotoImage(file="logos/Nuggets300.png")
		LogoCanvas.image = nuggetsLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=nuggetsLogo)
	if TeamsVar.get() == "Detroit Pistons":
		LogoCanvas.delete("all")
		pistonsLogo = PhotoImage(file="logos/Pistons300.png")
		LogoCanvas.image = pistonsLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=pistonsLogo)
	if TeamsVar.get() == "Golden State Warriors":
		LogoCanvas.delete("all")
		warriorsLogo = PhotoImage(file="logos/Warriors300.png")
		LogoCanvas.image = warriorsLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=warriorsLogo)
	if TeamsVar.get() == "Houston Rockets":
		LogoCanvas.delete("all")
		rocketsLogo = PhotoImage(file="logos/Rockets300.png")
		LogoCanvas.image = rocketsLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=rocketsLogo)
	if TeamsVar.get() == "Indiana Pacers":
		LogoCanvas.delete("all")
		pacersLogo = PhotoImage(file="logos/Pacers300.png")
		LogoCanvas.image = pacersLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=pacersLogo)
	if TeamsVar.get() == "Los Angeles Clippers":
		LogoCanvas.delete("all")
		clippersLogo = PhotoImage(file="logos/Clippers300.png")
		LogoCanvas.image = clippersLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=clippersLogo)
	if TeamsVar.get() == "Los Angeles Lakers":
		LogoCanvas.delete("all")
		lakersLogo = PhotoImage(file="logos/Lakers300.png")
		LogoCanvas.image =lakersLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=lakersLogo)
	if TeamsVar.get() == "Memphis Grizzlies":
		LogoCanvas.delete("all")
		grizzliesLogo = PhotoImage(file="logos/Grizzlies300.png")
		LogoCanvas.image = grizzliesLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=grizzliesLogo)
	if TeamsVar.get() == "Miami Heat":
		LogoCanvas.delete("all")
		heatLogo = PhotoImage(file="logos/Heat300.png")
		LogoCanvas.image = heatLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=heatLogo)
	if TeamsVar.get() == "Milwaukee Bucks":
		LogoCanvas.delete("all")
		bucksLogo = PhotoImage(file="logos/Bucks300.png")
		LogoCanvas.image = bucksLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=bucksLogo)
	if TeamsVar.get() == "Minnesota Timberwolves":
		LogoCanvas.delete("all")
		twolvesLogo = PhotoImage(file="logos/Twolves300.png")
		LogoCanvas.image = twolvesLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=twolvesLogo)
	if TeamsVar.get() == "New Orleans Pelicans":
		LogoCanvas.delete("all")
		pelicansLogo = PhotoImage(file="logos/Pelicans100.png")
		LogoCanvas.image = pelicansLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=pelicansLogo)
	if TeamsVar.get() == "New York Knicks":
		LogoCanvas.delete("all")
		knicksLogo = PhotoImage(file="logos/Knicks300.png")
		LogoCanvas.image = knicksLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=knicksLogo)
	if TeamsVar.get() == "Oklahoma City Thunder":
		LogoCanvas.delete("all")
		thunderLogo = PhotoImage(file="logos/Thunder300.png")
		LogoCanvas.image = thunderLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=thunderLogo)


TeamsVar.trace("w", callTeamLogo)


def callLabelCanvas(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Boston Celtics":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Brooklyn Nets":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Brooklyn Nets":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Charlotte Hornets":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Chicago Bulls":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Cleveland Cavaliers":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Dallas Mavericks":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Denver Nuggets":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Detroit Pistons":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Golden State Warriors":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Houston Rockets":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Indiana Pacers":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Los Angeles Clippers":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Los Angeles Lakers":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Memphis Grizzlies":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Miami Heat":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Milwaukee Bucks":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Minnesota Timberwolves":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "New Orleans Pelicans":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "New York Knicks":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Oklahoma City Thunder":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")

TeamsVar.trace("w", callLabelCanvas)


window.mainloop()




