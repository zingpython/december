class View:

	def printOut(self, output):
		print(output)

	def printList(self, shopping_list):
		
		for item in shopping_list:
			print(str(item[0])," | ",item[1]," | ",item[2])

	def takeInput(self, prompt):
		return input(prompt)

	def menu(self):
		print("1. Add an item")
		print("2. Show list")
		print("3. Check item")
		print("4. Uncheck item")
		print("5. Exit")

		return input("ENter a menu number: ")