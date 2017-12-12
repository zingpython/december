height = 50

for current_height in range( 1, (height*2) ):
	output = ""

	#Ascending stars
	if current_height <= height:
		for x in range( current_height ):
			output = output + " *"

	#Descending stars
	else:
		for x in range( height - (current_height - height) ):
			output = output + " *"


	print(output)