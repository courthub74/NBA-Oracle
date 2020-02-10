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
droplist.config(width=45, height=1, fg="Darkblue")
droplist.grid(row=1,column=1,sticky=W)

# TEAM SELECTED
teamSelected = Label(window, text="Team Selected:", bg="Darkblue", fg="White")
teamSelected.grid(row=2,column=0)
teamSelectedOutput = Text(window, width=40, height=1, bg="Black", fg="White")
teamSelectedOutput.grid(row=2,column=1,sticky=W)

# YEAR FORMED
yearFormed = Label(window, text="Year Formed:", bg="Darkblue", fg="White")
yearFormed.grid(row=3,column=0)
yearFormedOutput = Text(window, width=40, height=1, bg="Black", fg="White")
yearFormedOutput.grid(row=3,column=1,sticky=W)

# TEAM STADIUM
teamStadium = Label(window, text="Team Stadium:", bg="Darkblue", fg="White")
teamStadium.grid(row=4,column=0)
teamStadiumOutput = Text(window, width=40, height=1, bg="Black", fg="White")
teamStadiumOutput.grid(row=4,column=1,sticky=W)

# TEAM INFO
teamInfo = Label(window, text="Team Info:", bg="Darkblue", fg="White")
teamInfo.grid(row=5,column=0)
teamInfoOutput = Text(window, width=40, height=5, wrap=WORD, bg="Black", fg="White")
teamInfoOutput.grid(row=5,column=1,sticky=W)

# LAST GAME
lastGame = Label(window, text="Last Game Played:", bg="Darkblue", fg="White")
lastGame.grid(row=6,column=0)
lastGameOutput = Text(window, width=40, height=4, bg="Black", fg="White")
lastGameOutput.grid(row=6,column=1,sticky=W)

# WIN LOSS / STREAK
outcome = Label(window, text="Win/Loss", bg="Darkblue", fg="White")
outcome.grid(row=7,column=0)
outcomeOutput = Text(window, width=40, height=1, bg="Black", fg="White")
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
		selectATL = atlanta.hawksTeam
		teamSelectedOutput.insert(INSERT, selectATL)
	if TeamsVar.get() == "Boston Celtics":
		teamSelectedOutput.delete(0.0, END)
		selectBOS = boston.celticsTeam
		teamSelectedOutput.insert(INSERT, selectBOS)
	if TeamsVar.get() == "Brooklyn Nets":
		teamSelectedOutput.delete(0.0, END)
		selectBKN = brooklyn.netsTeam
		teamSelectedOutput.insert(INSERT, selectBKN)
	if TeamsVar.get() == "Charlotte Hornets":
		teamSelectedOutput.delete(0.0, END)
		selectCHA = charlotte.hornetsTeam
		teamSelectedOutput.insert(INSERT, selectCHA)
	if TeamsVar.get() == "Chicago Bulls":
		teamSelectedOutput.delete(0.0, END)
		selectCHI = chicago.bullsTeam
		teamSelectedOutput.insert(INSERT, selectCHI)
	if TeamsVar.get() == "Cleveland Cavaliers":
		teamSelectedOutput.delete(0.0, END)
		selectCLE = cleveland.cavsTeam
		teamSelectedOutput.insert(INSERT, selectCLE)
	if TeamsVar.get() == "Dallas Mavericks":
		teamSelectedOutput.delete(0.0, END)
		selectDAL = dallas.mavsTeam
		teamSelectedOutput.insert(INSERT, selectDAL)
	if TeamsVar.get() == "Denver Nuggets":
		teamSelectedOutput.delete(0.0, END)
		selectDEN = denver.nuggetsTeam  # Locate the imported file and then the variable that is the parsed string you are looking for
		teamSelectedOutput.insert(INSERT, selectDEN) # NOW insert it into the field
	if TeamsVar.get() == "Detroit Pistons":
		teamSelectedOutput.delete(0.0, END)
		selectDET = detroit.pistonsTeam  
		teamSelectedOutput.insert(INSERT, selectDET)

TeamsVar.trace("w", callTeamSelected)

# CALL YEAR FORMED
def callYearFormed(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		yearFormedOutput.delete(0.0, END)
		yearATL = atlanta.yearFormedATL
		yearFormedOutput.insert(INSERT, yearATL)
	if TeamsVar.get() == "Boston Celtics":
		yearFormedOutput.delete(0.0, END)
		yearBOS = boston.yearFormedBOS
		yearFormedOutput.insert(INSERT, yearBOS)
	if TeamsVar.get() == "Brooklyn Nets":
		yearFormedOutput.delete(0.0, END)
		yearBKN = brooklyn.yearFormedBKN
		yearFormedOutput.insert(INSERT, yearBKN)
	if TeamsVar.get() == "Charlotte Hornets":
		yearFormedOutput.delete(0.0, END)
		yearCHA = charlotte.yearFormedCHA
		yearFormedOutput.insert(INSERT, yearCHA)
	if TeamsVar.get() == "Chicago Bulls":
		yearFormedOutput.delete(0.0, END)
		yearCHI = chicago.yearFormedCHI
		yearFormedOutput.insert(INSERT, yearCHI)
	if TeamsVar.get() == "Cleveland Cavaliers":
		yearFormedOutput.delete(0.0, END)
		yearCLE = cleveland.yearFormedCLE
		yearFormedOutput.insert(INSERT, yearCLE)
	if TeamsVar.get() == "Dallas Mavericks":
		yearFormedOutput.delete(0.0, END)
		yearDAL = dallas.yearFormedDAL
		yearFormedOutput.insert(INSERT, yearDAL)
	if TeamsVar.get() == "Denver Nuggets":
		yearFormedOutput.delete(0.0, END)
		yearDEN = denver.yearFormedDEN
		yearFormedOutput.insert(INSERT, yearDEN)
	if TeamsVar.get() == "Detroit Pistons":
		yearFormedOutput.delete(0.0, END)
		yearDET = detroit.yearFormedDET
		yearFormedOutput.insert(INSERT, yearDET)

TeamsVar.trace("w", callYearFormed)


# CALL TEAM STADIUM
def callTeamStadium(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		teamStadiumOutput.delete(0.0, END)
		stadiumATL = atlanta.teamStadiumATL
		teamStadiumOutput.insert(INSERT, stadiumATL)
	if TeamsVar.get() == "Boston Celtics":
		teamStadiumOutput.delete(0.0, END)
		stadiumBOS = boston.teamStadiumBOS
		teamStadiumOutput.insert(INSERT, stadiumBOS)
	if TeamsVar.get() == "Brooklyn Nets":
		teamStadiumOutput.delete(0.0, END)
		stadiumBKN = brooklyn.teamStadiumBKN
		teamStadiumOutput.insert(INSERT, stadiumBKN)
	if TeamsVar.get() == "Charlotte Hornets":
		teamStadiumOutput.delete(0.0, END)
		stadiumCHA = charlotte.teamStadiumCHA
		teamStadiumOutput.insert(INSERT, stadiumCHA)
	if TeamsVar.get() == "Chicago Bulls": 
		teamStadiumOutput.delete(0.0, END)
		stadiumCHI = chicago.teamStadiumCHI
		teamStadiumOutput.insert(INSERT, stadiumCHI)
	if TeamsVar.get() == "Cleveland Cavaliers": 
		teamStadiumOutput.delete(0.0, END)
		stadiumCLE = cleveland.teamStadiumCLE
		teamStadiumOutput.insert(INSERT, stadiumCLE)
	if TeamsVar.get() == "Dallas Mavericks":
		teamStadiumOutput.delete(0.0, END)
		stadiumDAL = dallas.teamStadiumDAL
		teamStadiumOutput.insert(INSERT, stadiumDAL)
	if TeamsVar.get() == "Denver Nuggets":
		teamStadiumOutput.delete(0.0, END)
		stadiumDEN = denver.teamStadiumDEN
		teamStadiumOutput.insert(INSERT, stadiumDEN)
	if TeamsVar.get() == "Detroit Pistons":
		teamStadiumOutput.delete(0.0, END)
		stadiumDET = detroit.teamStadiumDET
		teamStadiumOutput.insert(INSERT, stadiumDET)
			
TeamsVar.trace("w", callTeamStadium)

# CALL TEAM INFO
def callTeamInfo(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		teamInfoOutput.delete(0.0, END)
		infoATL = atlanta.teamInfoATL
		teamInfoOutput.insert(INSERT, infoATL)
	if TeamsVar.get() == "Boston Celtics":
		teamInfoOutput.delete(0.0, END)
		infoBOS = boston.teamInfoBOS
		teamInfoOutput.insert(INSERT, infoBOS)
	if TeamsVar.get() == "Brooklyn Nets":
		teamInfoOutput.delete(0.0, END)
		infoBKN = brooklyn.teamInfoBKN
		teamInfoOutput.insert(INSERT, infoBKN)
	if TeamsVar.get() == "Charlotte Hornets":
		teamInfoOutput.delete(0.0, END)
		infoCHA = charlotte.teamInfoCHA
		teamInfoOutput.insert(INSERT, infoCHA)
	if TeamsVar.get() == "Chicago Bulls":
		teamInfoOutput.delete(0.0, END)
		infoCHI = chicago.teamInfoCHI
		teamInfoOutput.insert(INSERT, infoCHI)
	if TeamsVar.get() == "Cleveland Cavaliers":
		teamInfoOutput.delete(0.0, END)
		infoCLE = cleveland.teamInfoCLE
		teamInfoOutput.insert(INSERT, infoCLE)
	if TeamsVar.get() == "Dallas Mavericks":
		teamInfoOutput.delete(0.0, END)
		infoDAL = dallas.teamInfoDAL
		teamInfoOutput.insert(INSERT, infoDAL)
	if TeamsVar.get() == "Denver Nuggets":
		teamInfoOutput.delete(0.0, END)
		infoDEN = denver.teamInfoDEN
		teamInfoOutput.insert(INSERT, infoDEN)
	if TeamsVar.get() == "Detroit Pistons":
		teamInfoOutput.delete(0.0, END)
		infoDET = detroit.teamInfoDET
		teamInfoOutput.insert(INSERT, infoDET)

TeamsVar.trace("w", callTeamInfo)

# CALL LAST GAME
def callLastGame(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		lastGameOutput.delete(0.0, END)
		hawksLastGame = atlanta.hawksGame 
		lastGameOutput.insert(INSERT, hawksLastGame)
	if TeamsVar.get() == "Boston Celtics":
		lastGameOutput.delete(0.0, END)
		celticsLastGame = boston.celticsGame 
		lastGameOutput.insert(INSERT, celticsLastGame)
	if TeamsVar.get() == "Brooklyn Nets":
		lastGameOutput.delete(0.0, END)
		netsLastGame = brooklyn.netsGame 
		lastGameOutput.insert(INSERT, netsLastGame)
	if TeamsVar.get() == "Charlotte Hornets":
		lastGameOutput.delete(0.0, END)
		hornetsLastGame = charlotte.hornetsGame 
		lastGameOutput.insert(INSERT, hornetsLastGame)
	if TeamsVar.get() == "Chicago Bulls":
		lastGameOutput.delete(0.0, END)
		bullsLastGame = chicago.bullsGame
		lastGameOutput.insert(INSERT,bullsLastGame)
	if TeamsVar.get() == "Cleveland Cavaliers":
		lastGameOutput.delete(0.0, END)
		cavsLastGame = cleveland.cavsGame
		lastGameOutput.insert(INSERT,cavsLastGame)
	if TeamsVar.get() == "Dallas Mavericks":
		lastGameOutput.delete(0.0, END)
		mavsLastGame = dallas.mavsGame 
		lastGameOutput.insert(INSERT, mavsLastGame)
	if TeamsVar.get() == "Denver Nuggets":
		lastGameOutput.delete(0.0, END)
		nuggetsLastGame = denver.nuggetsGame 
		lastGameOutput.insert(INSERT, nuggetsLastGame)
	if TeamsVar.get() == "Detroit Pistons":
		lastGameOutput.delete(0.0, END)
		pistonsLastGame = detroit.pistonsGame 
		lastGameOutput.insert(INSERT, pistonsLastGame)

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


TeamsVar.trace("w", callWinLoss)

# CALL TEAM LOGO
def callTeamLogo(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		LogoCanvas.delete("all")  # Deletes previous
		hawksLogo = PhotoImage(file="logos/Hawks300.png") # Creates the actual image
		LogoCanvas.image = hawksLogo  # Associates image with the canvas
		LogoCanvas.create_image(0, 0, anchor='nw', image=hawksLogo) # Creates the appearance of the image
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


TeamsVar.trace("w", callTeamLogo)

window.mainloop()
