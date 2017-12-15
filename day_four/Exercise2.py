
def intToBinary(number):
	#Create empty string to hold the binary number
	binary = ""

	#To find a binary number divide by 2 untill the number is 0
	while number > 0:
		#Find the remainder to find the binary digit
		remainder = number % 2
		#Add the binary digit to the left of the current binary number
		binary = str(remainder) + binary
		#Divide the number by 2 using integer division
		number = number // 2

		# print(number)
	#Return the completed binary number
	return binary

print( intToBinary(210) )



def binaryToInt(binary):
	# #Reverse the string so we can use a for loop going forwards instead of backwards
	# binary = binary[::-1]
	# #Create a total variable that will hold the total of the binary number
	# total = 0
	# #Create a variable that holds how much to increase the total by on a "1"
	# increase = 1

	# #FOr each digit in the binary number
	# for digit in binary:
	# 	#If the digit is a "1" increase the total by increase
	# 	if digit == "1":
	# 		total = total + increase

	# 	#As the last step in the for loop double increase
	# 	increase = increase * 2
	# #Return the total of the binary number
	# return total

	binary = binary[::-1]

	total = 0

	for index in range( len(binary) ):

		if binary[index] == "1":
			total = total + (2 ** index)

	return total

print( binaryToInt("11010010") )