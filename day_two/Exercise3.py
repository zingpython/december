word1 = input("Enter a word: ")
word2 = input("Enter a word: ")

dict1 = {}

dict2 = {}

for letter in word1:

	if letter in dict1.keys():
		dict1[letter] = dict1[letter] + 1
	else:
		dict1[letter] = 1


# print(dict1)

for letter in word2:

	if letter in dict2.keys():
		dict2[letter] = dict2[letter] + 1
	else:
		dict2[letter] = 1

# print(dict2)

# print(  dict1 == dict2  )

if dict1 == dict2:
	print("ANAGRAM")
else:
	print("NOT AN ANAGRAM")