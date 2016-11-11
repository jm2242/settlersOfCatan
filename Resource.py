from abc import ABCMeta, abstractmethod

class Resource(object):
	# A dev card that is playable in the game

	cost = {"Wheat":1,"Clay":0,"Rock":1,"Sheep":1,"wood":1}



	__metaclass__ = ABCMeta



	@abstractmethod
	def card_type(self):
		pass




