from tkinter import *
import requests
import json

# WINDOW
app = Tk()
app.geometry("600x900")
app.iconbitmap("icons/NBA.ico")
app.configure(background="DarkBlue")
app.title("NBA Oracle")
scroll = Scrollbar(app, orient="vertical")
scroll.pack(side=RIGHT, fill=Y)

###############################################################

# DATA
blankspace = "          "

# API SCRAPING

# PISTONS General Info 134872
pistonsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Detroit%20Pistons")
# PISTONS Last Game 134872
pistonsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134872")
# PISTONS Next Game 134872
pistonsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134872")

# General Info Parsed
dataRE = pistonsRE.text
parseRE = json.loads(dataRE)
# For the Test
# print(pistonsRE.status_code)
# print(json.dumps(parseRE, indent=4))

# Last Game Parsed
dataLG = pistonsLG.text
parseLG = json.loads(dataLG)

# Next Game Parsed
dataNG = pistonsNG.text
parseNG = json.loads(dataNG)

# info Layout for the Drop Down Menu to Gather from
teamName1 = parseRE["teams"][0]["strTeam"]
yearFormed1 = parseRE["teams"][0]["intFormedYear"]
teamStadium1 = parseRE["teams"][0]["strStadium"]
teamInfo1 = parseRE["teams"][0]["strDescriptionEN"]

# KCal the LAKERS are playing 134867
lakersRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Los%20Angeles%20Lakers")
# LAKERS last game info
lakersLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134867")
# LAKERS next game info
lakersNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134867")

# LAKERS General Info Parsed 134867
dataRE2 = lakersRE.text
parseRE2 = json.loads(dataRE2)
# Last Game Parsed
dataLG2 = lakersLG.text
parseLG2 = json.loads(dataLG2)
# Next Game Parsed
dataNG2 = lakersNG.text
parseNG2 = json.loads(dataNG2)

# info Layout for the Drop Down Menu to Gather from LAKERS 134867
teamName2 = parseRE2["teams"][0]["strTeam"]
yearFormed2 = parseRE2["teams"][0]["intFormedYear"]
teamStadium2 = parseRE2["teams"][0]["strStadium"]
teamInfo2 = parseRE2["teams"][0]["strDescriptionEN"]

# MILWAUKEE BUCKS General Info 134874
bucksRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Milwaukee%20Bucks")
# Last Game info for BUCKS 134874
bucksLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134874")
# Next Game info for BUCKS 134874
bucksNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134874")

# BUCKS General Info Parsed 134874
dataRE3 = bucksRE.text
parseRE3 = json.loads(dataRE3)
# Last Game Parsed
dataLG3 = bucksLG.text
parseLG3 = json.loads(dataLG3)
# Next Game Parsed
dataNG3 = bucksNG.text
parseNG3 = json.loads(dataNG3)

# info Layout for the Drop Down Menu to Gather from BUCKS 134874
teamName3 = parseRE3["teams"][0]["strTeam"]
yearFormed3 = parseRE3["teams"][0]["intFormedYear"]
teamStadium3 = parseRE3["teams"][0]["strStadium"]
teamInfo3 = parseRE3["teams"][0]["strDescriptionEN"]

# The LIST of Teams on the DROP DOWN MENU (Blank has 10 spaces)
TeamsList = [
    "Select Team Here:",
    "Atlanta Hawks",
    "Boston Celtics",
    "Brooklyn Nets",
    "Charlotte Hornets",
    "Chicago Bulls",
    "Cleveland Cavaliers",
    "Dallas Mavericks",
    "Denver Nuggets",
    "Detroit Pistons",
    "Golden State Warriors",
    "Houston Rockets",
    "Indiana Pacers",
    "Los Angeles Clippers",
    "Los Angeles Lakers",
    "Memphis Grizzlies",
    "Miami Heat",
    "Milwaukee Bucks",
    "Minnesota Timberwolves",
    "New Orleans Pelicans",
    "New York Knicks",
    "Oklahoma City Thunder",
    "Orlando Magic",
    "Philadelphia 76ers",
    "Phoenix Suns",
    "Portland Trail Blazers",
    "Sacramento Kings",
    "San Antonio Spurs",
    "Toronto Raptors",
    "Utah Jazz",
    "Washington Wizards",

]


###############################################################

# FUNCTIONALITY

# Team Selected Populate
def callTeamSelected(*args):
    if TeamsVar.get() == "Detroit Pistons":
        teamSelectedOutput.delete(0.0, 'end')
        tSelect1 = teamName1
        teamSelectedOutput.insert(INSERT, tSelect1)
    if TeamsVar.get() == "Los Angeles Lakers":
        teamSelectedOutput.delete(0.0, 'end')
        tSelect2 = teamName2
        teamSelectedOutput.insert(INSERT, tSelect2)
    if TeamsVar.get() == "Milwaukee Bucks":
        teamSelectedOutput.delete(0.0, 'end')
        tSelect3 = teamName3
        teamSelectedOutput.insert(INSERT, tSelect3)


# Year Formed Populate
def callYearFormed(*args):
    if TeamsVar.get() == "Detroit Pistons":
        yearFormOutput.delete(0.0, 'end')
        yearSel1 = yearFormed1
        yearFormOutput.insert(INSERT, yearSel1)
    if TeamsVar.get() == "Los Angeles Lakers":
        yearFormOutput.delete(0.0, 'end')
        yearSel2 = yearFormed2
        yearFormOutput.insert(INSERT, yearSel2)
    if TeamsVar.get() == "Milwaukee Bucks":
        yearFormOutput.delete(0.0, 'end')
        yearSel3 = yearFormed3
        yearFormOutput.insert(INSERT, yearSel3)


# Team Info Populate
def callTeamInfo(*args):
    if TeamsVar.get() == "Detroit Pistons":
        teamInfoOutput.delete(0.0, 'end')
        infoSel1 = teamInfo1
        teamInfoOutput.insert(INSERT, infoSel1)
    if TeamsVar.get() == "Los Angeles Lakers":
        teamInfoOutput.delete(0.0, 'end')
        infoSel2 = teamInfo2
        teamInfoOutput.insert(INSERT, infoSel2)
    if TeamsVar.get() == "Milwaukee Bucks":
        teamInfoOutput.delete(0.0, 'end')
        infoSel3 = teamInfo3
        teamInfoOutput.insert(INSERT, infoSel3)


# For BELOW you would have to extract the image that comes from the link provided

'''def callOthaLogo(*args):
    if TeamsVar.get() == "Detroit Pistons":
        othaLogo.delete(0.0, 'end')
        pisLogo = teamLogo
        othaLogo.insert(INSERT, pisLogo)'''


# DROP DOWN MENU COMMAND (Trace Values)
TeamsVar = StringVar()
TeamsVar.set(TeamsList[0])
TeamsVar.trace("w", callTeamSelected)
TeamsVar.trace("w", callYearFormed)
TeamsVar.trace("w", callTeamInfo)
# TeamsVar.trace("w", callOthaLogo)

###############################################################

# HEADER
logo = PhotoImage(file='icons/nbaCLEAR.png')
logoNBA = Label(app, image=logo, bg="DarkBlue")
resizNBAlogo = logo.subsample(1, 1)
logoNBA.config(image=resizNBAlogo)
logoNBA.pack()

# Drop Down Menu
droplist = OptionMenu(app, TeamsVar, *TeamsList)
droplist.config(width=20, height=1, fg='Blue')
droplist.pack()

# Team Selected
teamSelected = Label(app, text="Team Selected", bg='DarkBlue', fg='White', font='Arial 10 bold')
teamSelected.pack()
teamSelectedOutput = Text(app, width=30, height=1, bg='Black', fg='White', font='none 10')
teamSelectedOutput.pack()

# Team Logo
teamLogo = Label(app, text="Team Logo", bg='DarkBlue', fg='White', font='Arial 10 bold')
teamLogo.pack()

LogoCanvas = Canvas(height=150, width=100, borderwidth=0, highlightthickness=0, bg='DarkBlue', bd=0)
LogoCanvas.pack()

# Year Formed
yearForm = Label(app, text="Year Formed", bg='DarkBlue', fg='White', font='Arial 10 bold')
yearForm.pack()
yearFormOutput = Text(app, width=10, height=1, bg='Black', fg='White', font='none 10')
yearFormOutput.pack()

# Team Info
teamInfo = Label(app, text="Team History", bg='DarkBlue', fg='White', font='Arial 10 bold')
teamInfo.pack()
teamInfoOutput = Text(app, width=70, height=4, bg='Black', fg='White', font='none 10')
teamInfoOutput.pack()


# The image could maybe get extracted for a good challenge
'''othaLogo = Canvas(app, bg="Blue")
othaLogo.pack()'''


def callTeamLogo(*args):
    if TeamsVar.get() == "Detroit Pistons":
        LogoCanvas.delete("all")
        pistonsLogo = PhotoImage(file='icons/Pistons1001.png')
        LogoCanvas.image = pistonsLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=pistonsLogo)
        LogoCanvas.pack()
    if TeamsVar.get() == "Los Angeles Lakers":
        LogoCanvas.delete("all")
        lakersLogo = PhotoImage(file='icons/Lakers1001.png')
        LogoCanvas.image = lakersLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=lakersLogo)
        LogoCanvas.pack()
    if TeamsVar.get() == "Milwaukee Bucks":
        LogoCanvas.delete("all")
        bucksLogo = PhotoImage(file='icons/Bucks2001.png')
        LogoCanvas.image = bucksLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=bucksLogo)
        LogoCanvas.pack()


TeamsVar.trace("w", callTeamLogo)
# Trace call with creation of the canvas and logo on it

app.mainloop()
