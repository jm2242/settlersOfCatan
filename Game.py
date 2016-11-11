
VICTORY = 10


class Game():

	# game properties

	# keep track of which player has these
	largest_army = None
	longest_road = None

	# keep track of the players
	players = []

	def __init__(self, numPlayers):





	def init_board():
		pass

	# deal the appropriate resources to all players given the die roll
	# requires an integer dieRoll between 2 and 12
	def deal_resources(dieRoll):
		if diRoll < 2 or dieRoll > 12:
			raise "die combination not possible"
