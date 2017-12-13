user_input = input( "Enter a word:" )

is_palindrome = True

for index in range( len(user_input) ):

	if user_input[index] != user_input[ -(index+1) ]:
		is_palindrome = False


if is_palindrome == False:
	print("Not a palindome")
else:
	print("Palindome")


#Slice method

if user_input == user_input[::-1]:
	print("Palindrome")
else:
	print("Not a palindome")


#Using the reverse method
print( "".join( reversed(user_input) )  )

if user_input == "".join( reversed(user_input) ):
	print("Palindrome")
else:
	print("Not a palindrome")