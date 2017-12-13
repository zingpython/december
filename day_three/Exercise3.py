#Dictionary to convert from letter to number
letter_to_number = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10,
			"k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19,
			"t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}

#Dictionary to convert from number to letter
number_to_letter = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j",
			11:"k", 12:"l", 13:"m", 14:"n", 15:"o", 16:"p", 17:"q", 18:"r", 19:"s",
			20:"t", 21:"u", 22:"v", 23:"w", 24:"x", 25:"y", 26:"z"}

#Take in the file to be encrypted
filename = input("Enter a file name: ")

#Take in the shift amount
shift = int( input("Enter the shift number: ") )

#open the file to be encrypted
with open(filename, "r") as text_file:
	#Read each line of the file
	lines = text_file.readlines()

	#Open the file to be written into
	with open("encrypted_file.txt", "w") as write_file:

		#For each line in the original text file
		for line in lines:

			#create a new sentence that starts as a blank string
			new_sentence = ""

			#FOr each letter in line shift that letter and add to the new_string
			for letter in line:

				#Look at Day 2 Exercise 4.py This is a copy and paste of that file
				if letter.isalpha():

					if letter.isupper():
						is_upper = True
					else:
						is_upper = False

					number = letter_to_number[ letter.lower() ]

					number = number + shift

					if number > 26:
						number = number - 26
					elif number < 1:
						number = number + 26

					new_letter = number_to_letter[number]

					if is_upper == True:
						new_letter = new_letter.upper()

					new_sentence = new_sentence + new_letter

				else:
					new_sentence = new_sentence + letter

			#Add the new sentence to the new file.
			write_file.write(new_sentence)