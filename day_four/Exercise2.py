
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

	binary = binary[::-1]

	increase = 1

	for digit in binary:


		increase = increase * 2