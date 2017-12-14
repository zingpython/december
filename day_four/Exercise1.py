

def findWord(search_word):
	# search_word = input("Enter a word: ")

	with open("word.txt", "r") as text_file:
		lines = text_file.readlines()

		found = False

		for line in lines:

			if search_word == line.strip():
				found = True

		if found == True:
			# print(search_word)
			return search_word
		else:
			# print("NOT FOUND")
			return "NOT FOUND"

# print( findWord("hello") )


def countLetters():
	#Open the file
	with open("letters.txt", "r") as text_file:
		#Read each line of the file
		lines = text_file.readlines()

		#Create an empty dictionary to hold a key value pair of a letter and the number of times it has appeared
		letter_dict = {}

		#Run a for loop for each line in the lines
		for line in lines:

			#Run a for loop for each letter in a line
			for letter in line:

				#If the letter is in the dictionary
				if letter in letter_dict.keys():
					#Increase its value by 1
					letter_dict[letter] = letter_dict[letter] + 1
				#If the letter is not in the dicitonary
				else:
					#Add it to the dictionary as the key with a value of 0
					letter_dict[letter] = 1

				# THis is equivalent to lines 15 to 22 in one line
				# letter_dict[letter] = letter_dict.get(letter, 0) + 1

		return letter_dict

counted_letter = countLetters()

print(counted_letter)	
