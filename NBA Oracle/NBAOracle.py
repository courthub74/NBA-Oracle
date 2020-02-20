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

# LOGO LABEL
LabelCanvas = Canvas(height=1, width=3, borderwidth=0, highlightthickness=0, bg="Darkblue", bd=0)
LabelCanvas.grid(row=8,column=0)


# FUNCTIONALITY
#############################################################
# CALL TEAM SELECTED 
def callTeamSelected(*args):
	if TeamsVar.get() == "Atlanta Hawks":  # If StringVar matches selected Var then
		teamSelectedOutput.delete(0.0, END)  # Clear previous data from field
		atlanta.hawksTeam                     # Variable called from imported file 
		teamSelectedOutput.insert(INSERT, atlanta.hawksTeam)  # insert method to insert called variable into textfield
	if TeamsVar.get() == "Boston Celtics":
		teamSelectedOutput.delete(0.0, END)
		boston.celticsTeam
		teamSelectedOutput.insert(INSERT, boston.celticsTeam)
	if TeamsVar.get() == "Brooklyn Nets":
		teamSelectedOutput.delete(0.0, END)
		brooklyn.netsTeam
		teamSelectedOutput.insert(INSERT, brooklyn.netsTeam)
	if TeamsVar.get() == "Charlotte Hornets":
		teamSelectedOutput.delete(0.0, END)
		charlotte.hornetsTeam
		teamSelectedOutput.insert(INSERT, charlotte.hornetsTeam)
	if TeamsVar.get() == "Chicago Bulls":
		teamSelectedOutput.delete(0.0, END)
		chicago.bullsTeam
		teamSelectedOutput.insert(INSERT, chicago.bullsTeam)
	if TeamsVar.get() == "Cleveland Cavaliers":
		teamSelectedOutput.delete(0.0, END)
		cleveland.cavsTeam
		teamSelectedOutput.insert(INSERT, cleveland.cavsTeam)
	if TeamsVar.get() == "Dallas Mavericks":
		teamSelectedOutput.delete(0.0, END)
		dallas.mavsTeam
		teamSelectedOutput.insert(INSERT, dallas.mavsTeam)
	if TeamsVar.get() == "Denver Nuggets":
		teamSelectedOutput.delete(0.0, END)
		denver.nuggetsTeam  
		teamSelectedOutput.insert(INSERT, denver.nuggetsTeam) 
	if TeamsVar.get() == "Detroit Pistons":
		teamSelectedOutput.delete(0.0, END)
		detroit.pistonsTeam  
		teamSelectedOutput.insert(INSERT, detroit.pistonsTeam)
	if TeamsVar.get() == "Golden State Warriors":
		teamSelectedOutput.delete(0.0, END)
		goldenstate.warriorsTeam
		teamSelectedOutput.insert(INSERT, goldenstate.warriorsTeam)
	if TeamsVar.get() == "Houston Rockets":
		teamSelectedOutput.delete(0.0, END)
		houston.rocketsTeam
		teamSelectedOutput.insert(INSERT, houston.rocketsTeam)
	if TeamsVar.get() == "Indiana Pacers":
		teamSelectedOutput.delete(0.0, END)
		indiana.pacersTeam
		teamSelectedOutput.insert(INSERT, indiana.pacersTeam)
	if TeamsVar.get() == "Los Angeles Clippers":
		teamSelectedOutput.delete(0.0, END)
		losangelesC.clippersTeam
		teamSelectedOutput.insert(INSERT, losangelesC.clippersTeam)
	if TeamsVar.get() == "Los Angeles Lakers":
		teamSelectedOutput.delete(0.0, END)
		losangelesL.lakersTeam
		teamSelectedOutput.insert(INSERT, losangelesL.lakersTeam)
	if TeamsVar.get() == "Memphis Grizzlies":
		teamSelectedOutput.delete(0.0, END)
		memphis.grizzTeam
		teamSelectedOutput.insert(INSERT, memphis.grizzTeam)


TeamsVar.trace("w", callTeamSelected) #TeamsVar a TRACE variable I directly called the function callTeamSelected 'w' for write writing to textfield

# CALL YEAR FORMED
def callYearFormed(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		yearFormedOutput.delete(0.0, END)
		atlanta.yearFormedATL
		yearFormedOutput.insert(INSERT, atlanta.yearFormedATL)
	if TeamsVar.get() == "Boston Celtics":
		yearFormedOutput.delete(0.0, END)
		boston.yearFormedBOS
		yearFormedOutput.insert(INSERT, boston.yearFormedBOS)
	if TeamsVar.get() == "Brooklyn Nets":
		yearFormedOutput.delete(0.0, END)
		brooklyn.yearFormedBKN
		yearFormedOutput.insert(INSERT, brooklyn.yearFormedBKN)
	if TeamsVar.get() == "Charlotte Hornets":
		yearFormedOutput.delete(0.0, END)
		charlotte.yearFormedCHA
		yearFormedOutput.insert(INSERT, charlotte.yearFormedCHA)
	if TeamsVar.get() == "Chicago Bulls":
		yearFormedOutput.delete(0.0, END)
		chicago.yearFormedCHI
		yearFormedOutput.insert(INSERT, chicago.yearFormedCHI)
	if TeamsVar.get() == "Cleveland Cavaliers":
		yearFormedOutput.delete(0.0, END)
		cleveland.yearFormedCLE
		yearFormedOutput.insert(INSERT, cleveland.yearFormedCLE)
	if TeamsVar.get() == "Dallas Mavericks":
		yearFormedOutput.delete(0.0, END)
		dallas.yearFormedDAL
		yearFormedOutput.insert(INSERT, dallas.yearFormedDAL)
	if TeamsVar.get() == "Denver Nuggets":
		yearFormedOutput.delete(0.0, END)
		denver.yearFormedDEN
		yearFormedOutput.insert(INSERT, denver.yearFormedDEN)
	if TeamsVar.get() == "Detroit Pistons":
		yearFormedOutput.delete(0.0, END)
		detroit.yearFormedDET
		yearFormedOutput.insert(INSERT, detroit.yearFormedDET)
	if TeamsVar.get() == "Golden State Warriors":
		yearFormedOutput.delete(0.0, END)
		goldenstate.yearFormedGS
		yearFormedOutput.insert(INSERT, goldenstate.yearFormedGS)
	if TeamsVar.get() == "Houston Rockets":
		yearFormedOutput.delete(0.0, END)
		houston.yearFormedHOU
		yearFormedOutput.insert(INSERT, houston.yearFormedHOU)
	if TeamsVar.get() == "Indiana Pacers":
		yearFormedOutput.delete(0.0, END)
		indiana.yearFormedIND
		yearFormedOutput.insert(INSERT, indiana.yearFormedIND)
	if TeamsVar.get() == "Los Angeles Clippers":
		yearFormedOutput.delete(0.0, END)
		losangelesC.yearFormedLAC
		yearFormedOutput.insert(INSERT, losangelesC.yearFormedLAC)
	if TeamsVar.get() == "Los Angeles Lakers":
		yearFormedOutput.delete(0.0, END)
		losangelesL.yearFormedLAL
		yearFormedOutput.insert(INSERT, losangelesL.yearFormedLAL)
	if TeamsVar.get() == "Memphis Grizzlies":
		yearFormedOutput.delete(0.0, END)
		memphis.yearFormedMEM
		yearFormedOutput.insert(INSERT, memphis.yearFormedMEM)

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
	if TeamsVar.get() == "Golden State Warriors":
		teamInfoOutput.delete(0.0, END)
		infoGS = goldenstate.teamInfoGS
		teamInfoOutput.insert(INSERT, infoGS)
	if TeamsVar.get() == "Houston Rockets":
		teamInfoOutput.delete(0.0, END)
		infoHOU = houston.teamInfoHOU
		teamInfoOutput.insert(INSERT, infoHOU)
	if TeamsVar.get() == "Indiana Pacers":
		teamInfoOutput.delete(0.0, END)
		infoIND = indiana.teamInfoIND
		teamInfoOutput.insert(INSERT, infoIND)
	if TeamsVar.get() == "Los Angeles Clippers":
		teamInfoOutput.delete(0.0, END)
		infoLAC = losangelesC.teamInfoLAC
		teamInfoOutput.insert(INSERT, infoLAC)
	if TeamsVar.get() == "Los Angeles Lakers":
		teamInfoOutput.delete(0.0, END)
		infoLAL = losangelesL.teamInfoLAL
		teamInfoOutput.insert(INSERT, infoLAL)
	if TeamsVar.get() == "Memphis Grizzlies":
		teamInfoOutput.delete(0.0, END)
		infoMEM = memphis.teamInfoMEM
		teamInfoOutput.insert(INSERT, infoMEM)

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
	if TeamsVar.get() == "Golden State Warriors":
		lastGameOutput.delete(0.0, END)
		warriorsLastGame = goldenstate.warriorsGame 
		lastGameOutput.insert(INSERT, warriorsLastGame)
	if TeamsVar.get() == "Houston Rockets":
		lastGameOutput.delete(0.0, END)
		rocketsLastGame = houston.rocketsGame 
		lastGameOutput.insert(INSERT, rocketsLastGame)
	if TeamsVar.get() == "Indiana Pacers":
		lastGameOutput.delete(0.0, END)
		pacersLastGame = indiana.pacersGame
		lastGameOutput.insert(INSERT, pacersLastGame)
	if TeamsVar.get() == "Los Angeles Clippers":
		lastGameOutput.delete(0.0, END)
		clippersLastGame = losangelesC.clippersGame 
		lastGameOutput.insert(INSERT, clippersLastGame)
	if TeamsVar.get() == "Los Angeles Lakers":
		lastGameOutput.delete(0.0, END)
		lakersLastGame = losangelesL.lakersGame 
		lastGameOutput.insert(INSERT, lakersLastGame)
	if TeamsVar.get() == "Memphis Grizzlies":
		lastGameOutput.delete(0.0, END)
		grizzliesLastGame = memphis.grizzGame 
		lastGameOutput.insert(INSERT, grizzliesLastGame)

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
		clippersStanding = losangelesC.win()
		outcomeOutput.insert(INSERT, clippersStanding)
	if TeamsVar.get() == "Los Angeles Lakers":
		outcomeOutput.delete(0.0, END)
		lakersStanding = losangelesL.win()
		outcomeOutput.insert(INSERT, lakersStanding)
	if TeamsVar.get() == "Memphis Grizzlies":
		outcomeOutput.delete(0.0, END)
		grizzliesStanding = memphis.win()
		outcomeOutput.insert(INSERT, grizzliesStanding)

TeamsVar.trace("w", callWinLoss)

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

TeamsVar.trace("w", callTeamLogo)



window.mainloop()
