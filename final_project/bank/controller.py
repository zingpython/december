from view import View
from model import Bank

def bankMenu(my_view,my_bank, id):
	bank_running = True
	while bank_running == True:
		user_input = my_view.bankMenu()

		if user_input == "1":

			#Run user input until the user gives a valid Float number
			input_while = True
			withdraw = 0.0
			while input_while == True:
				withdraw_input = my_view.takeInput("enter an amount to withdraw: ")
				#Try block to check if user input is a float
				try:
					withdraw = float(withdraw_input)
					#Input while = false will only run IF withdraw_input is successfuly converted to a float 
					input_while = False
				except ValueError:
					#If withdraw_input cannout be converted print try again.
					print("Invalid number. Try again")

			user_info = my_bank.selectById(id)

			#If the amount to withdraw is less than or equal to your current balance AND it is greater than 0. Withdraw that much
			if withdraw <= user_info[6] and withdraw>0:
				new_balance = user_info[6]-withdraw
				my_bank.updateBalance(id, new_balance)
				my_view.printOut("Withdrew "+str(withdraw)+"$ from your account")
			#If it is less than 0 or greater than our current balance. Return an error
			elif withdraw < 0:
				my_view.printOut("Error please enter a positive number")
			else:
				my_view.printOut("Insufficent funds")


		elif user_input == "2":

			#Run while lop until user gives a valid input that can be converted to a Float
			input_while = True
			deposit = 0.0
			while input_while == True:
				deposit_input = my_view.takeInput("enter an amount to deposit: ")

				#Try block checks if user_input can be converted to a float
				try:
					deposit = float(deposit_input)
					#Only runs IF deposite_input can be converted to a Float
					input_while = False
				except ValueError:
					#Prints error message if user_input cannout be convereted
					print("Invalid number. Try again")

			# Get user info from table
			user_info = my_bank.selectById(id)
			#Add deposit to current balance
			new_balance = deposit + user_info[6]
			#Update table with new balance
			my_bank.updateBalance(id, new_balance)

		elif user_input == "3":
			#Get user info and output user info
			user_info = my_bank.selectById(id)
			my_view.printUserInfo(user_info)
		# elif user_input == "4":
			#Take id from user.
			#Check if user exists(Done on login function)
			#If it is a valid user then take in how much to transfer (Done in deposit and withdraw)
			#Check if transfer ammount is less than current balance. (Done in withdraw)
			#If transfer ammount is valid remove that much from your account and add it to the other user's account (Done with deposit and withdraw)
		elif user_input == "5":
			bank_running = False
		else:
			my_view.printOut("Invalid entry. Try again")

my_view = View()

my_bank = Bank()

login_running = True

while login_running == True:
	user_input = my_view.loginMenu()

	if user_input == "1":

		#Run until the user inputs a username that doesnt already exst
		username_while = True
		username = ""
		while username_while == True:
			#Take in potential username
			username = my_view.takeInput("Enter a username: ")
			#Get all users from database
			rows = my_bank.selectAll()

			#iterate through each user in database and if a username matches potential username then the user needs to select a new username
			found = False
			for row in rows:
				if username == row[1]:
					found = True

			#If username is in database run while loop again otherwise, exit while loop
			if found == False:
				username_while = False
			else:
				my_view.printOut("That username already exists.\n")

		#take in password, address, email, and phone number
		password = my_view.takeInput("Enter a Password: ")
		address = my_view.takeInput("Enter an address: ")
		phonenumber = my_view.takeInput("Enter a Phone number: ")
		email = my_view.takeInput("Enter your email: ")

		#insert into database
		my_bank.insertRow(username,password,address,phonenumber,email)

	elif user_input == "2":
		username = my_view.takeInput("Enter your Username: ")
		password = my_view.takeInput("Enter your Password: ")

		rows = my_bank.selectAll()
		print(rows)
		found = False
		index = -1
		for row in range(len(rows)):
			if username == rows[row][1]:
				found = True
				index = row

		if found == True:
			if password == rows[index][2]:
				bankMenu(my_view, my_bank, rows[index][0] )
			else:
				my_view.printOut("Invalid username or password")
		elif len(row) == 0:
			my_view.printOut("No users exits. Create a user first")
		else:
			my_view.printOut("Invalid username or password")


	elif user_input == "3":
		login_running = False
		my_bank.closeConnection()
	else:
		my_view.printOut("That is not a valid choice. Try again.\n")