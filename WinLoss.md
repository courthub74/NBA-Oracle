#Issue 1: Determining Winner

I have populated given data from the sportsAPI for my NBAOracle. The next challenge is to
determine is the selected team by the user has won or loss their last game. This is a challenge
because the API doesn't directly tell you if selected team has won or loss.

The API data is returned as such:

hometeam = "String of team that played as home team"
awayteam = "String of team that played as away team"
homescore = "String of home team score"
awayscore = "String of away team score"

Being that the team that user selects is not always home or away, it presents a task to determine is the selected team has won or loss from that information.

I have to create a function that can properly asses the winner from the information given.
