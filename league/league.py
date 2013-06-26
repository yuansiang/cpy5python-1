###league.py

class Team():
	def __init__(self,teamName):
		self.__teamName = teamName
		self.__wins = 0
		self.__draws = 0
		self.__losses = 0
		self.__points = 0
		self.__GF = 0
		self.__GA = 0

	def getName(self):
		return self.__teamName
		
	def getPoints(self):
		#calculate points
		self.__points = self.__wins * 3 + self.__draws
		return self.__points
	
	def getGF(self):
		return self.__GF
	
	def getGA(self):
		return self.__GA
	
	def addEntry(self,gf,ga):
		gf = int(gf)
		ga = int(ga)
		
		#update wins/draws/losses/gf/ga
		if gf == ga:
			self.__draws = self.__draws + 1
		elif gf > ga:
			self.__wins = self.__wins + 1
		else:
			self.__losses = self.__losses + 1
		
		self.__GF = self.__GF + gf
		self.__GA = self.__GA + ga
		
	def display(self):
		return "{0}  {1:2d}  {2:2d}  {3:2d}  {4:3d}  {5:3d}  {6:3d}".format(self.__teamName,self.__wins,self.__draws,self.__losses,self.__GF,self.__GA,self.__points)

teamList = [] #empty list of teams
teams = {} #empty dictionary to refer to teams

infile = open('LEAGUE.DAT','r')
for line in infile:
	teamAName = line[0:16]
	teamAScore = line[16]
	teamBName = line[18:34]
	teamBScore = line[34]
	
	if teamAName not in teamList: #Check if team has been created. if not,
		teamList.append(teamAName) #Add teamname into list of existing teams
		teams[teamAName] = Team(teamAName) #Add team into dictionary for future referencing
		
	if teamBName not in teamList:
		teamList.append(teamBName)
		teams[teamBName] = Team(teamBName)
		
	teams[teamAName].addEntry(teamAScore,teamBScore) #update data for both teams
	teams[teamBName].addEntry(teamBScore,teamAScore)
	
infile.close() #close reference to file, as no use for it anymore to clear memory

standings = [] #insertion sort

for team in teams: #where team returns each key of the teams dictionary
	
	points = teams[team].getPoints() #to prevent repetition when obtaining same value
	
	for i in range(len(standings)):
		if points == standings[i].getPoints(): #GF - GA tie condition
			if teams[team].getGF - teams[team].getGA > standings[i].getGF - standings[i].getGA:
				standings.insert(i,teams[team]) #insert into correct sorted placing
				break
			else:
				standings.insert(i+1,teams[team])#insert into correct sorted placing
				break
		elif points > standings[i].getPoints():
			standings.insert(i,teams[team])#insert into correct sorted placing
			break
	else:
		standings.insert(len(standings),teams[team])#insert into back of list
		
print("No Team               W   D   L   GF   GA  PTS")

for i in range(len(standings)):
	print("{0:2d}".format(i+1),standings[i].display()) #print results