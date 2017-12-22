class View:

	def printOut(self, output):
		print(output)

	def takeInput(self, prompt):
		return input(prompt)

	def loginMenu(self):
		print("1. Create User")
		print("2. Log in")
		print("3. Exit")
		return input("Enter a menu number: ")

	def bankMenu(self):
		print("1. Withdraw funds")
		print("2. Deposit funds")
		print("3. Account Information")
		print("4. Transfer funds")
		print("5. Log out")
		return input("Enter a menu number: ")

	def printUserInfo(self, user_info):
		print("Username: "+user_info[1])
		print("Address: "+user_info[3])
		print("Phone Number: "+user_info[4])
		print("Email: "+user_info[5])
		print("Balance: "+ str(user_info[6]) )