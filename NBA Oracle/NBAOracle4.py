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
import oklahoma
import orlando
import philadelphia
import phoenix
import portland
import sacramento

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

# # WIN STREAK
# streak = Label(window, text="Win Streak:", bg="Darkblue", fg="White", font="Helvetica 10 bold")
# streak.grid(row=14,column=0)
# streakOutput = Text(window, width=20, height=1, bg="Black", fg="White")
# streakOutput.grid(row=15,column=1,sticky=W)

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
	if TeamsVar.get() == "New Orleans Pelicans":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, neworleans.pelicansTeam)
	if TeamsVar.get() == "New York Knicks":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, newyork.knicksTeam)
	if TeamsVar.get() == "Oklahoma City Thunder":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, oklahoma.thunderTeam)
	if TeamsVar.get() == "Orlando Magic":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, orlando.magicTeam)
	if TeamsVar.get() == "Philadelphia 76ers":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, philadelphia.sixersTeam)
	if TeamsVar.get() == "Phoenix Suns":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, phoenix.sunsTeam)
	if TeamsVar.get() == "Portland Trail Blazers":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, portland.blazersTeam)
	if TeamsVar.get() == "Sacramento Kings":
		teamSelectedOutput.delete(0.0, END)
		teamSelectedOutput.insert(INSERT, sacramento.kingsTeam)

TeamsVar.trace("w", callTeamSelected)


# CALL YEAR FORMED
def callYearFormed(*args):
	if TeamsVar.get() == "New Orleans Pelicans":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, neworleans.yearFormedNOP)
	if TeamsVar.get() == "New York Knicks":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, newyork.yearFormedNYK)
	if TeamsVar.get() == "Oklahoma City Thunder":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, oklahoma.yearFormedOKC)
	if TeamsVar.get() == "Orlando Magic":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, orlando.yearFormedORL)
	if TeamsVar.get() == "Philadelphia 76ers":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, philadelphia.yearFormedPHI)
	if TeamsVar.get() == "Phoenix Suns":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, phoenix.yearFormedPHO)
	if TeamsVar.get() == "Portland Trail Blazers":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, portland.yearFormedPOR)
	if TeamsVar.get() == "Sacramento Kings":
		yearFormedOutput.delete(0.0, END)
		yearFormedOutput.insert(INSERT, sacramento.yearFormedSAC)

TeamsVar.trace("w", callYearFormed)


# CALL TEAM STADIUM
def callTeamStadium(*args):
	if TeamsVar.get() == "New Orleans Pelicans":
		teamStadiumOutput.delete(0.0, END)
		teamStadiumOutput.insert(INSERT, neworleans.teamStadiumNOP)
	if TeamsVar.get() == "New York Knicks":
		teamStadiumOutput.delete(0.0, END)
		teamStadiumOutput.insert(INSERT, newyork.teamStadiumNYK)
	if TeamsVar.get() == "Oklahoma City Thunder":
		teamStadiumOutput.delete(0.0, END)
		teamStadiumOutput.insert(INSERT, oklahoma.teamStadiumOKC)
	if TeamsVar.get() == "Orlando Magic":
		teamStadiumOutput.delete(0.0, END)
		teamStadiumOutput.insert(INSERT, orlando.teamStadiumORL)
	if TeamsVar.get() == "Philadelphia 76ers":
		teamStadiumOutput.delete(0.0, END)
		teamStadiumOutput.insert(INSERT, philadelphia.teamStadiumPHI)
	if TeamsVar.get() == "Phoenix Suns":
		teamStadiumOutput.delete(0.0, END)
		teamStadiumOutput.insert(INSERT, phoenix.teamStadiumPHO)
	if TeamsVar.get() == "Portland Trail Blazers":
		teamStadiumOutput.delete(0.0, END)
		teamStadiumOutput.insert(INSERT, portland.teamStadiumPOR)
	if TeamsVar.get() == "Sacramento Kings":
		teamStadiumOutput.delete(0.0, END)
		teamStadiumOutput.insert(INSERT, sacramento.teamStadiumSAC)

TeamsVar.trace("w", callTeamStadium)


# CALL TEAM INFO
def callTeamInfo(*args):
	if TeamsVar.get() == "New Orleans Pelicans":
		teamInfoOutput.delete(0.0, END)
		teamInfoOutput.insert(INSERT, neworleans.teamInfoNOP)
	if TeamsVar.get() == "New York Knicks":
		teamInfoOutput.delete(0.0, END)
		teamInfoOutput.insert(INSERT, newyork.teamInfoNYK)
	if TeamsVar.get() == "Oklahoma City Thunder":
		teamInfoOutput.delete(0.0, END)
		teamInfoOutput.insert(INSERT, oklahoma.teamInfoOKC)
	if TeamsVar.get() == "Orlando Magic":
		teamInfoOutput.delete(0.0, END)
		teamInfoOutput.insert(INSERT, orlando.teamInfoORL)
	if TeamsVar.get() == "Philadelphia 76ers":
		teamInfoOutput.delete(0.0, END)
		teamInfoOutput.insert(INSERT, philadelphia.teamInfoPHI)
	if TeamsVar.get() == "Phoenix Suns":
		teamInfoOutput.delete(0.0, END)
		teamInfoOutput.insert(INSERT, phoenix.teamInfoPHO)
	if TeamsVar.get() == "Portland Trail Blazers":
		teamInfoOutput.delete(0.0, END)
		teamInfoOutput.insert(INSERT, portland.teamInfoPOR)
	if TeamsVar.get() == "Sacramento Kings":
		teamInfoOutput.delete(0.0, END)
		teamInfoOutput.insert(INSERT, sacramento.teamInfoSAC)

TeamsVar.trace("w", callTeamInfo)


# CALL LAST GAME
def callLastGame(*args):
	if TeamsVar.get() == "New Orleans Pelicans":
		lastGameOutput.delete(0.0, END)
		lastGameOutput.insert(INSERT, neworleans.pelicansGame)
	if TeamsVar.get() == "New York Knicks":
		lastGameOutput.delete(0.0, END)
		lastGameOutput.insert(INSERT, newyork.knicksGame)
	if TeamsVar.get() == "Oklahoma City Thunder":
		lastGameOutput.delete(0.0, END)
		lastGameOutput.insert(INSERT, oklahoma.thunderGame)
	if TeamsVar.get() == "Orlando Magic":
		lastGameOutput.delete(0.0, END)
		lastGameOutput.insert(INSERT, orlando.magicGame)
	if TeamsVar.get() == "Philadelphia 76ers":
		lastGameOutput.delete(0.0, END)
		lastGameOutput.insert(INSERT, philadelphia.sixersGame)
	if TeamsVar.get() == "Phoenix Suns":
		lastGameOutput.delete(0.0, END)
		lastGameOutput.insert(INSERT, phoenix.sunsGame)
	if TeamsVar.get() == "Portland Trail Blazers":
		lastGameOutput.delete(0.0, END)
		lastGameOutput.insert(INSERT, portland.blazersGame)
	if TeamsVar.get() == "Sacramento Kings":
		lastGameOutput.delete(0.0, END)
		lastGameOutput.insert(INSERT, sacramento.kingsGame)

TeamsVar.trace("w", callLastGame)


# WIN or LOSS
def callWinLoss(*args):
	if TeamsVar.get() == "New Orleans Pelicans":
		outcomeOutput.delete(0.0, END)
		outcomeOutput.insert(INSERT, neworleans.win())
	if TeamsVar.get() == "New York Knicks":
		outcomeOutput.delete(0.0, END)
		outcomeOutput.insert(INSERT, newyork.win())
	if TeamsVar.get() == "Oklahoma City Thunder":
		outcomeOutput.delete(0.0, END)
		outcomeOutput.insert(INSERT, oklahoma.win())
	if TeamsVar.get() == "Orlando Magic":
		outcomeOutput.delete(0.0, END)
		outcomeOutput.insert(INSERT, orlando.win())
	if TeamsVar.get() == "Philadelphia 76ers":
		outcomeOutput.delete(0.0, END)
		outcomeOutput.insert(INSERT, philadelphia.win())
	if TeamsVar.get() == "Phoenix Suns":
		outcomeOutput.delete(0.0, END)
		outcomeOutput.insert(INSERT, phoenix.win())
	if TeamsVar.get() == "Portland Trail Blazers":
		outcomeOutput.delete(0.0, END)
		outcomeOutput.insert(INSERT, portland.win())
	if TeamsVar.get() == "Sacramento Kings":
		outcomeOutput.delete(0.0, END)
		outcomeOutput.insert(INSERT, sacramento.win())

TeamsVar.trace("w", callWinLoss)


# CALL NEXT OPPONENT
def callNextOpp(*args):
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

	if TeamsVar.get() == "Orlando Magic":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, orlando.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, orlando.nextGameOpp)

	if TeamsVar.get() == "Philadelphia 76ers":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, philadelphia.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, philadelphia.nextGameOpp)

	if TeamsVar.get() == "Phoenix Suns":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, phoenix.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, phoenix.nextGameOpp)

	if TeamsVar.get() == "Portland Trail Blazers":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, portland.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, portland.nextGameOpp)

	if TeamsVar.get() == "Sacramento Kings":
		try:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, sacramento.next())
		except:
			nextOppOutput.delete(0.0, END)
			nextOppOutput.insert(INSERT, sacramento.nextGameOpp)

TeamsVar.trace("w", callNextOpp)


# CALL NEXT LOCATION
def callNextLoc(*args):
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

	if TeamsVar.get() == "Orlando Magic":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, orlando.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, orlando.nextGameLoc)

	if TeamsVar.get() == "Philadelphia 76ers":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, philadelphia.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, philadelphia.nextGameLoc)

	if TeamsVar.get() == "Phoenix Suns":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, phoenix.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, phoenix.nextGameLoc)

	if TeamsVar.get() == "Portland Trail Blazers":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, portland.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, portland.nextGameLoc)

	if TeamsVar.get() == "Sacramento Kings":
		try:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, sacramento.where())
		except:
			locNextOutput.delete(0.0, END)
			locNextOutput.insert(INSERT, sacramento.nextGameLoc)



TeamsVar.trace("w", callNextLoc)


# CALL NEXT DATE
def callNextDate(*args):
	if TeamsVar.get() == "New Orleans Pelicans":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, neworleans.nextOppDateNOP)
	if TeamsVar.get() == "New York Knicks":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, neworleans.nextOppDateNOP)
	if TeamsVar.get() == "Oklahoma City Thunder":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, oklahoma.nextOppDateOKC)
	if TeamsVar.get() == "Orlando Magic":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, orlando.nextOppDateORL)
	if TeamsVar.get() == "Philadelphia 76ers":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, philadelphia.nextOppDatePHI)
	if TeamsVar.get() == "Phoenix Suns":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, phoenix.nextOppDatePHO)
	if TeamsVar.get() == "Portland Trail Blazers":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, portland.nextOppDatePOR)
	if TeamsVar.get() == "Sacramento Kings":
		nextDateOutput.delete(0.0, END)
		nextDateOutput.insert(INSERT, sacramento.nextOppDateSAC)

TeamsVar.trace("w", callNextDate)


# CALL TEAM LOGO
def callTeamLogo(*args):
	if TeamsVar.get() == "New Orleans Pelicans":
		LogoCanvas.delete("all")
		pelicansLogo = PhotoImage(file="logos/Pelicans300.png")
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
	if TeamsVar.get() == "Orlando Magic":
		LogoCanvas.delete("all")
		magicLogo = PhotoImage(file="logos/Magic400.png")
		LogoCanvas.image = magicLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=magicLogo)
	if TeamsVar.get() == "Philadelphia 76ers":
		LogoCanvas.delete("all")
		sixersLogo = PhotoImage(file="logos/76ers300.png")
		LogoCanvas.image = sixersLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=sixersLogo)
	if TeamsVar.get() == "Phoenix Suns":
		LogoCanvas.delete("all")
		sunsLogo = PhotoImage(file="logos/Suns300.png")
		LogoCanvas.image = sunsLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=sunsLogo)
	if TeamsVar.get() == "Portland Trail Blazers":
		LogoCanvas.delete("all")
		blazersLogo = PhotoImage(file="logos/Blazers300.png")
		LogoCanvas.image = blazersLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=blazersLogo)
	if TeamsVar.get() == "Sacramento Kings":
		LogoCanvas.delete("all")
		kingsLogo = PhotoImage(file="logos/Kings300.png")
		LogoCanvas.image = kingsLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=kingsLogo)

TeamsVar.trace("w", callTeamLogo)


# CALL LABEL CANVAS (Team Logo:)
def callLabelCanvas(*args):
	if TeamsVar.get() == "New Orleans Pelicans":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "New York Knicks":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Oklahoma City Thunder":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Orlando Magic":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Philadelphia 76ers":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Phoenix Suns":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Portland Trail Blazers":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")
	if TeamsVar.get() == "Sacramento Kings":
		LabelCanvas.delete(0.0, END)
		LabelCanvas.insert(INSERT, "Team Logo:")

TeamsVar.trace("w", callLabelCanvas)


window.mainloop()