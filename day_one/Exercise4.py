letter = input("Enter a letter: ").lower()

# if letter in ["a","e","i","o","u"]:
if letter == "a" or letter == "e" or letter == "i" or letter == "u":
	print("VOWEL")
elif letter == "y":
	print("SOMETIMES VOWEL, SOMETIMES CONSONANT")
else:
	print("CONSONANT")