from model import Model
from view import View

my_model = Model()
my_view = View()

running = True

while running == True:

	user_input = my_view.menu()

	if user_input == "1":

		choosing = True

		while choosing == True:

			new_card_num = my_view.takeInput("Enter a card number: ")

			if new_card_num.isdigit() and len(new_card_num) > 0:
				my_model.setCardNumber( new_card_num )
				choosing = False
			else:
				my_view.printOut("Invalid card number. Try again")

	elif user_input == "2":

		new_card_type = "INVALID"

		for key in my_model.starting_numbers.keys():
			
			for value in starting_numbers[key]:
				
				if value == my_model.getCardNumber()[0: len(value) ]:				
					new_card_type = key

		if new_card_type != "INVALID":

			if len(my_model.getCardNumber) != my_model.starting_length[new_card_type]:

				new_card_type = "INVALID"

		my_model.setCardType(new_card_type)


		#Luhn
		single_digits = my_model.getCardNumber()[-1::-2]
		doubled_digits = my_model.getCardNumber()[-2::-2]

		new_double = ""

		for digit in doubled_digits:
			digit = int(digit) * 2
			new_double = new_double + str(digit)

		total = 0

		for digit in single_digits:
			total = total + int(digit)

		for digit in new_double:
			total = total + int(digit)

		if total%10 == 0:
			my_model.setValid( True )
		else:
			my_model.setValid( False )



	elif user_input == "3":

		my_view.printOut( "Card NUmber: ", my_model.getCardNumber() )
		my_view.printOut("Card Type: ", my_model.getCardType() )
		my_view.printOut("Valid: ", str( my_model.getValid() ) )

	elif user_input == "4":
		running = False
	else:
		my_view.printOut("Invalid choice, try again.")