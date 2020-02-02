from tkinter import *
import teamslist

# WINDOW
window = Tk()
window.iconbitmap("icon/NBAclear.ico")
window.title("NBA Oracle")
window.configure(background="Darkblue")

# HEADER
logo = PhotoImage(file="header/NBAclear.png")
logoNBA = Label(window, image=logo, bg="Darkblue")
resizeLogo = logo.subsample(1, 1)
logoNBA.config(image=resizeLogo)
logoNBA.grid(row=0,column=1)

# DROP DOWN MENU
TeamsVar = StringVar() 
TeamsVar.set(teamslist.TeamsList[0])
droplist = OptionMenu(window, TeamsVar, *teamslist.TeamsList)
droplist.config(width=30, height=1, fg="Darkblue")
droplist.grid(row=1,column=1)

# TEAM SELECTED
teamSelected = Label(window, text="Team Selected:", bg="Darkblue", fg="White")
teamSelected.grid(row=2,column=0)
teamSelectedOutput = Text(window, width=20, height=1)
teamSelectedOutput.grid(row=2,column=1)

# YEAR FORMED
yearFormed = Label(window, text="Year Formed:", bg="Darkblue", fg="White")
yearFormed.grid(row=3,column=0)
yearFormedOutput = Text(window, width=20, height=1)
yearFormedOutput.grid(row=3,column=1)



window.mainloop()