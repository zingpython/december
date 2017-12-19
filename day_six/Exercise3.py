unsorted_list = [10, 8, 6, 108, 5, 6, 7]

swapped = True
#If we make a swap in the for loop then keep runnning the while loop
while swapped == True:
	#Start swaped as false so the for loop can set it to true
	swapped = False
	#For all indexes except the last index, compare them to the next index
	for index in range( len(unsorted_list)-1 ):
		#If the number in the next index is less than the number in the current index
		if unsorted_list[index] > unsorted_list[index+1]:
			#Swap the two values at index and index+1
			unsorted_list[index], unsorted_list[index+1] = unsorted_list[index+1],unsorted_list[index]
			#Because we made a swap set swapped equal to true
			swapped = True


print(unsorted_list)