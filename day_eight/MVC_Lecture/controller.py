from model import Model
from view import View

my_model = Model()
my_view = View()

running = True

while running == True:

	user_input = my_view.menu()

	if user_input == "1":

		csv_file_name = my_view.takeInput("Enter a csv file to read: ")

		lines = my_model.readFile(csv_file_name)

		for line in lines:
			my_model.insertUser( line[0], line[4], line[5] )

			last_id = my_model.getLastRowID()

			my_model.insertPhone( last_id, line[1] )
			my_model.insertPhone( last_id, line[2] )
			my_model.insertPhone( last_id, line[3] )

	elif user_input == "2":

		name = my_view.takeInput("Enter a name: ")
		email = my_view.takeInput("Enter an email: ")
		country = my_view.takeInput("Enter a country: ")

		my_model.insertUser(name, email, country)

	elif user_input == "3":
		all_users = my_model.selectAllUsers()

		my_view.printList(all_users)

	elif user_input == "4":
		all_phones = my_model.selectAllPhones()

		my_view.printList(all_phones)

	elif user_input == "5":
		
		user_id = my_view.takeInput("Enter a user ID: ")

		try:
			user_id = int( user_id )	

			user_phones = my_model.selectPhonesByUser(user_id)

			my_view.printList(user_phones)

		except ValueError:
			my_view.printOut("Not a number.")

	elif user_input == "6":
		running = False

	else:
		my_view.printOut("Invalid entry, try again.")