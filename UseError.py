
class UseError(Error):
	def __init__(self, item):
		self.message = "You do not have enough of " + item