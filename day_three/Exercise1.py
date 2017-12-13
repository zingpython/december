
search_word = input("Enter a word: ")

with open("word.txt", "r") as text_file:
	lines = text_file.readlines()

	found = False

	for line in lines:

		if search_word == line.strip():
			found = True

	if found == True:
		print(search_word)
	else:
		print("NOT FOUND")