###Q1.py

import re

##classes

class ScoreTable():
	def __init__(self):
		self.__highScoreBid = "No High Score"
		self.__highScore = 0
		
	def get_highScoreBid(self):
		return self.__highScoreBid
		
	def get_highScore(self):
		return self.__highScore
	
	def set_highScore(self,bid,score):
		self.__highScoreBid = bid
		self.__highScore = score
		
	def display(self):
		print("Top bowler:",self.get_highScoreBid())
		print("High Score:",self.get_highScore())

class Bowler():
	
	def __init__(self,bid,score):
		valid_Bid,valid_Score = False,False
		
		score = int(score)
		
		if not self.validate_bid(bid) and not self.validate_score(score):
			print("Bowler entry was not created.")
		else:
			self.__bid = bid
			self.__score = score
			
		if(score > scoreTable.get_highScore()):
			scoreTable.set_highScore(bid,score)
		
	def validate_bid(self, bid):
		pattern_ValidBid = re.compile("[0-9]{4}")
		
		if not pattern_ValidBid.match(bid):
			print("invalid Bowler ID. Bowler ID must be a 4-digit code.")
			return False
		else:
			return True
		
	def validate_score(self, score):
		score = int(score)
		if(0 <= score <= 300):
			self.__score = score
			valid_Score = True
		else:
			print("invalid Score. Score must be between 0 and 300.")
	
	def get_bid(self):
		return self.__bid
	
	def get_score(self):
		return self.__score
	
	def display(self):
		print("Bowler ID:",self.get_bid())
		print("Score:",self.get_score())
		
##main

if __name__ == '__main__':
	
	scoreTable = ScoreTable()
	
	flag_BowlerCreation = True
	
	for i in range(10):
		if(flag_BowlerCreation):
			bid = input("Bowler ID:")
			score = input("Score:")
			bowler = Bowler(bid,score)
			query_Continue = input("Continue? (Y/N)")
			if(query_Continue != "Y" and query_Continue != "y"):
				flag_BowlerCreation = False
		else:
			break
	
	
	scoreTable.display()