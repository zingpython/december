def selectionSort(unsorted_list):
	#Create empty list to hold the sorted values
	sorted_list = []
	#Run until unsorted_list is empty
	while len(unsorted_list) > 0:

		# print(unsorted_list)
		# print(sorted_list)
		# print("--------------")

		#lowest_index will hold the index of the lowest value, starts at 0 to prevent list out of range errors
		lowest_index = 0

		#FOr each item in unsorted list
		for current_index in range( len(unsorted_list) ):
			#Check if the value at current_index is less than the value at lowest_index
			if unsorted_list[current_index] < unsorted_list[lowest_index]:
				#If so set lowest_index to the current_index
				lowest_index = current_index

		#Add the lowest value to the end of the sorted_list.
		#We know that we have removed all values less than the current value from the list and added 
		#them to the end of sorted_list. This means that adding the current value to the end of the list
		#will be sorting that list
		sorted_list.append( unsorted_list.pop(lowest_index) )

	return sorted_list

print( selectionSort([11, 25, 12, 22, 64, 8, 4, 35, 50, 6]) )