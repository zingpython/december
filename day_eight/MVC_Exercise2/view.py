
class View:

	def printOut(self, output):
		print(output)

	def printList(self, output_list):
		for item in output_list:
			print( " | ".join( map( str, item ) )  )

	def takeInput(self, prompt):
		return input(prompt)

	def menu(self):
		print("1. Read from file")
		print("2. Enter a user manually")
		print("3. Select all users")
		print("4. Select all phone number")
		print("5. Select phone numbers by user id")
		print("6. Exit")

		return input("Enter a menu number: ")

