unsorted_list = [10, 8, 6, 108, 5, 6, 7]

#Move through the unsorted_list one index at a time
for right_index in range( len(unsorted_list) ):
	#Move backwards over all previous indices starting from one less than the right_index
	#					      Start point, end, increment
	#End points are exclusive so use one less than the value you want (when going backwards)
	for left_index in range( right_index-1, -1, -1 ):

		#If the value at right index is greater than the value at left_index
		if unsorted_list[right_index] >= unsorted_list[left_index]:
			#Remove the value at right index
			insert_value = unsorted_list.pop(right_index)

			#And insert it after the left_index
			#USe left_index+1 because insert() will insert the value before that index 
			#and we want to insert after that index
			unsorted_list.insert( left_index+1, insert_value )

			#Stop running the inner for loop to prevent extra swaps
			break

		#If the left_index is 0 and the value at right index is less than the value of left index.
		#We know that it is less than all other value before it and must be inserted at the front
		#of the list
		elif left_index == 0 and unsorted_list[right_index] < unsorted_list[left_index]:
			#remove the value at right_index
			insert_value = unsorted_list.pop(right_index)

			#And insert at the beginning of the list, index 0
			#.insert() function takes 2 values(the index to insert before, and the value to insert)
			unsorted_list.insert( 0, insert_value )

print(unsorted_list)