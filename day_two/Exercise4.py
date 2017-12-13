#Dictionary to convert from letter to number
letter_to_number = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10,
			"k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19,
			"t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}

#Dictionary to convert from number to letter
number_to_letter = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j",
			11:"k", 12:"l", 13:"m", 14:"n", 15:"o", 16:"p", 17:"q", 18:"r", 19:"s",
			20:"t", 21:"u", 22:"v", 23:"w", 24:"x", 25:"y", 26:"z"}

#Take in sentence and shift value
sentence = input("Enter a sentence: ")

shift = int( input("Enter the shift number: ") )

#Store the encrypted sentence in this new_sentence
new_sentence = ""

#For each letter in sentence
for letter in sentence:

	#If the letter is an alphabetic character
	if letter.isalpha():

		#Check if the letter is uppercase or lowercase and store that information in a boolean
		if letter.isupper():
			is_upper = True
		else:
			is_upper = False

		#Convert the letter to a number. NOTE: force letter to lowercase to prevent errors
		number = letter_to_number[ letter.lower() ]

		#Shift the letter by the shift value
		number = shift + number

		#Check if the number is out of the range 1 to 26 and return it to the proper range
		if number > 26:
			number = number - 26

		elif number < 1:
			number = number + 26

		#Convert the number back to a letter
		new_letter = number_to_letter[ number ]

		#If the letter was uppercase then convert new letter to uppercase
		if is_upper == True:
			new_letter = new_letter.upper()

		#Add new letter to the new_sentence
		new_sentence = new_sentence + new_letter

	#If letter is not an alphabetic character then add to the new_sentence unchanged
	else:
		new_sentence = new_sentence + letter

#Print new sentence
print(new_sentence)