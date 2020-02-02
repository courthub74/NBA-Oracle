from tkinter import *
import teamslist
import atl

# WINDOW
window = Tk()
window.geometry("500x800")
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
TeamsVar = StringVar() 
TeamsVar.set(teamslist.TeamsList[0])
droplist = OptionMenu(window, TeamsVar, *teamslist.TeamsList)
droplist.config(width=20, height=1, fg="Darkblue")
droplist.grid(row=1,column=1,sticky=W)

# TEAM SELECTED
teamSelected = Label(window, text="Team Selected:", bg="Darkblue", fg="White")
teamSelected.grid(row=2,column=0)
teamSelectedOutput = Text(window, width=20, height=1)
teamSelectedOutput.grid(row=2,column=1,sticky=W)

# YEAR FORMED
yearFormed = Label(window, text="Year Formed:", bg="Darkblue", fg="White")
yearFormed.grid(row=3,column=0)
yearFormedOutput = Text(window, width=20, height=1)
yearFormedOutput.grid(row=3,column=1,sticky=W)

# TEAM STADIUM
teamStadium = Label(window, text="Team Stadium:", bg="Darkblue", fg="White")
teamStadium.grid(row=4,column=0)
teamStadiumOutput = Text(window, width=20, height=1)
teamStadiumOutput.grid(row=4,column=1,sticky=W)

# TEAM INFO
teamInfo = Label(window, text="Team Info:", bg="Darkblue", fg="White")
teamInfo.grid(row=5,column=0)
teamInfoOutput = Text(window, width=40, height=5, wrap=WORD)
teamInfoOutput.grid(row=5,column=1,sticky=W)

# LAST GAME
lastGame = Label(window, text="Last Game Played:", bg="Darkblue", fg="White")
lastGame.grid(row=6,column=0)
lastGameOutput = Text(window, width=30, height=4)
lastGameOutput.grid(row=6,column=1,sticky=W)

# WIN LOSS / STREAK
outcome = Label(window, text="Win/Loss", bg="Darkblue", fg="White")
outcome.grid(row=7,column=0)
outcomeOutput = Text(window, width=20, height=1)
outcomeOutput.grid(row=7,column=1,sticky=W)

# LOGO
LogoCanvas = Canvas(height=300, width=300, borderwidth=0, highlightthickness=0, bg="Darkblue", bd=0)
LogoCanvas.grid(row=8,column=1)


# FUNCTIONALITY
#############################################################
# CALL TEAM SELECTED 
def callTeamSelected(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		teamSelectedOutput.delete(0.0, END)
		selectATL = atl.hawksTeam
		teamSelectedOutput.insert(INSERT, selectATL)

TeamsVar.trace("w", callTeamSelected)

# CALL YEAR FORMED
def callYearFormed(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		yearFormedOutput.delete(0.0, END)
		yearATL = atl.yearFormedATL
		yearFormedOutput.insert(INSERT, yearATL)

TeamsVar.trace("w", callYearFormed)

# CALL TEAM STADIUM
def callTeamStadium(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		teamStadiumOutput.delete(0.0, END)
		stadiumATL = atl.teamStadiumATL
		teamStadiumOutput.insert(INSERT, stadiumATL)

TeamsVar.trace("w", callTeamStadium)

# CALL TEAM INFO
def callTeamInfo(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		teamInfoOutput.delete(0.0, END)
		infoATL = atl.teamInfoATL
		teamInfoOutput.insert(INSERT, infoATL)

TeamsVar.trace("w", callTeamInfo)

# CALL LAST GAME
def callLastGame(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		lastGameOutput.delete(0.0, END)
		hawksLastGame = atl.hawksGame 
		lastGameOutput.insert(INSERT, hawksLastGame)

TeamsVar.trace("w", callLastGame)

# CALL TEAM LOGO
def callTeamLogo(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		LogoCanvas.delete("all")
		hawksLogo = PhotoImage(file="logos/Hawks300.png")
		LogoCanvas.image = hawksLogo
		LogoCanvas.create_image(0, 0, anchor='nw', image=hawksLogo)

TeamsVar.trace("w", callTeamLogo)

window.mainloop()
