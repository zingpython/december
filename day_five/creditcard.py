
class CreditCard:

	def __init__(self, card_num):
		self.card_num = card_num
		self.findCardType()
		self.luhn()

	def findCardType(self):
		# Create a dicitonary with a key of a card type and a value of a 
		# list that holds all possible starting numbers
		starting_numbers = {"VISA":["4"],
							"MASTERCARD":["51","52","53","54","55"],
							"AMEX":["34","37"],
							"DISCOVER":["6"]}

		#set a default card type
		self.card_type = "INVALID"

		# For each card type
		for key in starting_numbers.keys():
			#Read each possible starting number
			for value in starting_numbers[key]:
				#Check if the starting numbers of card_num match any starting numbers

				#Slice the string card_num on the length of the current starting number.
				#This will get the proper number of character to check. 
				#Ex: "1" will get only the first value, "54" will get the first 2 characters
				if value == self.card_num[0: len(value) ]:
					#If there is a match then the current key is the card type					
					self.card_type = key

		#Create a dictionary with a key of a card type and a value of the length that card should be
		starting_length = {"VISA":16,
							"DISCOVER":16,
							"MASTERCARD":16,
							"AMEX":15}

		#Only check the card length if the type is not invalid
		if self.card_type != "INVALID":
			#if the length of card_num is different then of what the card type should be
			#Then the card type is invalid
			if len(self.card_num) != starting_length[ self.card_type ]:
				self.card_type = "INVALID"

	def luhn(self):
		#Create two strings some string starting from the last place and every other character after
		single_digits = self.card_num[-1::-2]
		#And one starting from the second to last placec and every other character after
		doubled_digits = self.card_num[-2::-2]

		#Create an empty string that will hold the doubled values of doubled_digits
		new_double = ""

		#FOr each value in doubed_digits
		for digit in doubled_digits:
			#Double the digit
			digit = int(digit) * 2
			#And add to the string
			new_double = new_double + str(digit)

		#Create an empty integer that will hold the total of all digits
		total = 0

		#Total all digits in the single_digits string
		for digit in single_digits:
			total = total + int(digit)

		#Total all digits in the new_double string
		for digit in new_double:
			total = total + int(digit)

		#If the total is divisible by 10 then the card is valid
		if total%10 == 0:
			self.valid = True
		#If it is not divisible then it is not valid
		else:
			self.valid = False

my_card = CreditCard("4485040993287616")
print(my_card.valid)
print(my_card.card_type)