from Monopoly import Monopoly
from 



class DevCardHand():

	def __init__(self):
		self.knights = 0
		self.monopoly = 0
		self.road_builder = 0
		self.year_of_plenty = 0
		self.victory_point = 0


	# use a dev card
	def use_card(card_type):
		if isinstance(card_type, Monopoly):
			if self.monopoly ==0:
				raise UseError("Insufficient Monopoly Cards")
				return
			self.monopoly -= 1

		if isinstance(card_type, RoadBuilder):
			if self.road_builder ==0:
				raise UseError(str(card_type))
				return
			self.road_builder -= 1

		if isinstance(card_type, VictoryPoint):
			if self.victory_point ==0:
				raise UseError(str(card_type))
				return
			self.victory_point -= 1

		if isinstance(card_type, Knight):
			if self.knight ==0:
				raise UseError(str(card_type))
				return
			self.knight -= 1
		if isinstance(card_type, YearOfPlenty):
			if self.knight ==0:
				raise UseError(str(card_type))
				return
			self.year_of_plenty -= 1			
			
		


