#Take in user input
filename = input("Enter a file: ")
highest = int( input("How many words: ") )

#Open the file bsaed on user input
with open(filename, "r", encoding="ISO 8859-1") as text_file:
	#Read each line of the file
	lines = text_file.readlines()

	#Create a dicitonary to hold each key and the number of times each key appears
	word_dict = {}

	# For every line in our file
	for line in lines:

		#Split line into a list made of each word by using the split function on a space
		line = line.split(" ")

		#For each word in line
		for word in line:

			#Remove all non letter characters from the word

			#Create a new word which starts as an empty string
			new_word = ""

			#For each letter in the original word
			for letter in word:

				#If the letter is a alphabetic character then add to the new word
				if letter.isalpha():
					new_word = new_word + letter

			#Make the word lowercase to prevent multiple occurances of each word
			new_word = new_word.lower()

			#If the word is not an empty string, add to the dictionary
			if new_word != "":
				#If the word is not in the dictionary insert it with a default value of 1.
				#If it is in the dictonary increase its value by 1
				word_dict[new_word] = word_dict.get(new_word, 0) + 1

	#Sort the dictionary into a list
	#Create an empty list to hold each key ordered by its value [highest to lowest]
	word_list = []

	#FOr every key in the dictionary
	for key in word_dict.keys():

		#If the list is empty add a key in, we do nt need to sort the first value
		if len(word_list) == 0:
			word_list.append(key)

		#If the list is not empty find the right place for the word
		#NOTE: there must be at least one item in list for this to work.
		else:

			#FOr every item in our list
			for index in range(len(word_list)):

				#Check if the current item's value is less than the current key's value
				if word_dict[ key ] > word_dict[ word_list[index] ]:
					#If it is add the current key into the list infront of the current index.
					word_list.insert(index, key)
					#End the loop to prevent the loop from adding the key in multiple times
					break

				#If the current key's value is les than all other items in the list 
				#and index is on the last item of the list
				elif word_dict[key] <= word_dict[ word_list[index] ] and index == len(word_list)-1:
					#Add the key to the end of the list because its value is less than all other values
					word_list.append(key)
	
	#Print only the top highest words
	for word in word_list[0:highest]:
		print(word +", "+ str( word_dict[word] ) )