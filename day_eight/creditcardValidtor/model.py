
class Model:

	def __init__(self):
		self.starting_numbers = {"VISA":["4"], "MASTERCARD":["51","52","53","54","55"], "AMEX":["34","37"], "DISCOVER":["6"]}

		self.starting_length = {"VISA":16, "DISCOVER":16, "MASTERCARD":16, "AMEX":15}

	def getCardNumber(self):
		return self.card_number

	def setCardNumber(self, card_number):
		self.card_number = card_number

	def getCardType(self):
		return self.card_type

	def setCardType(self, card_type):
		self.card_type = card_type

	def getValid(self):
		return self.valid

	def setValid(self, valid):
		self.valid = valid

