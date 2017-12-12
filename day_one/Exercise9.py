for number in range( 2,101 ):

	is_prime = True

	for prime in range( 2, number ):
		
		if number%prime == 0:
			is_prime = False

	if is_prime == True:
		print("PRIME")
	else:
		print(number)