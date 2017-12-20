
class View:

	def printOut(self, output):
		print(output)

	def takeInput(self, prompt):
		return input(prompt)

	def menu(self):
		print("1. Enter a card number")
		print("2. Validate a card")
		print("3. Display card information")
		print("4. Exit")

		return input("Enter a menu number: ")