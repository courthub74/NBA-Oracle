from tkinter import *
import requests
import json

# WINDOW
app = Tk()
app.geometry("1800x1500")
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
hawksHome = "Home: " + str(homeTeamATL) + " " + str(homeScoreATL)
hawksAway = "Away: " + str(awayTeamATL) + " " + str(awayScoreATL)

hawksGame = lastGameDateATL + """
""" + hawksHome + """
""" + hawksAway + ""

#####################################################################################################
ATLhomeTeam = homeTeamATL
ATLoppTeam = awayTeamATL


def CallWinnerATL():
    if str(homeScoreATL) > str(awayScoreATL):
        return ATLhomeTeam


ATLwinner = CallWinnerATL()


# ALL THE FUNCTION ABOVE DOES IS COMPARE HOME TEAM SCORE TO AWAY TEAM

# BELOW YOU ARE USING THE OUTCOME TO LOOK FOR THE FOCUS TEAM BY
# ENTERING THE STRING OF THE 'FOCUS TEAM' COMPARING IT TO THE WINNER


def ATLCountWin(*args):
    if ATLwinner == "Atlanta Hawks":
        return "W"


ATLCountWin()
ATLwin = ATLCountWin()
print(ATLwin)


def ATLCountLoss(*args):
    if ATLwinner != "Atlanta Hawks":
        return "L"


ATLCountLoss()
ATLloss = ATLCountLoss()
print(ATLloss)


##########################################################################################################

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
celticsHome = "Home: " + str(homeTeamBOS) + " " + str(homeScoreBOS)
celticsAway = "Away: " + str(awayTeamBOS) + " " + str(awayScoreBOS)

celticsGame = lastGameDateBOS + """
""" + celticsHome + """
""" + celticsAway + ""

##########################################################################################################

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
print(BOSwin)


def BOSCountLoss(*args):
    if BOSwinner != "Boston Celtics":
        return "L"


BOSCountLoss()
BOSloss = BOSCountLoss()
print(BOSloss)

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
netsHome = "Home: " + str(homeTeamBKN) + " " + str(homeScoreBKN)
netsAway = "Away: " + str(awayTeamBKN) + " " + str(awayScoreBKN)

netsGame = lastGameDateBKN + """
""" + netsHome + """
""" + netsAway + ""

BKNhomeTeam = homeTeamBKN
BKNoppTeam = awayTeamBKN


def BKNCallWinner():
    if str(homeScoreBKN) > str(awayScoreBKN):
        return BKNhomeTeam


BKNwinner = BKNCallWinner()


def BKNCountWin():
    if BKNwinner == "Brooklyn Nets":
        return "W"


BKNCountWin()
BKNwin = BKNCountWin()
print(BKNwin)


def BKNCountLoss():
    if BKNwinner != "Brooklyn Nets":
        return "L"


BKNCountLoss()
BKNloss = BKNCountLoss()
print(BKNloss)
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
hornetsHome = "Home: " + str(homeTeamCHA) + " " + str(homeScoreCHA)
hornetsAway = "Away: " + str(awayTeamCHA) + " " + str(awayScoreCHA)

hornetsGame = lastGameDateCHA + """
""" + hornetsHome + """
""" + hornetsAway + ""


CHAhomeTeam = homeTeamCHA
CHAoppTeam = awayTeamCHA


def CallWinnerCHA():
    if str(homeScoreATL) > str(awayScoreATL):
        return ATLhomeTeam


CHAwinner = CallWinnerCHA()


def CHACountWin(*args):
    if CHAwinner == "Charlotte Hornets":
        outcomeOut.delete(0.0, END)
        won = "W"
        outcomeOut.insert(INSERT, won)


def CHACountLoss(*args):
    if CHAwinner != "Charlotte Hornets":
        outcomeOut.delete(0.0, END)
        loss = "L"
        outcomeOut.insert(INSERT, loss)


#################################################################################
# CHICAGO BULLS

# BULLS General Info 134870
bullsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Chicago%20Bulls")
# BULLS Last Game Info 134870
bullsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134870")
# BULLS Next Game Info 134870
bullsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134870")

# General Info Parsed
dataCHI = bullsRE.text
parseCHI = json.loads(dataCHI)

# Last Game Parsed
LGdataCHI = bullsLG.text
LGparseCHI = json.loads(LGdataCHI)

# Next Game Parsed
NGdataCHI = bullsNG.text
NGparseCHI = json.loads(NGdataCHI)

# info Layout for the Drop Down Menu to Gather from
bullsTeam = parseCHI["teams"][0]["strTeam"]
yearFormedCHI = parseCHI["teams"][0]["intFormedYear"]
teamStadiumCHI = parseCHI["teams"][0]["strStadium"]
teamInfoCHI = parseCHI["teams"][0]["strDescriptionEN"]
lastGameDateCHI = LGparseCHI["results"][0]["dateEventLocal"]
homeTeamCHI = LGparseCHI["results"][0]["strHomeTeam"]
awayTeamCHI = LGparseCHI["results"][0]["strAwayTeam"]
homeScoreCHI = LGparseCHI["results"][0]["intHomeScore"]
awayScoreCHI = LGparseCHI["results"][0]["intAwayScore"]

# Last Game Info Printout BULLS
bullsHome = "Home: " + str(homeTeamCHI) + " " + str(homeScoreCHI)
bullsAway = "Away: " + str(awayTeamCHI) + " " + str(awayScoreCHI)

bullsGame = lastGameDateCHI + """
""" + bullsHome + """
""" + bullsAway + ""


CHIhomeTeam = homeTeamCHI
CHIoppTeam = awayTeamCHI


def CallWinnerCHI():
    if str(homeScoreCHI) > str(awayScoreCHI):
        return CHIhomeTeam


CHIwinner = CallWinnerCHI()


def CHICountWin(*args):
    if CHIwinner == "Chicago Bulls":
        return "W"


CHICountWin()
CHIwin = CHICountWin()
print(CHIwin)


def CHICountLoss(*args):
    if CHIwinner != "Chicago Bulls":
        return "L"


CHICountLoss()
CHIloss = CHICountLoss()
print(CHIloss)


'''def CHICountWin(*args):
    if CHIwinner == "Chicago Bulls":
        outcomeOut.delete(0.0, END)
        won = "W"
        outcomeOut.insert(INSERT, won)


def CHICountLoss(*args):
    if CHIwinner != "Chicage Bulls":
        outcomeOut.delete(0.0, END)
        loss = "L"
        outcomeOut.insert(INSERT, loss)'''


#################################################################################
# CLEVELAND CAVALIERS

# CAVALIERS General Info 134871
cavsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Cleveland%20Cavaliers")
# CAVALIERS Last Game 134871
cavsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134871")
# CAVALIERS Next Game 134871
cavsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134871")

# General Info Parsed
dataCLE = cavsRE.text
parseCLE = json.loads(dataCLE)
# print(cavsRE.status_code)

# Last Game Parsed
LGdataCLE = cavsLG.text
LGparseCLE = json.loads(LGdataCLE)

# Next Game Parsed
NGdataCLE = cavsNG.text
NGparseCLE = json.loads(NGdataCLE)

# info Layout for the Drop Down Menu to Gather from
cavsTeam = parseCLE["teams"][0]["strTeam"]
yearFormedCLE = parseCLE["teams"][0]["intFormedYear"]
teamStadiumCLE = parseCLE["teams"][0]["strStadium"]
teamInfoCLE = parseCLE["teams"][0]["strDescriptionEN"]
lastGameDateCLE = LGparseCLE["results"][0]["dateEventLocal"]
homeTeamCLE = LGparseCLE["results"][0]["strHomeTeam"]
awayTeamCLE = LGparseCLE["results"][0]["strAwayTeam"]
homeScoreCLE = LGparseCLE["results"][0]["intHomeScore"]
awayScoreCLE = LGparseCLE["results"][0]["intAwayScore"]

# Last Game Info Printout CAVALIERS
cavsHome = "Home: " + str(homeTeamCLE) + " " + str(homeScoreCLE)
cavsAway = "Away: " + str(awayTeamCLE) + " " + str(awayScoreCLE)

cavsGame = lastGameDateCLE + """
""" + cavsHome + """
""" + cavsAway + ""

#################################################################################
# DALLAS MAVERICKS

# MAVERICKS General Info 134875
mavsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Dallas%20Mavericks")
# MAVERICKS Last Game 134875
mavsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134875")
# MAVERICKS Next Game 134875
mavsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134875")

# General Info Parsed
dataDAL = mavsRE.text
parseDAL = json.loads(dataDAL)

# Last Game Parsed
LGdataDAL = mavsLG.text
LGparseDAL = json.loads(LGdataDAL)

# Next Game Parsed
NGdataDAL = mavsNG.text
NGparseDAL = json.loads(NGdataDAL)

# info Layout for the Drop Down Menu to Gather from
mavsTeam = parseDAL["teams"][0]["strTeam"]
yearFormedDAL = parseDAL["teams"][0]["intFormedYear"]
teamStadiumDAL = parseDAL["teams"][0]["strStadium"]
teamInfoDAL = parseDAL["teams"][0]["strDescriptionEN"]
lastGameDateDAL = LGparseDAL["results"][0]["dateEventLocal"]
homeTeamDAL = LGparseDAL["results"][0]["strHomeTeam"]
awayTeamDAL = LGparseDAL["results"][0]["strAwayTeam"]
homeScoreDAL = LGparseDAL["results"][0]["intHomeScore"]
awayScoreDAL = LGparseDAL["results"][0]["intAwayScore"]

# Last Game Info Printout MAVERICKS
mavsHome = "Home: " + str(homeTeamDAL) + " " + str(homeScoreDAL)
mavsAway = "Away: " + str(awayTeamDAL) + " " + str(awayScoreDAL)

mavsGame = lastGameDateDAL + """
""" + mavsHome + """
""" + mavsAway + ""

#################################################################################
# DENVER NUGGETS

# NUGGETS Info Parsed 134885
nuggetsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Denver%20Nuggets")
# NUGGETS Last Game 134885
nuggetsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134885")
# NUGGETS Next Game 134885
nuggetsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134885")

# General Info Parsed
dataDEN = nuggetsRE.text
parseDEN = json.loads(dataDEN)

# Last Game Parsed
LGdataDEN = nuggetsLG.text
LGparseDEN = json.loads(LGdataDEN)

# Next Game Parsed
NGdataDEN = nuggetsNG.text
NGparseDEN = json.loads(NGdataDEN)

# info Layout for the Drop Down Menu to Gather from
nuggetsTeam = parseDEN["teams"][0]["strTeam"]
yearFormedDEN = parseDEN["teams"][0]["intFormedYear"]
teamStadiumDEN = parseDEN["teams"][0]["strStadium"]
teamInfoDEN = parseDEN["teams"][0]["strDescriptionEN"]
lastGameDateDEN = LGparseDEN["results"][0]["dateEventLocal"]
homeTeamDEN = LGparseDEN["results"][0]["strHomeTeam"]
awayTeamDEN = LGparseDEN["results"][0]["strAwayTeam"]
homeScoreDEN = LGparseDEN["results"][0]["intHomeScore"]
awayScoreDEN = LGparseDEN["results"][0]["intAwayScore"]

# Last Game Info Printout PISTONS
nuggetsHome = "Home: " + str(homeTeamDEN) + " " + str(homeScoreDEN)
nuggetsAway = "Away: " + str(awayTeamDEN) + " " + str(awayScoreDEN)

nuggetsGame = lastGameDateDEN + """
""" + nuggetsHome + """
""" + nuggetsAway + ""

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
# print(pistonsRE.status_code)
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
pistonsHome = "Home: " + str(homeTeamDET) + " " + str(homeScoreDET)
pistonsAway = "Away: " + str(awayTeamDET) + " " + str(awayScoreDET)

pistonsGame = lastGameDateDET + """
""" + pistonsHome + """
""" + pistonsAway + ""

#######################################################################################
# GOLDEN STATE WARRIORS

# WARRIORS General Info 134865
warriorsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Golden%20State%20Warriors")

# WARRIORS Last Game 134865
warriorsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134865")

# WARRIORS Next Game 134865
warriorsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134865")

# General Info Parsed
dataGS = warriorsRE.text
parseGS = json.loads(dataGS)
# For the Test
# print(warriorsRE.status_code)

# Last Game Parsed
LGdataGS = warriorsLG.text
LGparseGS = json.loads(LGdataGS)

# Next Game Parsed
NGdataGS = warriorsNG.text
NGparseGS = json.loads(NGdataGS)

# info Layout for the Drop Down Menu to Gather from
warriorsTeam = parseGS["teams"][0]["strTeam"]
yearFormedGS = parseGS["teams"][0]["intFormedYear"]
teamStadiumGS = parseGS["teams"][0]["strStadium"]
teamInfoGS = parseGS["teams"][0]["strDescriptionEN"]
lastGameDateGS = LGparseGS["results"][0]["dateEventLocal"]
homeTeamGS = LGparseGS["results"][0]["strHomeTeam"]
awayTeamGS = LGparseGS["results"][0]["strAwayTeam"]
homeScoreGS = LGparseGS["results"][0]["intHomeScore"]
awayScoreGS = LGparseGS["results"][0]["intAwayScore"]

# Last Game Info Printout WARRIORS
warriorsHome = "Home: " + str(homeTeamGS) + " " + str(homeScoreGS)
warriorsAway = "Away: " + str(awayTeamGS) + " " + str(awayScoreGS)

warriorsGame = lastGameDateGS + """
""" + warriorsHome + """
""" + warriorsAway + ""

########################################################################################
# HOUSTON CALLS (ROCKETS)

# ROCKETS Info 134876
rocketsRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Houston%20Rockets")
# ROCKETS Last Game Info 134876
rocketsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134876")
# ROCKETS Next Game Info 134876
rocketsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134876")

# ROCKETS Info Parsed 134876
dataHOU = rocketsRE.text
parseHOU = json.loads(dataHOU)
# ROCKETS Last Game Parsed 134876
LGdataHOU = rocketsLG.text
LGparseHOU = json.loads(LGdataHOU)
# ROCKETS Next Game Parsed 134876
NGdataHOU = rocketsNG.text
NGparseHOU = json.loads(NGdataHOU)

# info Layout for the Drop Down Menu to Gather from ROCKETS 134876
rocketsTeam = parseHOU["teams"][0]["strTeam"]
yearFormedHOU = parseHOU["teams"][0]["intFormedYear"]
teamStadiumHOU = parseHOU["teams"][0]["strStadium"]
teamInfoHOU = parseHOU["teams"][0]["strDescriptionEN"]
lastGameDateHOU = LGparseHOU["results"][0]["dateEventLocal"]
homeTeamHOU = LGparseHOU["results"][0]["strHomeTeam"]
awayTeamHOU = LGparseHOU["results"][0]["strAwayTeam"]
homeScoreHOU = LGparseHOU["results"][0]["intHomeScore"]
awayScoreHOU = LGparseHOU["results"][0]["intAwayScore"]

# Last Game Info Printout LAKERS
rocketsHome = "Home: " + str(homeTeamHOU) + " " + str(homeScoreHOU)
rocketsAway = "Away: " + str(awayTeamHOU) + " " + str(awayScoreHOU)

rocketsGame = lastGameDateHOU + """
""" + rocketsHome + """
""" + rocketsAway + ""

#########################################################################################
# INDIANA PACERS

# PACERS General Info 134873
pacersRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Indiana%20Pacers")
# PACERS Last Game Info
pacersLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134873")
# PACERS Next Game Info
pacersNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134873")

# PACERS General Info Parsed 134873
dataIND = pacersRE.text
parseIND = json.loads(dataIND)
# Last Game Parsed
LGdataIND = pacersLG.text
LGparseIND = json.loads(LGdataIND)
# Next Game Parsed
NGdataIND = pacersNG.text
NGparseIND = json.loads(NGdataIND)

# info Layout for the Drop Down Menu to Gather from PACERS 134873
pacersTeam = parseIND["teams"][0]["strTeam"]
yearFormedIND = parseIND["teams"][0]["intFormedYear"]
teamStadiumIND = parseIND["teams"][0]["strStadium"]
teamInfoIND = parseIND["teams"][0]["strDescriptionEN"]
lastGameDateIND = LGparseIND["results"][0]["dateEventLocal"]
homeTeamIND = LGparseIND["results"][0]["strHomeTeam"]
awayTeamIND = LGparseIND["results"][0]["strAwayTeam"]
homeScoreIND = LGparseIND["results"][0]["intHomeScore"]
awayScoreIND = LGparseIND["results"][0]["intAwayScore"]

# Last Game Info Printout PACERS
pacersHome = "Home: " + str(homeTeamIND) + " " + str(homeScoreIND)
pacersAway = "Away: " + str(awayTeamIND) + " " + str(awayScoreIND)

pacersGame = lastGameDateIND + """
""" + pacersHome + """
""" + pacersAway + ""

#########################################################################################
# LOS ANGELES CLIPPERS
# CLIPPERS General Info 134866
clippersRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Los%20Angeles%20Clippers")
# CLIPPERS last game info 134866
clippersLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134866")
# CLIPPERS next game info 134866
clippersNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134866")

# CLIPPERS General Info Parsed 134866
dataLAC = clippersRE.text
parseLAC = json.loads(dataLAC)
# Last Game Parsed
LGdataLAC = clippersLG.text
LGparseLAC = json.loads(LGdataLAC)
# Next Game Parsed
NGdataLAC = clippersNG.text
NGparseLAC = json.loads(NGdataLAC)

# info Layout for the Drop Down Menu to Gather from CLIPPERS 134867
clippersTeam = parseLAC["teams"][0]["strTeam"]
yearFormedLAC = parseLAC["teams"][0]["intFormedYear"]
teamStadiumLAC = parseLAC["teams"][0]["strStadium"]
teamInfoLAC = parseLAC["teams"][0]["strDescriptionEN"]
lastGameDateLAC = LGparseLAC["results"][0]["dateEventLocal"]
homeTeamLAC = LGparseLAC["results"][0]["strHomeTeam"]
awayTeamLAC = LGparseLAC["results"][0]["strAwayTeam"]
homeScoreLAC = LGparseLAC["results"][0]["intHomeScore"]
awayScoreLAC = LGparseLAC["results"][0]["intAwayScore"]

# Last Game Info Printout CLIPPERS
clippersHome = "Home: " + str(homeTeamLAC) + " " + str(homeScoreLAC)
clippersAway = "Away: " + str(awayTeamLAC) + " " + str(awayScoreLAC)

clippersGame = lastGameDateLAC + """
""" + clippersHome + """
""" + clippersAway + ""

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
lakersHome = "Home: " + str(homeTeamLAL) + " " + str(homeScoreLAL)
lakersAway = "Away: " + str(awayTeamLAL) + " " + str(awayScoreLAL)

lakersGame = lastGameDateDET + """
""" + lakersHome + """
""" + lakersAway + ""

############################################################################################
# MEMPHIS GRIZZLIES

# GRIZZLIES General Info 134877
grizzRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Memphis%20Grizzlies")
# Last Game info for GRIZZLIES 134877
grizzLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134877")
# Next Game info for GRIZZLIES 134877
grizzNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134877")

# GRIZZ General Info Parsed 134877
dataMEM = grizzRE.text
parseMEM = json.loads(dataMEM)
# GRIZZ Last Game Parsed
LGdataMEM = grizzLG.text
LGparseMEM = json.loads(LGdataMEM)
# GRIZZ Next Game Parsed
NGdataMEM = grizzNG.text
NGparseMEM = json.loads(NGdataMEM)

# info Layout for the Drop Down Menu to Gather from GRIZZ 134877
grizzTeam = parseMEM["teams"][0]["strTeam"]
yearFormedMEM = parseMEM["teams"][0]["intFormedYear"]
teamStadiumMEM = parseMEM["teams"][0]["strStadium"]
teamInfoMEM = parseMEM["teams"][0]["strDescriptionEN"]
lastGameDateMEM = LGparseMEM["results"][0]["dateEventLocal"]
homeTeamMEM = LGparseMEM["results"][0]["strHomeTeam"]
awayTeamMEM = LGparseMEM["results"][0]["strAwayTeam"]
homeScoreMEM = LGparseMEM["results"][0]["intHomeScore"]
awayScoreMEM = LGparseMEM["results"][0]["intAwayScore"]

# Last Game Info Printout GRIZZLIES
grizzHome = "Home: " + str(homeTeamMEM) + " " + str(homeScoreMEM)
grizzAway = "Away: " + str(awayTeamMEM) + " " + str(awayScoreMEM)

grizzGame = lastGameDateMEM + """
""" + grizzHome + """
""" + grizzAway + ""

############################################################################################
# MIAMI HEAT

# HEAT General Info 134882
heatRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Miami%20Heat")
# Last Game Info HEAT 134882
heatLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134882")
# Next Game Info HEAT 134882
heatNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134882")

# HEAT General Info Parsed 134882
dataMIA = heatRE.text
parseMIA = json.loads(dataMIA)
# Last Game Parsed
LGdataMIA = heatLG.text
LGparseMIA = json.loads(LGdataMIA)
# Next Game Parsed
NGdataMIA = heatNG.text
NGparseMIA = json.loads(NGdataMIA)

# info Layout for the Drop Down Menu to Gather from HEAT 134882
heatTeam = parseMIA["teams"][0]["strTeam"]
yearFormedMIA = parseMIA["teams"][0]["intFormedYear"]
teamStadiumMIA = parseMIA["teams"][0]["strStadium"]
teamInfoMIA = parseMIA["teams"][0]["strDescriptionEN"]
lastGameDateMIA = LGparseMIA["results"][0]["dateEventLocal"]
homeTeamMIA = LGparseMIA["results"][0]["strHomeTeam"]
awayTeamMIA = LGparseMIA["results"][0]["strAwayTeam"]
homeScoreMIA = LGparseMIA["results"][0]["intHomeScore"]
awayScoreMIA = LGparseMIA["results"][0]["intAwayScore"]

# Last Game Info Printout BUCKS
heatHome = "Home: " + str(homeTeamMIA) + " " + str(homeScoreMIA)
heatAway = "Away: " + str(awayTeamMIA) + " " + str(awayScoreMIA)

heatGame = lastGameDateMIA + """
""" + heatHome + """
""" + heatAway + ""

############################################################################################
# MILWAUKEE BUCKS General Info 134874
bucksRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Milwaukee%20Bucks")
# Last Game info for BUCKS 134874
bucksLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134874")
# Next Game info for BUCKS 134874
bucksNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134874")

# BUCKS General Info Parsed 134874
dataMIL = bucksRE.text
parseMIL = json.loads(dataMIL)
# Last Game Parsed
LGdataMIL = bucksLG.text
LGparseMIL = json.loads(LGdataMIL)
# Next Game Parsed
NGdataMIL = bucksNG.text
NGparseMIL = json.loads(NGdataMIL)

# info Layout for the Drop Down Menu to Gather from BUCKS 134874
bucksTeam = parseMIL["teams"][0]["strTeam"]
yearFormedMIL = parseMIL["teams"][0]["intFormedYear"]
teamStadiumMIL = parseMIL["teams"][0]["strStadium"]
teamInfoMIL = parseMIL["teams"][0]["strDescriptionEN"]
lastGameDateMIL = LGparseMIL["results"][0]["dateEventLocal"]
homeTeamMIL = LGparseMIL["results"][0]["strHomeTeam"]
awayTeamMIL = LGparseMIL["results"][0]["strAwayTeam"]
homeScoreMIL = LGparseMIL["results"][0]["intHomeScore"]
awayScoreMIL = LGparseMIL["results"][0]["intAwayScore"]

# Last Game Info Printout BUCKS
bucksHome = "Home: " + str(homeTeamMIL) + " " + str(homeScoreMIL)
bucksAway = "Away: " + str(awayTeamMIL) + " " + str(awayScoreMIL)

bucksGame = lastGameDateMIL + """
""" + bucksHome + """
""" + bucksAway + ""

#######################################################################
# MINNESOTA TIMBERWOLVES

# T WOLVES General Info 134886
twolvesRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Minnesota%20Timberwolves")
# T-WOLVES Last Game Info
twolvesLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134886")
# T-WOLVES Next Game Info
twolvesNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134886")

# T-WOLVES General Info Parsed 134886
dataMIN = twolvesRE.text
parseMIN = json.loads(dataMIN)
# Last Game Parsed
LGdataMIN = twolvesLG.text
LGparseMIN = json.loads(LGdataMIN)
# Next Game Parsed
NGdataMIN = twolvesNG.text
NGparseMIN = json.loads(NGdataMIN)

# info Layout for the Drop Down Menu to Gather from T-WOLVES 134866
twolvesTeam = parseMIN["teams"][0]["strTeam"]
yearFormedMIN = parseMIN["teams"][0]["intFormedYear"]
teamStadiumMIN = parseMIN["teams"][0]["strStadium"]
teamInfoMIN = parseMIN["teams"][0]["strDescriptionEN"]
lastGameDateMIN = LGparseMIN["results"][0]["dateEventLocal"]
homeTeamMIN = LGparseMIN["results"][0]["strHomeTeam"]
awayTeamMIN = LGparseMIN["results"][0]["strAwayTeam"]
homeScoreMIN = LGparseMIN["results"][0]["intHomeScore"]
awayScoreMIN = LGparseMIN["results"][0]["intAwayScore"]

# Last Game Info Printout BUCKS
twolvesHome = "Home: " + str(homeTeamMIN) + " " + str(homeScoreMIN)
twolvesAway = "Away: " + str(awayTeamMIN) + " " + str(awayScoreMIN)

twolvesGame = lastGameDateMIN + """
""" + twolvesHome + """
""" + twolvesAway + ""

#######################################################################
# NEW ORLEANS PELICANS

# General Info for PELICANS 134878
pelicansRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=New%20Orleans%20Pelicans")
# Last Game Info for PELLICANS 134878
pelicansLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134878")
# Next Game Info for PELICANS 134878
pelicansNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134878")

# General Info Parsed
dataNOLA = pelicansRE.text
parseNOLA = json.loads(dataNOLA)
# Last Game Parsed
LGdataNOLA = pelicansLG.text
LGparseNOLA = json.loads(LGdataNOLA)
# Next Game Parsed
NGdataNOLA = pelicansNG.text
NGparseNOLA = json.loads(NGdataNOLA)

# info Layout for the Drop Down Menu to Gather from PELICANS 134878
pelicansTeam = parseNOLA["teams"][0]["strTeam"]
yearFormedNOLA = parseNOLA["teams"][0]["intFormedYear"]
teamStadiumNOLA = parseNOLA["teams"][0]["strStadium"]
teamInfoNOLA = parseNOLA["teams"][0]["strDescriptionEN"]
lastGameDateNOLA = LGparseNOLA["results"][0]["dateEventLocal"]
homeTeamNOLA = LGparseNOLA["results"][0]["strHomeTeam"]
awayTeamNOLA = LGparseNOLA["results"][0]["strAwayTeam"]
homeScoreNOLA = LGparseNOLA["results"][0]["intHomeScore"]
awayScoreNOLA = LGparseNOLA["results"][0]["intAwayScore"]

# Last Game Info Printout BUCKS
pelicansHome = "Home: " + str(homeTeamNOLA) + " " + str(homeScoreNOLA)
pelicansAway = "Away: " + str(awayTeamNOLA) + " " + str(awayScoreNOLA)

pelicansGame = lastGameDateNOLA + """
""" + pelicansHome + """
""" + pelicansAway + ""

#######################################################################
# NEW YORK KNICKS

# General Info for KNICKS 134862
knicksRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=New%20York%20Knicks")
# Last Game Info
knicksLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134862")
# Next Game Info
knicksNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134862")

# General Info Parsed KNICKS 134862
dataNYK = knicksRE.text
parseNYK = json.loads(dataNYK)
# Last Game Parsed
LGdataNYK = knicksLG.text
LGparseNYK = json.loads(LGdataNYK)
# Next Game Parsed
NGdataNYK = knicksNG.text
NGparseNYK = json.loads(NGdataNYK)

# info Layout for the Drop Down Menu to Gather from KNICKS 134862
knicksTeam = parseNYK["teams"][0]["strTeam"]
yearFormedNYK = parseNYK["teams"][0]["intFormedYear"]
teamStadiumNYK = parseNYK["teams"][0]["strStadium"]
teamInfoNYK = parseNYK["teams"][0]["strDescriptionEN"]
lastGameDateNYK = LGparseNYK["results"][0]["dateEventLocal"]
homeTeamNYK = LGparseNYK["results"][0]["strHomeTeam"]
awayTeamNYK = LGparseNYK["results"][0]["strAwayTeam"]
homeScoreNYK = LGparseNYK["results"][0]["intHomeScore"]
awayScoreNYK = LGparseNYK["results"][0]["intAwayScore"]

# Last Game Info Printout KNICKS
knicksHome = "Home: " + str(homeTeamNYK) + " " + str(homeScoreNYK)
knicksAway = "Away: " + str(awayTeamNYK) + " " + str(awayScoreNYK)

knicksGame = lastGameDateNYK + """
""" + knicksHome + """
""" + knicksAway + ""

#######################################################################
# OKLAHOMA CITY THUNDER

# General Info for THUNDER 134887
thunderRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Oklahoma%20City%20Thunder")
# Last Game Info
thunderLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134887")
# Next Game Info
thunderNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134887")

# General Info Parsed for THUNDER 134887
dataOKC = thunderRE.text
parseOKC = json.loads(dataOKC)
# Last Game Info
LGdataOKC = thunderLG.text
LGparseOKC = json.loads(LGdataOKC)
# Next Game Info
NGdataOKC = thunderNG.text
NGparseOKC = json.loads(NGdataOKC)

# info Layout for the Drop Down Menu to Gather from THUNDER 134887
thunderTeam = parseOKC["teams"][0]["strTeam"]
yearFormedOKC = parseOKC["teams"][0]["intFormedYear"]
teamStadiumOKC = parseOKC["teams"][0]["strStadium"]
teamInfoOKC = parseOKC["teams"][0]["strDescriptionEN"]
lastGameDateOKC = LGparseOKC["results"][0]["dateEventLocal"]
homeTeamOKC = LGparseOKC["results"][0]["strHomeTeam"]
awayTeamOKC = LGparseOKC["results"][0]["strAwayTeam"]
homeScoreOKC = LGparseOKC["results"][0]["intHomeScore"]
awayScoreOKC = LGparseOKC["results"][0]["intAwayScore"]

# Last Game Info Printout KNICKS
thunderHome = "Home: " + str(homeTeamOKC) + " " + str(homeScoreOKC)
thunderAway = "Away: " + str(awayTeamOKC) + " " + str(awayScoreOKC)

thunderGame = lastGameDateOKC + """
""" + thunderHome + """
""" + thunderAway + ""

#######################################################################
# ORLANDO MAGIC

# General Info for MAGIC 134883
magicRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Orlando%20Magic")
# Last Game Info
magicLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134883")
# Next Game Info
magicNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134883")

# General Info Parsed MAGIC 134883
dataORL = magicRE.text
parseORL = json.loads(dataORL)
# Last Game Parsed
LGdataORL = magicLG.text
LGparseORL = json.loads(LGdataORL)
# Next Game Parsed
NGdataORL = magicNG.text
NGparseORL = json.loads(NGdataORL)

# info Layout for the Drop Down Menu to Gather from MAGIC 134883
magicTeam = parseORL["teams"][0]["strTeam"]
yearFormedORL = parseORL["teams"][0]["intFormedYear"]
teamStadiumORL = parseORL["teams"][0]["strStadium"]
teamInfoORL = parseORL["teams"][0]["strDescriptionEN"]
lastGameDateORL = LGparseORL["results"][0]["dateEventLocal"]
homeTeamORL = LGparseORL["results"][0]["strHomeTeam"]
awayTeamORL = LGparseORL["results"][0]["strAwayTeam"]
homeScoreORL = LGparseORL["results"][0]["intHomeScore"]
awayScoreORL = LGparseORL["results"][0]["intAwayScore"]

# Last Game Info Printout MAGIC
magicHome = "Home: " + str(homeTeamORL) + " " + str(homeScoreORL)
magicAway = "Away: " + str(awayTeamORL) + " " + str(awayScoreORL)

magicGame = lastGameDateOKC + """
""" + magicHome + """
""" + magicAway + ""

#######################################################################
# PHILADELPHIA 76ERS

# General Info for 76ERS 134863
sixersRE = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Philadelphia%2076ers")
# Last Game Info for 76ERS 134863
sixersLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134863")
# Next Game Info for 76ERS 134863
sixersNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134863")

# General Info Parsed 76ERS 134863
dataPHI = sixersRE.text
parsePHI = json.loads(dataPHI)
# Last Game Info Parsed
LGdataPHI = sixersLG.text
LGparsePHI = json.loads(LGdataPHI)
# Next Game Info Parsed
NGdataPHI = sixersNG.text
NGparsePHI = json.loads(NGdataPHI)

# info Layout for the Drop Down Menu to Gather from 76ERS 134863
sixersTeam = parsePHI["teams"][0]["strTeam"]
yearFormedPHI = parsePHI["teams"][0]["intFormedYear"]
teamStadiumPHI = parsePHI["teams"][0]["strStadium"]
teamInfoPHI = parsePHI["teams"][0]["strDescriptionEN"]
lastGameDatePHI = LGparsePHI["results"][0]["dateEventLocal"]
homeTeamPHI = LGparsePHI["results"][0]["strHomeTeam"]
awayTeamPHI = LGparsePHI["results"][0]["strAwayTeam"]
homeScorePHI = LGparsePHI["results"][0]["intHomeScore"]
awayScorePHI = LGparsePHI["results"][0]["intAwayScore"]

# Last Game Info Printout SIXERS
sixersHome = "Home: " + str(homeTeamPHI) + " " + str(homeScorePHI)
sixersAway = "Away: " + str(awayTeamPHI) + " " + str(awayScorePHI)

sixersGame = lastGameDatePHI + """
""" + sixersHome + """
""" + sixersAway + ""

# print(sixersRE.status_code)  # Pull a status code on the actual REQUEST

#######################################################################
# PHOENIX SUNS

# General Info for SUNS 134868
sunsRE = requests.get("https://thesportsdb.com/api/v1/json/1/searchteams.php?t=Phoenix%20Suns")
# Last Game Info for SUNS 134868
sunsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134868")
# Next Game Info
sunsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventsnext.php?id=134868")

# General Info Parsed
dataPHO = sunsRE.text
parsePHO = json.loads(dataPHO)
# Last Game Parsed
LGdataPHO = sunsLG.text
LGparsePHO = json.loads(LGdataPHO)
# Next Game Parsed
NGdataPHO = sunsNG.text
NGparsePHO = json.loads(NGdataPHO)

# info Layout for the Drop Down Menu to Gather from 76ERS 134863
sunsTeam = parsePHO["teams"][0]["strTeam"]
yearFormedPHO = parsePHO["teams"][0]["intFormedYear"]
teamStadiumPHO = parsePHO["teams"][0]["strStadium"]
teamInfoPHO = parsePHO["teams"][0]["strDescriptionEN"]
lastGameDatePHO = LGparsePHO["results"][0]["dateEventLocal"]
homeTeamPHO = LGparsePHO["results"][0]["strHomeTeam"]
awayTeamPHO = LGparsePHO["results"][0]["strAwayTeam"]
homeScorePHO = LGparsePHO["results"][0]["intHomeScore"]
awayScorePHO = LGparsePHO["results"][0]["intAwayScore"]

# Last Game Info Printout SUNS
sunsHome = "Home: " + str(homeTeamPHO) + " " + str(homeScorePHO)
sunsAway = "Away: " + str(awayTeamPHO) + " " + str(awayScorePHO)

sunsGame = lastGameDatePHO + """
""" + sunsHome + """
""" + sunsAway + ""

#######################################################################
# PORTLAND TRAIL BLAZERS 134888

# General Info for BLAZERS
blazersRE = requests.get("https://thesportsdb.com/api/v1/json/1/searchteams.php?t=Portland%20Trail%20Blazers")
# Last Game Info for BLAZERS 134888
blazersLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134888")
# Next Game Info for BLAZERS 134888
blazersNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134888")

# General Info Parsed
dataPOR = blazersRE.text
parsePOR = json.loads(dataPOR)
# Last Game Parsed
LGdataPOR = blazersLG.text
LGparsePOR = json.loads(LGdataPOR)
# Next Game Parsed
NGdataPOR = blazersNG.text
NGparsePOR = json.loads(NGdataPOR)

# info Layout for the Drop Down Menu to Gather from 76ERS 134863
blazersTeam = parsePOR["teams"][0]["strTeam"]
yearFormedPOR = parsePOR["teams"][0]["intFormedYear"]
teamStadiumPOR = parsePOR["teams"][0]["strStadium"]
teamInfoPOR = parsePOR["teams"][0]["strDescriptionEN"]
lastGameDatePOR = LGparsePOR["results"][0]["dateEventLocal"]
homeTeamPOR = LGparsePOR["results"][0]["strHomeTeam"]
awayTeamPOR = LGparsePOR["results"][0]["strAwayTeam"]
homeScorePOR = LGparsePOR["results"][0]["intHomeScore"]
awayScorePOR = LGparsePOR["results"][0]["intAwayScore"]

# Last Game Info Printout SUNS
blazersHome = "Home: " + str(homeTeamPOR) + " " + str(homeScorePOR)
blazersAway = "Away: " + str(awayTeamPOR) + " " + str(awayScorePOR)

blazersGame = lastGameDatePOR + """
""" + blazersHome + """
""" + blazersAway + ""

#######################################################################
# SACRAMENTO KINGS

# General Info for KINGS 134869
kingsRE = requests.get("https://thesportsdb.com/api/v1/json/1/searchteams.php?t=Sacramento%20Kings")
# Last Game Info
kingsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134869")
# Next Game Info
kingsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134869")

# General Info Parsed
dataSAC = kingsRE.text
parseSAC = json.loads(dataSAC)
# Last Game Parsed
LGdataSAC = kingsLG.text
LGparseSAC = json.loads(LGdataSAC)
# Next Game Parsed
NGdataSAC = kingsNG.text
NGparseSAC = json.loads(NGdataSAC)

# info Layout for the Drop Down Menu to Gather from 76ERS 134863
kingsTeam = parseSAC["teams"][0]["strTeam"]
yearFormedSAC = parseSAC["teams"][0]["intFormedYear"]
teamStadiumSAC = parseSAC["teams"][0]["strStadium"]
teamInfoSAC = parseSAC["teams"][0]["strDescriptionEN"]
lastGameDateSAC = LGparseSAC["results"][0]["dateEventLocal"]
homeTeamSAC = LGparseSAC["results"][0]["strHomeTeam"]
awayTeamSAC = LGparseSAC["results"][0]["strAwayTeam"]
homeScoreSAC = LGparseSAC["results"][0]["intHomeScore"]
awayScoreSAC = LGparseSAC["results"][0]["intAwayScore"]

# Last Game Info Printout SUNS
kingsHome = "Home: " + str(homeTeamSAC) + " " + str(homeScoreSAC)
kingsAway = "Away: " + str(awayTeamSAC) + " " + str(awayScoreSAC)

kingsGame = lastGameDateSAC + """
""" + kingsHome + """
""" + kingsAway + ""

#######################################################################
# SAN ANTONIO SPURS

# General Info for SPURS 134879
spursRE = requests.get("https://thesportsdb.com/api/v1/json/1/searchteams.php?t=San%20Antonio%20Spurs")
# Last Game Info
spursLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134879")
# Next Game Info
spursNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134879")

# General Info Parsed
dataSAN = spursRE.text
parseSAN = json.loads(dataSAN)
# Last Game Parsed
LGdataSAN = spursLG.text
LGparseSAN = json.loads(LGdataSAN)
# Next Game Parsed
NGdataSAN = spursNG.text
NGparseSAN = json.loads(NGdataSAN)

# info Layout for the Drop Down Menu to Gather from SPURS 134879
spursTeam = parseSAN["teams"][0]["strTeam"]
yearFormedSAN = parseSAN["teams"][0]["intFormedYear"]
teamStadiumSAN = parseSAN["teams"][0]["strStadium"]
teamInfoSAN = parseSAN["teams"][0]["strDescriptionEN"]
lastGameDateSAN = LGparseSAN["results"][0]["dateEventLocal"]
homeTeamSAN = LGparseSAN["results"][0]["strHomeTeam"]
awayTeamSAN = LGparseSAN["results"][0]["strAwayTeam"]
homeScoreSAN = LGparseSAN["results"][0]["intHomeScore"]
awayScoreSAN = LGparseSAN["results"][0]["intAwayScore"]

# Last Game Info Printout SPURS
spursHome = "Home: " + str(homeTeamSAN) + " " + str(homeScoreSAN)
spursAway = "Away: " + str(awayTeamSAN) + " " + str(awayScoreSAN)

spursGame = lastGameDateSAN + """
""" + spursHome + """
""" + spursAway + ""

#######################################################################
# TORONTO RAPTORS

# General Info on RAPTORS 134864
raptorsRE = requests.get("https://thesportsdb.com/api/v1/json/1/searchteams.php?t=Toronto%20Raptors")
# Last Game Info
raptorsLG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134864")
# Next Game Info
raptorsNG = requests.get("https://www.thesportsdb.com/api/v1/json/4013017/eventslast.php?id=134864")

# General Info Parsed
dataTOR = raptorsRE.text
parseTOR = json.loads(dataTOR)
# Last Game Parsed
LGdataTOR = raptorsLG.text
LGparseTOR = json.loads(LGdataTOR)
# Next Game Parsed
NGdataTOR = raptorsNG.text
NGparseTOR = json.loads(NGdataTOR)

# info Layout for the Drop Down Menu to Gather from RAPTORS 134864
raptorsTeam = parseTOR["teams"][0]["strTeam"]
yearFormedTOR = parseTOR["teams"][0]["intFormedYear"]
teamStadiumTOR = parseTOR["teams"][0]["strStadium"]
teamInfoTOR = parseTOR["teams"][0]["strDescriptionEN"]
lastGameDateTOR = LGparseTOR["results"][0]["dateEventLocal"]
homeTeamTOR = LGparseTOR["results"][0]["strHomeTeam"]
awayTeamTOR = LGparseTOR["results"][0]["strAwayTeam"]
homeScoreTOR = LGparseTOR["results"][0]["intHomeScore"]
awayScoreTOR = LGparseTOR["results"][0]["intAwayScore"]

# Last Game Info Printout RAPTORS
raptorsHome = "Home: " + str(homeTeamTOR) + " " + str(homeScoreTOR)
raptorsAway = "Away: " + str(awayTeamTOR) + " " + str(awayScoreTOR)

raptorsGame = lastGameDateTOR + """
""" + spursHome + """
""" + spursAway + ""

#######################################################################


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
    if TeamsVar.get() == "Chicago Bulls":
        teamSelectedOutput.delete(0.0, 'end')
        selectCHI = bullsTeam
        teamSelectedOutput.insert(INSERT, selectCHI)
    if TeamsVar.get() == "Cleveland Cavaliers":
        teamSelectedOutput.delete(0.0, 'end')
        selectCLE = cavsTeam
        teamSelectedOutput.insert(INSERT, selectCLE)
    if TeamsVar.get() == "Dallas Mavericks":
        teamSelectedOutput.delete(0.0, 'end')
        selectDAL = mavsTeam
        teamSelectedOutput.insert(INSERT, selectDAL)
    if TeamsVar.get() == "Denver Nuggets":
        teamSelectedOutput.delete(0.0, 'end')
        selectDEN = nuggetsTeam
        teamSelectedOutput.insert(INSERT, selectDEN)
    if TeamsVar.get() == "Detroit Pistons":
        teamSelectedOutput.delete(0.0, 'end')
        selectDET = pistonsTeam
        teamSelectedOutput.insert(INSERT, selectDET)
    if TeamsVar.get() == "Golden State Warriors":
        teamSelectedOutput.delete(0.0, 'end')
        selectGS = warriorsTeam
        teamSelectedOutput.insert(INSERT, selectGS)
    if TeamsVar.get() == "Houston Rockets":
        teamSelectedOutput.delete(0.0, 'end')
        selectHOU = rocketsTeam
        teamSelectedOutput.insert(INSERT, selectHOU)
    if TeamsVar.get() == "Indiana Pacers":
        teamSelectedOutput.delete(0.0, 'end')
        selectIND = pacersTeam
        teamSelectedOutput.insert(INSERT, selectIND)
    if TeamsVar.get() == "Los Angeles Lakers":
        teamSelectedOutput.delete(0.0, 'end')
        selectLAL = lakersTeam
        teamSelectedOutput.insert(INSERT, selectLAL)
    if TeamsVar.get() == "Los Angeles Clippers":
        teamSelectedOutput.delete(0.0, 'end')
        selectLAC = clippersTeam
        teamSelectedOutput.insert(INSERT, selectLAC)
    if TeamsVar.get() == "Memphis Grizzlies":
        teamSelectedOutput.delete(0.0, 'end')
        selectMEM = grizzTeam
        teamSelectedOutput.insert(INSERT, selectMEM)
    if TeamsVar.get() == "Miami Heat":
        teamSelectedOutput.delete(0.0, 'end')
        selectMIA = heatTeam
        teamSelectedOutput.insert(INSERT, selectMIA)
    if TeamsVar.get() == "Milwaukee Bucks":
        teamSelectedOutput.delete(0.0, 'end')
        selectMIL = bucksTeam
        teamSelectedOutput.insert(INSERT, selectMIL)
    if TeamsVar.get() == "Minnesota Timberwolves":
        teamSelectedOutput.delete(0.0, 'end')
        selectMIN = twolvesTeam
        teamSelectedOutput.insert(INSERT, selectMIN)
    if TeamsVar.get() == "New Orleans Pelicans":
        teamSelectedOutput.delete(0.0, 'end')
        selectNOLA = pelicansTeam
        teamSelectedOutput.insert(INSERT, selectNOLA)
    if TeamsVar.get() == "New York Knicks":
        teamSelectedOutput.delete(0.0, 'end')
        selectNYK = knicksTeam
        teamSelectedOutput.insert(INSERT, selectNYK)
    if TeamsVar.get() == "Oklahoma City Thunder":
        teamSelectedOutput.delete(0.0, 'end')
        selectOKC = thunderTeam
        teamSelectedOutput.insert(INSERT, selectOKC)
    if TeamsVar.get() == "Orlando Magic":
        teamSelectedOutput.delete(0.0, 'end')
        selectORL = magicTeam
        teamSelectedOutput.insert(INSERT, selectORL)
    if TeamsVar.get() == "Philadelphia 76ers":
        teamSelectedOutput.delete(0.0, 'end')
        selectPHI = sixersTeam
        teamSelectedOutput.insert(INSERT, selectPHI)
    if TeamsVar.get() == "Phoenix Suns":
        teamSelectedOutput.delete(0.0, 'end')
        selectPHO = sunsTeam
        teamSelectedOutput.insert(INSERT, selectPHO)
    if TeamsVar.get() == "Portland Trail Blazers":
        teamSelectedOutput.delete(0.0, 'end')
        selectPOR = blazersTeam
        teamSelectedOutput.insert(INSERT, selectPOR)
    if TeamsVar.get() == "Sacramento Kings":
        teamSelectedOutput.delete(0.0, 'end')
        selectSAC = kingsTeam
        teamSelectedOutput.insert(INSERT, selectSAC)
    if TeamsVar.get() == "San Antonio Spurs":
        teamSelectedOutput.delete(0.0, 'end')
        selectSAN = spursTeam
        teamSelectedOutput.insert(INSERT, selectSAN)


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
    if TeamsVar.get() == "Chicago Bulls":
        yearFormOutput.delete(0.0, 'end')
        yearCHI = yearFormedCHI
        yearFormOutput.insert(INSERT, yearCHI)
    if TeamsVar.get() == "Cleveland Cavaliers":
        yearFormOutput.delete(0.0, 'end')
        yearCLE = yearFormedCLE
        yearFormOutput.insert(INSERT, yearCLE)
    if TeamsVar.get() == "Dallas Mavericks":
        yearFormOutput.delete(0.0, 'end')
        yearDAL = yearFormedDAL
        yearFormOutput.insert(INSERT, yearDAL)
    if TeamsVar.get() == "Denver Nuggets":
        yearFormOutput.delete(0.0, 'end')
        yearDEN = yearFormedDEN
        yearFormOutput.insert(INSERT, yearDEN)
    if TeamsVar.get() == "Detroit Pistons":
        yearFormOutput.delete(0.0, 'end')
        yearDET = yearFormedDET
        yearFormOutput.insert(INSERT, yearDET)
    if TeamsVar.get() == "Golden State Warriors":
        yearFormOutput.delete(0.0, 'end')
        yearGS = yearFormedGS
        yearFormOutput.insert(INSERT, yearGS)
    if TeamsVar.get() == "Houston Rockets":
        yearFormOutput.delete(0.0, 'end')
        yearHOU = yearFormedHOU
        yearFormOutput.insert(INSERT, yearHOU)
    if TeamsVar.get() == "Indiana Pacers":
        yearFormOutput.delete(0.0, 'end')
        yearIND = yearFormedIND
        yearFormOutput.insert(INSERT, yearIND)
    if TeamsVar.get() == "Los Angeles Lakers":
        yearFormOutput.delete(0.0, 'end')
        yearLAL = yearFormedLAL
        yearFormOutput.insert(INSERT, yearLAL)
    if TeamsVar.get() == "Los Angeles Clippers":
        yearFormOutput.delete(0.0, 'end')
        yearLAC = yearFormedLAC
        yearFormOutput.insert(INSERT, yearLAC)
    if TeamsVar.get() == "Memphis Grizzlies":
        yearFormOutput.delete(0.0, 'end')
        yearMEM = yearFormedMEM
        yearFormOutput.insert(INSERT, yearMEM)
    if TeamsVar.get() == "Miami Heat":
        yearFormOutput.delete(0.0, 'end')
        yearMIA = yearFormedMIA
        yearFormOutput.insert(INSERT, yearMIA)
    if TeamsVar.get() == "Milwaukee Bucks":
        yearFormOutput.delete(0.0, 'end')
        yearMIL = yearFormedMIL
        yearFormOutput.insert(INSERT, yearMIL)
    if TeamsVar.get() == "Minnesota Timberwolves":
        yearFormOutput.delete(0.0, 'end')
        yearMIN = yearFormedMIN
        yearFormOutput.insert(INSERT, yearMIN)
    if TeamsVar.get() == "New Orleans Pelicans":
        yearFormOutput.delete(0.0, 'end')
        yearNOLA = yearFormedNOLA
        yearFormOutput.insert(INSERT, yearNOLA)
    if TeamsVar.get() == "New York Knicks":
        yearFormOutput.delete(0.0, 'end')
        yearNYK = yearFormedNYK
        yearFormOutput.insert(INSERT, yearNYK)
    if TeamsVar.get() == "Oklahoma City Thunder":
        yearFormOutput.delete(0.0, 'end')
        yearOKC = yearFormedOKC
        yearFormOutput.insert(INSERT, yearOKC)
    if TeamsVar.get() == "Orlando Magic":
        yearFormOutput.delete(0.0, 'end')
        yearORL = yearFormedORL
        yearFormOutput.insert(INSERT, yearORL)
    if TeamsVar.get() == "Philadelphia 76ers":
        yearFormOutput.delete(0.0, 'end')
        yearPHI = yearFormedPHI
        yearFormOutput.insert(INSERT, yearPHI)
    if TeamsVar.get() == "Phoenix Suns":
        yearFormOutput.delete(0.0, 'end')
        yearPHO = yearFormedPHO
        yearFormOutput.insert(INSERT, yearPHO)
    if TeamsVar.get() == "Portland Trail Blazers":
        yearFormOutput.delete(0.0, 'end')
        yearPOR = yearFormedPOR
        yearFormOutput.insert(INSERT, yearPOR)
    if TeamsVar.get() == "Sacramento Kings":
        yearFormOutput.delete(0.0, 'end')
        yearSAC = yearFormedSAC
        yearFormOutput.insert(INSERT, yearSAC)
    if TeamsVar.get() == "San Antonio Spurs":
        yearFormOutput.delete(0.0, 'end')
        yearSAN = yearFormedSAN
        yearFormOutput.insert(INSERT, yearSAN)


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
    if TeamsVar.get() == "Chicago Bulls":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumCHI = teamStadiumCHI
        teamStadiumOutput.insert(INSERT, stadiumCHI)
    if TeamsVar.get() == "Cleveland Cavaliers":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumCLE = teamStadiumCLE
        teamStadiumOutput.insert(INSERT, stadiumCLE)
    if TeamsVar.get() == "Dallas Mavericks":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumDAL = teamStadiumDAL
        teamStadiumOutput.insert(INSERT, stadiumDAL)
    if TeamsVar.get() == "Denver Nuggets":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumDEN = teamStadiumDEN
        teamStadiumOutput.insert(INSERT, stadiumDEN)
    if TeamsVar.get() == "Detroit Pistons":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumDET = teamStadiumDET
        teamStadiumOutput.insert(INSERT, stadiumDET)
    if TeamsVar.get() == "Golden State Warriors":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumGS = teamStadiumGS
        teamStadiumOutput.insert(INSERT, stadiumGS)
    if TeamsVar.get() == "Houston Rockets":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumHOU = teamStadiumHOU
        teamStadiumOutput.insert(INSERT, stadiumHOU)
    if TeamsVar.get() == "Indiana Pacers":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumIND = teamStadiumIND
        teamStadiumOutput.insert(INSERT, stadiumIND)
    if TeamsVar.get() == "Los Angeles Lakers":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumLAL = teamStadiumLAL
        teamStadiumOutput.insert(INSERT, stadiumLAL)
    if TeamsVar.get() == "Los Angeles Clippers":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumLAC = teamStadiumLAC
        teamStadiumOutput.insert(INSERT, stadiumLAC)
    if TeamsVar.get() == "Memphis Grizzlies":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumMEM = teamStadiumMEM
        teamStadiumOutput.insert(INSERT, stadiumMEM)
    if TeamsVar.get() == "Miami Heat":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumMIA = teamStadiumMIA
        teamStadiumOutput.insert(INSERT, stadiumMIA)
    if TeamsVar.get() == "Milwaukee Bucks":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumMIL = teamStadiumMIL
        teamStadiumOutput.insert(INSERT, stadiumMIL)
    if TeamsVar.get() == "Minnesota Timberwolves":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumMIN = teamStadiumMIN
        teamStadiumOutput.insert(INSERT, stadiumMIN)
    if TeamsVar.get() == "New Orleans Pelicans":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumNOLA = teamStadiumNOLA
        teamStadiumOutput.insert(INSERT, stadiumNOLA)
    if TeamsVar.get() == "New York Knicks":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumNYK = teamStadiumNYK
        teamStadiumOutput.insert(INSERT, stadiumNYK)
    if TeamsVar.get() == "Oklahoma City Thunder":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumOKC = teamStadiumOKC
        teamStadiumOutput.insert(INSERT, stadiumOKC)
    if TeamsVar.get() == "Orlando Magic":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumORL = teamStadiumORL
        teamStadiumOutput.insert(INSERT, stadiumORL)
    if TeamsVar.get() == "Philadelphia 76ers":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumPHI = teamStadiumPHI
        teamStadiumOutput.insert(INSERT, stadiumPHI)
    if TeamsVar.get() == "Phoenix Suns":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumPHO = teamStadiumPHO
        teamStadiumOutput.insert(INSERT, stadiumPHO)
    if TeamsVar.get() == "Portland Trail Blazers":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumPOR = teamStadiumPOR
        teamStadiumOutput.insert(INSERT, stadiumPOR)
    if TeamsVar.get() == "Sacramento Kings":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumSAC = teamStadiumSAC
        teamStadiumOutput.insert(INSERT, stadiumSAC)
    if TeamsVar.get() == "San Antonio Spurs":
        teamStadiumOutput.delete(0.0, 'end')
        stadiumSAN = teamStadiumSAN
        teamStadiumOutput.insert(INSERT, stadiumSAN)


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
    if TeamsVar.get() == "Chicago Bulls":
        teamInfoOutput.delete(0.0, 'end')
        infoCHI = teamInfoCHI
        teamInfoOutput.insert(INSERT, infoCHI)
    if TeamsVar.get() == "Cleveland Cavaliers":
        teamInfoOutput.delete(0.0, 'end')
        infoCLE = teamInfoCLE
        teamInfoOutput.insert(INSERT, infoCLE)
    if TeamsVar.get() == "Dallas Mavericks":
        teamInfoOutput.delete(0.0, 'end')
        infoDAL = teamInfoDAL
        teamInfoOutput.insert(INSERT, infoDAL)
    if TeamsVar.get() == "Detroit Pistons":
        teamInfoOutput.delete(0.0, 'end')
        infoDET = teamInfoDET
        teamInfoOutput.insert(INSERT, infoDET)
    if TeamsVar.get() == "Denver Nuggets":
        teamInfoOutput.delete(0.0, 'end')
        infoDEN = teamInfoDEN
        teamInfoOutput.insert(INSERT, infoDEN)
    if TeamsVar.get() == "Golden State Warriors":
        teamInfoOutput.delete(0.0, 'end')
        infoGS = teamInfoGS
        teamInfoOutput.insert(INSERT, infoGS)
    if TeamsVar.get() == "Houston Rockets":
        teamInfoOutput.delete(0.0, 'end')
        infoHOU = teamInfoHOU
        teamInfoOutput.insert(INSERT, infoHOU)
    if TeamsVar.get() == "Indiana Pacers":
        teamInfoOutput.delete(0.0, 'end')
        infoIND = teamInfoIND
        teamInfoOutput.insert(INSERT, infoIND)
    if TeamsVar.get() == "Los Angeles Lakers":
        teamInfoOutput.delete(0.0, 'end')
        infoLAL = teamInfoLAL
        teamInfoOutput.insert(INSERT, infoLAL)
    if TeamsVar.get() == "Los Angeles Clippers":
        teamInfoOutput.delete(0.0, 'end')
        infoLAC = teamInfoLAC
        teamInfoOutput.insert(INSERT, infoLAC)
    if TeamsVar.get() == "Memphis Grizzlies":
        teamInfoOutput.delete(0.0, 'end')
        infoMEM = teamInfoMEM
        teamInfoOutput.insert(INSERT, infoMEM)
    if TeamsVar.get() == "Miami Heat":
        teamInfoOutput.delete(0.0, 'end')
        infoMIA = teamInfoMIA
        teamInfoOutput.insert(INSERT, infoMIA)
    if TeamsVar.get() == "Milwaukee Bucks":
        teamInfoOutput.delete(0.0, 'end')
        infoMIL = teamInfoMIL
        teamInfoOutput.insert(INSERT, infoMIL)
    if TeamsVar.get() == "Minnesota Timberwolves":
        teamInfoOutput.delete(0.0, 'end')
        infoMIN = teamInfoMIN
        teamInfoOutput.insert(INSERT, infoMIN)
    if TeamsVar.get() == "New Orleans Pelicans":
        teamInfoOutput.delete(0.0, 'end')
        infoNOLA = teamInfoNOLA
        teamInfoOutput.insert(INSERT, infoNOLA)
    if TeamsVar.get() == "New York Knicks":
        teamInfoOutput.delete(0.0, 'end')
        infoNYK = teamInfoNYK
        teamInfoOutput.insert(INSERT, infoNYK)
    if TeamsVar.get() == "Oklahoma City Thunder":
        teamInfoOutput.delete(0.0, 'end')
        infoOKC = teamInfoOKC
        teamInfoOutput.insert(INSERT, infoOKC)
    if TeamsVar.get() == "Orlando Magic":
        teamInfoOutput.delete(0.0, 'end')
        infoORL = teamInfoORL
        teamInfoOutput.insert(INSERT, infoORL)
    if TeamsVar.get() == "Philadelphia 76ers":
        teamInfoOutput.delete(0.0, 'end')
        infoPHI = teamInfoPHI
        teamInfoOutput.insert(INSERT, infoPHI)
    if TeamsVar.get() == "Phoenix Suns":
        teamInfoOutput.delete(0.0, 'end')
        infoPHO = teamInfoPHO
        teamInfoOutput.insert(INSERT, infoPHO)
    if TeamsVar.get() == "Portland Trail Blazers":
        teamInfoOutput.delete(0.0, 'end')
        infoPOR = teamInfoPOR
        teamInfoOutput.insert(INSERT, infoPOR)
    if TeamsVar.get() == "Sacramento Kings":
        teamInfoOutput.delete(0.0, 'end')
        infoSAC = teamInfoSAC
        teamInfoOutput.insert(INSERT, infoSAC)
    if TeamsVar.get() == "San Antonio Spurs":
        teamInfoOutput.delete(0.0, 'end')
        infoSAN = teamInfoSAN
        teamInfoOutput.insert(INSERT, infoSAN)


# Last Game Populate
def callLastGame(*args):
    if TeamsVar.get() == "Atlanta Hawks":
        lastGameOutput.delete(0.0, 'end')  # Delete Clears the way for the incoming information
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
    if TeamsVar.get() == "Chicago Bulls":
        lastGameOutput.delete(0.0, 'end')
        bullsLastGame = bullsGame
        lastGameOutput.insert(INSERT, bullsLastGame)
    if TeamsVar.get() == "Cleveland Cavaliers":
        lastGameOutput.delete(0.0, 'end')
        cavsLastGame = cavsGame
        lastGameOutput.insert(INSERT, cavsLastGame)
    if TeamsVar.get() == "Dallas Mavericks":
        lastGameOutput.delete(0.0, 'end')
        mavsLastGame = mavsGame
        lastGameOutput.insert(INSERT, mavsLastGame)
    if TeamsVar.get() == "Denver Nuggets":
        lastGameOutput.delete(0.0, 'end')
        nuggetsLastGame = nuggetsGame
        lastGameOutput.insert(INSERT, nuggetsLastGame)
    if TeamsVar.get() == "Detroit Pistons":
        lastGameOutput.delete(0.0, 'end')
        pistonsLastGame = pistonsGame
        lastGameOutput.insert(INSERT, pistonsLastGame)
    if TeamsVar.get() == "Golden State Warriors":
        lastGameOutput.delete(0.0, 'end')
        warriorsLastGame = warriorsGame
        lastGameOutput.insert(INSERT, warriorsLastGame)
    if TeamsVar.get() == "Houston Rockets":
        lastGameOutput.delete(0.0, 'end')
        rocketsLastGame = rocketsGame
        lastGameOutput.insert(INSERT, rocketsLastGame)
    if TeamsVar.get() == "Indiana Pacers":
        lastGameOutput.delete(0.0, 'end')
        pacersLastGame = pacersGame
        lastGameOutput.insert(INSERT, pacersLastGame)
    if TeamsVar.get() == "Los Angeles Lakers":
        lastGameOutput.delete(0.0, 'end')
        lakersLastGame = lakersGame
        lastGameOutput.insert(INSERT, lakersLastGame)
    if TeamsVar.get() == "Los Angeles Clippers":
        lastGameOutput.delete(0.0, 'end')
        clippersLastGame = clippersGame
        lastGameOutput.insert(INSERT, clippersLastGame)
    if TeamsVar.get() == "Memphis Grizzlies":
        lastGameOutput.delete(0.0, 'end')
        grizzLastGame = grizzGame
        lastGameOutput.insert(INSERT, grizzLastGame)
    if TeamsVar.get() == "Miami Heat":
        lastGameOutput.delete(0.0, 'end')
        heatLastGame = heatGame
        lastGameOutput.insert(INSERT, heatLastGame)
    if TeamsVar.get() == "Milwaukee Bucks":
        lastGameOutput.delete(0.0, 'end')
        bucksLastGame = bucksGame
        lastGameOutput.insert(INSERT, bucksLastGame)
    if TeamsVar.get() == "Minnesota Timberwolves":
        lastGameOutput.delete(0.0, 'end')
        twolvesLastGame = twolvesGame
        lastGameOutput.insert(INSERT, twolvesLastGame)
    if TeamsVar.get() == "New Orleans Pelicans":
        lastGameOutput.delete(0.0, 'end')
        pelicansLastGame = pelicansGame
        lastGameOutput.insert(INSERT, pelicansLastGame)
    if TeamsVar.get() == "New York Knicks":
        lastGameOutput.delete(0.0, 'end')
        knicksLastGame = knicksGame
        lastGameOutput.insert(INSERT, knicksLastGame)
    if TeamsVar.get() == "Oklahoma City Thunder":
        lastGameOutput.delete(0.0, 'end')
        thunderLastGame = thunderGame
        lastGameOutput.insert(INSERT, thunderLastGame)
    if TeamsVar.get() == "Orlando Magic":
        lastGameOutput.delete(0.0, 'end')
        magicLastGame = magicGame
        lastGameOutput.insert(INSERT, magicLastGame)
    if TeamsVar.get() == "Philadelphia 76ers":
        lastGameOutput.delete(0.0, 'end')
        sixersLastGame = sixersGame
        lastGameOutput.insert(INSERT, sixersLastGame)
    if TeamsVar.get() == "Phoenix Suns":
        lastGameOutput.delete(0.0, 'end')
        sunsLastGame = sunsGame
        lastGameOutput.insert(INSERT, sunsLastGame)
    if TeamsVar.get() == "Portland Trail Blazers":
        lastGameOutput.delete(0.0, 'end')
        blazersLastGame = blazersGame
        lastGameOutput.insert(INSERT, blazersLastGame)
    if TeamsVar.get() == "Sacramento Kings":
        lastGameOutput.delete(0.0, 'end')
        kingsLastGame = kingsGame
        lastGameOutput.insert(INSERT, kingsLastGame)
    if TeamsVar.get() == "San Antonio Spurs":
        lastGameOutput.delete(0.0, 'end')
        spursLastGame = spursGame
        lastGameOutput.insert(INSERT, spursLastGame)


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


###############################################################
# TKINTER DOMAIN

# HEADER
logo = PhotoImage(file='icons/nbaCLEAR.png')
logoNBA = Label(app, image=logo, bg="DarkBlue")
resizNBAlogo = logo.subsample(1, 1)
logoNBA.config(image=resizNBAlogo)
logoNBA.pack()

# Drop Down Menu
droplist = OptionMenu(app, TeamsVar, *TeamsList)
droplist.config(width=40, height=1, fg='Blue')
droplist.pack()

# Team Selected
teamSelected = Label(app, text="Team Selected", bg='DarkBlue', fg='White', font='Arial 10 bold')
teamSelected.pack()
teamSelectedOutput = Text(app, width=30, height=2, bg='Black', fg='White', font='none 15')
teamSelectedOutput.pack()

# Year Formed
yearForm = Label(app, text="Year Formed", bg='DarkBlue', fg='White', font='Arial 10 bold')
yearForm.pack()
yearFormOutput = Text(app, width=20, height=2, bg='Black', fg='White', font='none 15')
yearFormOutput.pack()

# Team Stadium
teamStadium = Label(app, text="Team Stadium", bg='DarkBlue', fg='White', font='Arial 10 bold')
teamStadium.pack()
teamStadiumOutput = Text(app, width=50, height=2, bg='Black', fg='White', font='none 15')
teamStadiumOutput.pack()

# Team Info
teamInfo = Label(app, text="Team History", bg='DarkBlue', fg='White', font='Arial 10 bold')
teamInfo.pack()
teamInfoOutput = Text(app, width=150, height=4, bg='Black', fg='White', font='none 15')
teamInfoOutput.pack()

# Last Game Info
lastGame = Label(app, text="Last Game Played", bg='DarkBlue', fg='White', font='Arial 10 bold')
lastGame.pack()
lastGameOutput = Text(app, width=40, height=5, bg='Black', fg='White', font='none 15')
lastGameOutput.pack()

# Win or Loss
outcome = Label(app, text="Win or Loss", bg="DarkBlue", fg='White', font='Arial 10 bold')
outcome.pack()
outcomeOut = Text(app, width=20, height=1, bg='Black', fg='White', font='none 15')
outcomeOut.pack()

#################################################################################################
# LOGO TERRITORY

# Logo Canvas
LogoCanvas = Canvas(height=150, width=150, borderwidth=0, highlightthickness=0, bg='Darkblue', bd=0)
LogoCanvas.pack()


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
        LogoCanvas.delete("all")
        LogoCanvas.image = netsLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=netsLogo)
    if TeamsVar.get() == "Charlotte Hornets":
        hornetsLogo = PhotoImage(file="icons/Hornets1001.png")
        LogoCanvas.delete("all")
        LogoCanvas.image = hornetsLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=hornetsLogo)
    if TeamsVar.get() == "Chicago Bulls":
        bullsLogo = PhotoImage(file="icons/Bulls2001.png")
        LogoCanvas.delete("all")
        LogoCanvas.image = bullsLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=bullsLogo)
    if TeamsVar.get() == "Cleveland Cavaliers":
        LogoCanvas.delete("all")
        cavsLogo = PhotoImage(file="icons/Cavs2002.png")
        LogoCanvas.image = cavsLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=cavsLogo)
    if TeamsVar.get() == "Dallas Mavericks":
        LogoCanvas.delete("all")
        mavsLogo = PhotoImage(file="icons/Mavs3001.png")
        LogoCanvas.image = mavsLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=mavsLogo)
    if TeamsVar.get() == "Denver Nuggets":
        LogoCanvas.delete("all")
        nuggetsLogo = PhotoImage(file="icons/Nuggets2001.png")
        LogoCanvas.image = nuggetsLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=nuggetsLogo)
    if TeamsVar.get() == "Detroit Pistons":
        LogoCanvas.delete("all")
        pistonsLogo = PhotoImage(file='icons/Pistons1001.png')
        LogoCanvas.image = pistonsLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=pistonsLogo)
        LogoCanvas.pack()
    if TeamsVar.get() == "Golden State Warriors":
        LogoCanvas.delete("all")
        warriorsLogo = PhotoImage(file="icons/Warriors2001.png")
        LogoCanvas.image = warriorsLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=warriorsLogo)
        LogoCanvas.pack()
    if TeamsVar.get() == "Houston Rockets":
        LogoCanvas.delete("all")
        rocketsLogo = PhotoImage(file="icons/Rockets3001.png")
        LogoCanvas.image = rocketsLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=rocketsLogo)
    if TeamsVar.get() == "Indiana Pacers":
        LogoCanvas.delete("all")
        pacersLogo = PhotoImage(file="icons/Pacers1001.png")
        LogoCanvas.image = pacersLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=pacersLogo)
    if TeamsVar.get() == "Los Angeles Lakers":
        LogoCanvas.delete("all")
        lakersLogo = PhotoImage(file='icons/Lakers1001.png')
        LogoCanvas.image = lakersLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=lakersLogo)
        LogoCanvas.pack()
    if TeamsVar.get() == "Los Angeles Clippers":
        LogoCanvas.delete("all")
        clippersLogo = PhotoImage(file="icons/Clippers1001.png")
        LogoCanvas.image = clippersLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=clippersLogo)
    if TeamsVar.get() == "Memphis Grizzlies":
        LogoCanvas.delete("all")
        grizzLogo = PhotoImage(file="icons/Grizzlies1001.png")
        LogoCanvas.image = grizzLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=grizzLogo)
    if TeamsVar.get() == "Miami Heat":
        LogoCanvas.delete("all")
        heatLogo = PhotoImage(file="icons/Heat3001.png")
        LogoCanvas.image = heatLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=heatLogo)
    if TeamsVar.get() == "Milwaukee Bucks":
        LogoCanvas.delete("all")
        bucksLogo = PhotoImage(file='icons/Bucks2001.png')
        LogoCanvas.image = bucksLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=bucksLogo)
        LogoCanvas.pack()
    if TeamsVar.get() == "Minnesota Timberwolves":
        LogoCanvas.delete("all")
        twolvesLogo = PhotoImage(file="icons/Twolves2001.png")
        LogoCanvas.image = twolvesLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=twolvesLogo)
        LogoCanvas.pack()
    if TeamsVar.get() == "New Orleans Pelicans":
        LogoCanvas.delete("all")
        pelicansLogo = PhotoImage(file="icons/Pelicans2001.png")
        LogoCanvas.image = pelicansLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=pelicansLogo)
    if TeamsVar.get() == "New York Knicks":
        LogoCanvas.delete("all")
        knicksLogo = PhotoImage(file="icons/Knicks1001.png")
        LogoCanvas.image = knicksLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=knicksLogo)
    if TeamsVar.get() == "Oklahoma City Thunder":
        LogoCanvas.delete("all")
        thunderLogo = PhotoImage(file="icons/Thunder1002.png")
        LogoCanvas.image = thunderLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=thunderLogo)
    if TeamsVar.get() == "Orlando Magic":
        LogoCanvas.delete("all")
        magicLogo = PhotoImage(file="icons/Magic3001.png")
        LogoCanvas.image = magicLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=magicLogo)
    if TeamsVar.get() == "Philadelphia 76ers":
        LogoCanvas.delete("all")
        sixersLogo = PhotoImage(file="icons/Sixers1001.png")
        LogoCanvas.image = sixersLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=sixersLogo)
    if TeamsVar.get() == "Phoenix Suns":
        LogoCanvas.delete("all")
        sunsLogo = PhotoImage(file="icons/Suns1001.png")
        LogoCanvas.image = sunsLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=sunsLogo)
    if TeamsVar.get() == "Portland Trail Blazers":
        LogoCanvas.delete("all")
        blazersLogo = PhotoImage(file="icons/Blazers1001.png")
        LogoCanvas.image = blazersLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=blazersLogo)
    if TeamsVar.get() == "Sacramento Kings":
        LogoCanvas.delete("all")
        kingsLogo = PhotoImage(file="icons/Kings1001.png")
        LogoCanvas.image = kingsLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=kingsLogo)
    if TeamsVar.get() == "San Antonio Spurs":
        LogoCanvas.delete("all")
        spursLogo = PhotoImage(file="icons/Spurs1001.png")
        LogoCanvas.image = spursLogo
        LogoCanvas.create_image(0, 0, anchor='nw', image=spursLogo)


TeamsVar.trace("w", callTeamLogo)
# Trace call with creation of the canvas and logo on it

app.mainloop()
