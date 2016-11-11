

class Player:
	def __init__(self, player_id):
		self.player_id = player_id
		self.largest_army = None
		self.longest_road = None
		self.score = 0
		self.dev_cards = DevCardHand()
		self.resources = ResourcesHand()




