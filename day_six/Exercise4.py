unsorted_list = [11, 25, 12, 22, 64, 8, 4, 35, 50, 6]

#Make each item in unsorted_list a list
for index in range( len( unsorted_list ) ):
	#Set the value at the current index equal to the value at the current index as a list
	unsorted_list[index] = [ unsorted_list[index] ]

#While unsorted_list has more than 1 list in it
while len(unsorted_list) > 1:

	#We are going to build a new unsorted list with half the original items in it
	new_unsorted_list = []

	#FOr every other index build a list that is those two lists merged together
	for index in range( 0, len(unsorted_list), 2 ):

		#Create a list to store a new inner list that is the two lists merged together
		new_inner_list = []

		# print(unsorted_list, index)
		# print(new_unsorted_list)
		# print("===================")

		#If the current index is the last index
		if index+1 == len(unsorted_list):
			#Add to the end of new_unsorted list instead of merging
			#Because it has not list to merge with
			new_unsorted_list.append( unsorted_list.pop(index) )
		#If the current index is not the last index
		else:
			#Run the following if statements until the lists at index and index+1 are empty
			#As long as one list has at least one value this loop will run
			while len( unsorted_list[index] ) > 0 or len( unsorted_list[index+1] ) > 0:

				# print(unsorted_list[index])
				# print(unsorted_list[index+1])
				# print("----------")

				#If one list is empty add the first item of the other list to the new inner list
				if unsorted_list[index] == []:
					#Add the value of the first index of the list at index +1 to new_inner_list
					#and remove from index+1 the same value
					new_inner_list.append( unsorted_list[index+1].pop(0) )

				#This if is the same as the previous if but for the opposite list
				elif unsorted_list[index+1] == []:
					new_inner_list.append( unsorted_list[index].pop(0) )

				#If the value at the first index of the list at index is less than the value
				#at the first index of the list at index+1
				elif unsorted_list[index][0] <= unsorted_list[index+1][0]:
					#Then remove the value at the first index of the list at index
					#and add it to the new_inner_list
					new_inner_list.append( unsorted_list[index].pop(0) )

				#If the value at the first index of the list at index+1 is less than the value
				#at the first index of the list at index
				elif unsorted_list[index][0] > unsorted_list[index+1][0]:
					#Then remove the value at the first index of the list at index+1
					#and add it to the new_inner_list
					new_inner_list.append( unsorted_list[index+1].pop(0) )

			#Once the while loop is complete add the new_inner_list to the new_unsorted_list
			new_unsorted_list.append( new_inner_list )
			
	#Once all items have been removed from the original unsorted_list set unsorted_list
	#equal to new_unsorted_list and start again, until unsorted_list has only one list
	unsorted_list = new_unsorted_list

print(unsorted_list)