size = 10

for x in range( 1 , size+1 ):

	output = ""

	for y in range( 1 , size+1 ):

		output = output + "  " + str( x*y )

	print(output)