#Take in the sentence to capitalize
sentence = input("Enter a sentence: ")

# new_sentence will hold the new sentence we are building
new_sentence = ""

# Makes the first letter of a sentence capital
capitalize_next = True

#For each letter in my sentence return its index
for index in range( len(sentence) ):

	#If the letter at the index is an alphabetic character and capitalize_next is true
	if sentence[index].isalpha() == True and capitalize_next == True:
		#Then capitalize the letter
		new_sentence = new_sentence + sentence[index].upper()
		#And set capitalize next equal to false to prevent further capitalizations
		capitalize_next = False

	#If the current letter is a . ! or ? then we have found the end of a sentence
	elif sentence[index] in [".", "?", "!"]:
		#Add the punctuation to the new_sentence
		new_sentence = new_sentence + sentence[index]
		#And capitalize the next letter found by setting capitalize_next to True
		capitalize_next = True

	#If the current letter is a lowercase i and the characters before and after it are spaces
	elif sentence[index] == "i" and sentence[index+1] == " " and sentence[index-1] == " ":
		#Then capitalize the i
		new_sentence = new_sentence + "I"

	#Otherwise add the letter to the sentence unchanged
	else:
		new_sentence = new_sentence + sentence[index]

	# print(new_sentence)
#Output new sentence
print(new_sentence)