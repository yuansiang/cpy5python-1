with open("HIGHEST.txt","r") as infile:
	line = infile.readline()

highScore = line.split(" ")
print(highScore)
highScore[1] = int(highScore[1])

playerList = []

for i in range(5):
	playerNameValidated = False
	playerScoreValidated = False
	quit = False
	
	while not playerNameValidated:
		playerName = input("Input player name, or press enter to finish:")
		if playerName == "":
			if i == 0:
				print("You must enter a name!") #presence check
			else:
				playerNameValidated = True
				quit = True
		else:
			playerNameValidated = True
	
	if quit:
		break
	
	while not playerScoreValidated and not quit:
		playerScore = input("Input player score:")
		try: #check for number input
			playerScore = int(playerScore)
			playerScoreValidated = True
		except:
			print("Score must be an integer!")
			
	player = [playerName,playerScore]
	playerList.append(player)

highestPlayer = ["No players",0]

for player in playerList:
	if player[1] > highestPlayer[1]:
		highestPlayer = player
		
print("Highest score of today: " + str(highestPlayer[1]) + " from player:" + highestPlayer[0])
if highestPlayer[1] > highScore[1]:
	highestPlayer[1] = str(highestPlayer[1])
	print("It looks like today's high score beat the previous one!")
	with open("HIGHEST.txt","w") as outfile:
		outfile.write(" ".join(highestPlayer))