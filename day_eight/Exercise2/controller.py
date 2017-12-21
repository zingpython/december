from model import Model
from view import View

my_model = Model()
my_view = View()

running = True

while running == True:
	user_input = my_view.menu()

	if user_input == "1":

		item = my_view.takeInput("What item will you add? ")

		my_model.insertItem(item)

	elif user_input == "2":

		shopping_list = my_model.selectAllItems()

		my_view.printList(shopping_list)

	elif user_input == "3":

		choosing = True

		while choosing == True:

			id = my_view.takeInput("Enter the id to check off: ")

			try:
				id = int(id)

				choosing = False

				my_model.updateChecked(id, "CHECKED")

			except ValueError:
				my_view.printOut("Not a number, try again")

	elif user_input == "4":

		choosing = True

		while choosing == True:

			id = my_view.takeInput("Enter the id to check off: ")

			try:
				id = int(id)

				choosing = False

				my_model.updateChecked(id, "UNCHECKED")

			except ValueError:
				my_view.printOut("Not a number, try again")

	elif user_input == "5":
		running = False
		
	else:
		my_view.printOut("Invalid choice, try again.")