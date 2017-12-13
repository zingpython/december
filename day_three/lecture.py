
#Open the text file in read mode as the variable text_file
with open("word.txt", "r") as text_file:
	#create the variable lines with the readline() fucntion
	lines = text_file.readlines()
	#lines is a list of strings so we can use a for loop to print each line 
	for line in lines:

		print( line.strip() )

#Open the text file in append mode. This will not delete the file and only add to the end of the file
with open("word.txt", "a") as new_text_file:
	#Wrtie a string "THIS IS A TEST" to the end of word.txt
	new_text_file.write("\nTHIS IS A TEST")

#Open the text file in write mode. This will delete the entire contents of the file.
with open("word.txt", "w") as write_text_file:
	#Using the lines list created earlier add each line to the file with the write function
	for line in lines:
		write_text_file.write( "\t"+line )