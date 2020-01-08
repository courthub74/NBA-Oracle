from tkinter import *
import requests
import json

# WINDOW
app = Tk()
app.geometry("550x800")
app.iconbitmap("icons/NBA.ico")
app.configure(background="DarkBlue")
# app.config(image='icons/BallCourt.png')
app.title("NBA Oracle")
scroll = Scrollbar(app, orient="vertical")
scroll.pack(side=RIGHT, fill=Y)

###############################################################

# DATA
blankspace = "          "

# TEAM DATA API SCRAPING
##############################################################################
# ATLANTA HAWKS

# ATLANTA General Info 134880
hawksRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Atlanta%20Hawks")
# ATLANTA Last Game 134880
hawksLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134880")
# ATLANTA Next Game 134880
hawksNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134880")

# ATLANTA Info Parse 134880
dataATL = hawksRE.text
parseATL = json.loads(dataATL)

# ATLANTA Last Game Parse 134880
LGdataATL = hawksLG.text
LGparseATL = json.loads(LGdataATL)

# ATLANTA Next Game Parse 134880
NGdataATL = hawksNG.text
NGparseATL = json.loads(NGdataATL)

# Info Layout for Drop Down ATLANTA
hawksTeam = parseATL["teams"][0]["strTeam"]
yearFormedATL = parseATL["teams"][0]["intFormedYear"]
teamStadiumATL = parseATL["teams"][0]["strStadium"]
teamInfoATL = parseATL["teams"][0]["strDescriptionEN"]
lastGameDateATL = LGparseATL["results"][0]["dateEventLocal"]
homeTeamATL = LGparseATL["results"][0]["strHomeTeam"]
awayTeamATL = LGparseATL["results"][0]["strAwayTeam"]
homeScoreATL = LGparseATL["results"][0]["intHomeScore"]
awayScoreATL = LGparseATL["results"][0]["intAwayScore"]

# Last Game Info Printout
hawksHome = "Home: " + homeTeamATL + " " + homeScoreATL
hawksAway = "Away: " + awayTeamATL + " " + awayScoreATL

hawksGame = lastGameDateATL + """
""" + hawksHome + """
""" + hawksAway + ""

#################################################################################
# BOSTON CELTICS
# CELTICS General Info 134860
celticsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Boston%20Celtics")
# CELTICS Last Game 134860
celticsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134860")
# CELTICS Next Game 134860
celticsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134860")

# CELTICS General Info Parse
dataBOS = celticsRE.text
parseBOS = json.loads(dataBOS)

# CELTICS Last Game Parse
LGdataBOS = celticsLG.text
LGparseBOS = json.loads(LGdataBOS)

# CELTICS Next Game Parse
NGdataBOS = celticsNG.text
NGparseBOS = json.loads(NGdataBOS)

# Info Layout for Drop Down BOSTON
celticsTeam = parseBOS["teams"][0]["strTeam"]
yearFormedBOS = parseBOS["teams"][0]["intFormedYear"]
teamStadiumBOS = parseBOS["teams"][0]["strStadium"]
teamInfoBOS = parseBOS["teams"][0]["strDescriptionEN"]
lastGameDateBOS = LGparseBOS["results"][0]["dateEventLocal"]
homeTeamBOS = LGparseBOS["results"][0]["strHomeTeam"]
awayTeamBOS = LGparseBOS["results"][0]["strAwayTeam"]
homeScoreBOS = LGparseBOS["results"][0]["intHomeScore"]
awayScoreBOS = LGparseBOS["results"][0]["intAwayScore"]

# Last Game Info Printout CELTICS
celticsHome = "Home: " + homeTeamBOS + " " + homeScoreBOS
celticsAway = "Away: " + awayTeamBOS + " " + awayScoreBOS

celticsGame = lastGameDateBOS + """
""" + celticsHome + """
""" + celticsAway + ""
#################################################################################
# BROOKLYN NETS
# NETS General Info 134861
netsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Brooklyn%20Nets")
# NETS Last Game 134861
netsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134861")
# NETS Next Game 134861
netsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134861")

# General Info Parsed
dataBKN = netsRE.text
parseBKN = json.loads(dataBKN)

# Last Game Parsed
LGdataBKN = netsLG.text
LGparseBKN = json.loads(LGdataBKN)

# Next Game Parsed
NGdataBKN = netsNG.text
NGparseBKN = json.loads(NGdataBKN)

# info Layout for the Drop Down Menu to Gather from
netsTeam = parseBKN["teams"][0]["strTeam"]
yearFormedBKN = parseBKN["teams"][0]["intFormedYear"]
teamStadiumBKN = parseBKN["teams"][0]["strStadium"]
teamInfoBKN = parseBKN["teams"][0]["strDescriptionEN"]
lastGameDateBKN = LGparseBKN["results"][0]["dateEventLocal"]
homeTeamBKN = LGparseBKN["results"][0]["strHomeTeam"]
awayTeamBKN = LGparseBKN["results"][0]["strAwayTeam"]
homeScoreBKN = LGparseBKN["results"][0]["intHomeScore"]
awayScoreBKN = LGparseBKN["results"][0]["intAwayScore"]

# Last Game Info Printout NETS
netsHome = "Home: " + homeTeamBKN + " " + homeScoreBKN
netsAway = "Away: " + awayTeamBKN + " " + awayScoreBKN

netsGame = lastGameDateBKN + """
""" + netsHome + """
""" + netsAway + ""
#################################################################################
# CHARLOTTE HORNETS
# HORNETS General Info 134881
hornetsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Charlotte%20Hornets")
# HORNETS Last Game Info 134881
hornetsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134881")
# HORNETS Next Game Info 134881
hornetsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134881")

# General Info Parsed
dataCHA = hornetsRE.text
parseCHA = json.loads(dataCHA)

# Last Game Parsed
LGdataCHA = hornetsLG.text
LGparseCHA = json.loads(LGdataCHA)

# Next Game Parsed
NGdataCHA = hornetsNG.text
NGdataCHA = json.loads(NGdataCHA)

# info Layout for the Drop Down Menu to Gather from
hornetsTeam = parseCHA["teams"][0]["strTeam"]
yearFormedCHA = parseCHA["teams"][0]["intFormedYear"]
teamStadiumCHA = parseCHA["teams"][0]["strStadium"]
teamInfoCHA = parseCHA["teams"][0]["strDescriptionEN"]
lastGameDateCHA = LGparseCHA["results"][0]["dateEventLocal"]
homeTeamCHA = LGparseCHA["results"][0]["strHomeTeam"]
awayTeamCHA = LGparseCHA["results"][0]["strAwayTeam"]
homeScoreCHA = LGparseCHA["results"][0]["intHomeScore"]
awayScoreCHA = LGparseCHA["results"][0]["intAwayScore"]

# Last Game Info Printout HORNETS
hornetsHome = "Home: " + homeTeamCHA + " " + homeScoreCHA
hornetsAway = "Away: " + awayTeamCHA + " " + awayScoreCHA

hornetsGame = lastGameDateCHA + """
""" + hornetsHome + """
""" + hornetsAway + ""
#################################################################################
# DETROIT PISTONS

# PISTONS General Info 134872
pistonsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Detroit%20Pistons")
# PISTONS Last Game 134872
pistonsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134872")
# PISTONS Next Game 134872
pistonsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134872")

# General Info Parsed
dataDET = pistonsRE.text
parseDET = json.loads(dataDET)
# For the Test
# print(pistonsDET.status_code)
# print(json.dumps(parseDET, indent=4))

# Last Game Parsed
LGdataDET = pistonsLG.text
LGparseDET = json.loads(LGdataDET)

# Next Game Parsed
NGdataDET = pistonsNG.text
NGparseDET = json.loads(NGdataDET)

# info Layout for the Drop Down Menu to Gather from
pistonsTeam = parseDET["teams"][0]["strTeam"]
yearFormedDET = parseDET["teams"][0]["intFormedYear"]
teamStadiumDET = parseDET["teams"][0]["strStadium"]
teamInfoDET = parseDET["teams"][0]["strDescriptionEN"]
lastGameDateDET = LGparseDET["results"][0]["dateEventLocal"]
homeTeamDET = LGparseDET["results"][0]["strHomeTeam"]
awayTeamDET = LGparseDET["results"][0]["strAwayTeam"]
homeScoreDET = LGparseDET["results"][0]["intHomeScore"]
awayScoreDET = LGparseDET["results"][0]["intAwayScore"]

# Last Game Info Printout PISTONS
pistonsHome = "Home: " + homeTeamDET + " " + homeScoreDET
pistonsAway = "Away: " + awayTeamDET + " " + awayScoreDET

pistonsGame = lastGameDateDET + """
""" + pistonsHome + """
""" + pistonsAway + ""
#########################################################################################
# LOS ANGELES LAKERS
# KCal the LAKERS are playing 134867
lakersRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Los%20Angeles%20Lakers")
# LAKERS last game info
lakersLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134867")
# LAKERS next game info
lakersNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134867")

# LAKERS General Info Parsed 134867
dataLAL = lakersRE.text
parseLAL = json.loads(dataLAL)
# Last Game Parsed
LGdataLAL = lakersLG.text
LGparseLAL = json.loads(LGdataLAL)
# Next Game Parsed
NGdataLAL = lakersNG.text
NGparseLAL = json.loads(NGdataLAL)

# info Layout for the Drop Down Menu to Gather from LAKERS 134867
lakersTeam = parseLAL["teams"][0]["strTeam"]
yearFormedLAL = parseLAL["teams"][0]["intFormedYear"]
teamStadiumLAL = parseLAL["teams"][0]["strStadium"]
teamInfoLAL = parseLAL["teams"][0]["strDescriptionEN"]
lastGameDateLAL = LGparseLAL["results"][0]["dateEventLocal"]
homeTeamLAL = LGparseLAL["results"][0]["strHomeTeam"]
awayTeamLAL = LGparseLAL["results"][0]["strAwayTeam"]
homeScoreLAL = LGparseLAL["results"][0]["intHomeScore"]
awayScoreLAL = LGparseLAL["results"][0]["intAwayScore"]

# Last Game Info Printout LAKERS
lakersHome = "Home: " + homeTeamLAL + " " + homeScoreLAL
lakersAway = "Away: " + awayTeamLAL + " " + awayScoreLAL

lakersGame = lastGameDateDET + """
""" + lakersHome + """
""" + lakersAway + ""
#########################################################################
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
    if TeamsVar.get() == "Atlanta Hawks":
        teamSelectedOutput.delete(0.0, 'end')
        selectATL = hawksTeam
        teamSelectedOutput.insert(INSERT, selectATL)
    if TeamsVar.get() == "Boston Celtics":
        teamSelectedOutput.delete(0.0, 'end')
        selectBOS = celticsTeam
        teamSelectedOutput.insert(INSERT, selectBOS)
    if TeamsVar.get() == "Brooklyn Nets":
        teamSelectedOutput.delete(0.0, 'end')
        selectBKN = netsTeam
        teamSelectedOutput.insert(INSERT, selectBKN)
    if TeamsVar.get() == "Charlotte Hornets":
        teamSelectedOutput.delete(0.0, 'end')
        selectCHA = hornetsTeam
        teamSelectedOutput.insert(INSERT, selectCHA)
    if TeamsVar.get() == "Detroit Pistons":
        teamSelectedOutput.delete(0.0, 'end')
        tSelect1 = pistonsTeam
        teamSelectedOutput.insert(INSERT, tSelect1)
    if TeamsVar.get() == "Los Angeles Lakers":
        teamSelectedOutput.delete(0.0, 'end')
        tSelect2 = lakersTeam
        teamSelectedOutput.insert(INSERT, tSelect2)
    if TeamsVar.get() == "Milwaukee Bucks":
        teamSelectedOutput.delete(0.0, 'end')
        tSelect3 = teamName3
        teamSelectedOutput.insert(INSERT, tSelect3)


# Year Formed Populate
def callYearFormed(*args):
    if TeamsVar.get() == "Atlanta Hawks":
        yearFormOutput.delete(0.0, 'end')
        yearATL = yearFormedATL
        yearFormOutput.insert(INSERT, yearATL)
    if TeamsVar.get() == "Boston Celtics":
        yearFormOutput.delete(0.0, 'end')
        yearBOS = yearFormedBOS
        yearFormOutput.insert(INSERT, yearBOS)
    if TeamsVar.get() == "Brooklyn Nets":
        yearFormOutput.delete(0.0, 'end')
        yearBKN = yearFormedBKN
        yearFormOutput.insert(INSERT, yearBKN)
    if TeamsVar.get() == "Charlotte Hornets":
        yearFormOutput.delete(0.0, 'end')
        yearCHA = yearFormedCHA
        yearFormOutput.insert(INSERT, yearCHA)
    if TeamsVar.get() == "Detroit Pistons":
        yearFormOutput.delete(0.0, 'end')
        yearSel1 = yearFormedDET
        yearFormOutput.insert(INSERT, yearSel1)
    if TeamsVar.get() == "Los Angeles Lakers":
        yearFormOutput.delete(0.0, 'end')
        yearSel2 = yearFormedLAL
        yearFormOutput.insert(INSERT, yearSel2)
    if TeamsVar.get() == "Milwaukee Bucks":
        yearFormOutput.delete(0.0, 'end')
        yearSel3 = yearFormed3
        yearFormOutput.insert(INSERT, yearSel3)


# Team Stadium Populate
def callTeamStadium(*args):
    if TeamsVar.get() == "Atlanta Hawks":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumATL = teamStadiumATL
        teamStadiumOutput.insert(INSERT, stadiumATL)
    if TeamsVar.get() == "Boston Celtics":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumBOS = teamStadiumBOS
        teamStadiumOutput.insert(INSERT, stadiumBOS)
    if TeamsVar.get() == "Brooklyn Nets":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumBKN = teamStadiumBKN
        teamStadiumOutput.insert(INSERT, stadiumBKN)
    if TeamsVar.get() == "Charlotte Hornets":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumCHA = teamStadiumCHA
        teamStadiumOutput.insert(INSERT, stadiumCHA)
    if TeamsVar.get() == "Detroit Pistons":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumDET = teamStadiumDET
        teamStadiumOutput.insert(INSERT, stadiumDET)
    if TeamsVar.get() == "Los Angeles Lakers":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumLAL = teamStadiumLAL
        teamStadiumOutput.insert(INSERT, stadiumLAL)


# Team Info Populate
def callTeamInfo(*args):
    if TeamsVar.get() == "Atlanta Hawks":
        teamInfoOutput.delete(0.0, 'end')
        infoATL = teamInfoATL
        teamInfoOutput.insert(INSERT, infoATL)
    if TeamsVar.get() == "Boston Celtics":
        teamInfoOutput.delete(0.0, 'end')
        infoBOS = teamInfoBOS
        teamInfoOutput.insert(INSERT, infoBOS)
    if TeamsVar.get() == "Brooklyn Nets":
        teamInfoOutput.delete(0.0, 'end')
        infoBKN = teamInfoBKN
        teamInfoOutput.insert(INSERT, infoBKN)
    if TeamsVar.get() == "Charlotte Hornets":
        teamInfoOutput.delete(0.0, 'end')
        infoCHA = teamInfoCHA
        teamInfoOutput.insert(INSERT, infoCHA)
    if TeamsVar.get() == "Detroit Pistons":
        teamInfoOutput.delete(0.0, 'end')
        infoSel1 = teamInfoDET
        teamInfoOutput.insert(INSERT, infoSel1)
    if TeamsVar.get() == "Los Angeles Lakers":
        teamInfoOutput.delete(0.0, 'end')
        infoSel2 = teamInfoLAL
        teamInfoOutput.insert(INSERT, infoSel2)
    if TeamsVar.get() == "Milwaukee Bucks":
        teamInfoOutput.delete(0.0, 'end')
        infoSel3 = teamInfo3
        teamInfoOutput.insert(INSERT, infoSel3)


# Last Game Populate
def callLastGame(*args):
    if TeamsVar.get() == "Atlanta Hawks":
        lastGameOutput.delete(0.0, 'end')
        hawksLastGame = hawksGame
        lastGameOutput.insert(INSERT, hawksLastGame)
    if TeamsVar.get() == "Boston Celtics":
        lastGameOutput.delete(0.0, 'end')
        celticsLastGame = celticsGame
        lastGameOutput.insert(INSERT, celticsLastGame)
    if TeamsVar.get() == "Brooklyn Nets":
        lastGameOutput.delete(0.0, 'end')
        netsLastGame = netsGame
        lastGameOutput.insert(INSERT, netsLastGame)
    if TeamsVar.get() == "Charlotte Hornets":
        lastGameOutput.delete(0.0, 'end')
        hornetsLastGame = hornetsGame
        lastGameOutput.insert(INSERT, hornetsLastGame)
    if TeamsVar.get() == "Detroit Pistons":
        lastGameOutput.delete(0.0, 'end')
        pistonsLastGame = pistonsGame
        lastGameOutput.insert(INSERT, pistonsLastGame)
    if TeamsVar.get() == "Los Angeles Lakers":
        lastGameOutput.delete(0.0, 'end')
        lakersLastGame = lakersGame
        lastGameOutput.insert(INSERT, lakersLastGame)


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
TeamsVar.trace("w", callTeamStadium)
TeamsVar.trace("w", callTeamInfo)
TeamsVar.trace("w", callLastGame)
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

# Year Formed
yearForm = Label(app, text="Year Formed", bg='DarkBlue', fg='White', font='Arial 10 bold')
yearForm.pack()
yearFormOutput = Text(app, width=10, height=1, bg='Black', fg='White', font='none 10')
yearFormOutput.pack()

# Team Stadium
teamStadium = Label(app, text="Team Stadium", bg='DarkBlue', fg='White', font='Arial 10 bold')
teamStadium.pack()
teamStadiumOutput = Text(app, width=30, height=1, bg='Black', fg='White', font='none 10')
teamStadiumOutput.pack()

# Team Info
teamInfo = Label(app, text="Team History", bg='DarkBlue', fg='White', font='Arial 10 bold')
teamInfo.pack()
teamInfoOutput = Text(app, width=70, height=4, bg='Black', fg='White', font='none 10')
teamInfoOutput.pack()

# Last Game Info
lastGame = Label(app, text="Last Game Played", bg='DarkBlue', fg='White', font='Arial 10 bold')
lastGame.pack()
lastGameOutput = Text(app, width=30, height=3, bg='Black', fg='White', font='none 10')
lastGameOutput.pack()

# Team Logo
'''teamLogo = Label(app, text="Team Logo", bg='DarkBlue', fg='White', font='Arial 10 bold')
teamLogo.pack()'''

# Logo Canvas
LogoCanvas = Canvas(height=150, width=100, borderwidth=0, highlightthickness=0, bg='DarkBlue', bd=0)
LogoCanvas.pack()

# The image could maybe get extracted for a good challenge
'''othaLogo = Canvas(app, bg="Blue")
othaLogo.pack()'''


def callTeamLogo(*args):
    if TeamsVar.get() == "Atlanta Hawks":
        LogoCanvas.delete("all")
        hawksLogo = PhotoImage(file="icons/Hawks1001.png")
        LogoCanvas.image = hawksLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=hawksLogo)
    if TeamsVar.get() == "Boston Celtics":
        celticsLogo = PhotoImage(file="icons/Celtics2001.png")
        LogoCanvas.image = celticsLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=celticsLogo)
    if TeamsVar.get() == "Brooklyn Nets":
        netsLogo = PhotoImage(file="icons/Nets2001.png")
        LogoCanvas.image = netsLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=netsLogo)
    if TeamsVar.get() == "Charlotte Hornets":
        hornetsLogo = PhotoImage(file="icons/Hornets1001.png")
        LogoCanvas.image = hornetsLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=hornetsLogo)
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
