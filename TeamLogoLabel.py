# CALL LOGO LABEL

spot = "Team Logo:"

def callLogoLabel(*args):
	if TeamsVar.get() == "Atlanta Hawks":
		LabelCanvas.delete("all")
		logospot = spot
		LabelCanvas.insert(INSERT, logospot)

TeamsVar.trace("w", callLogoLabel)
