small = input("Enter the number of bottles less than 1L: ")

large = input("Enter the number of bottles more than 1L: ")

total = ( int(small)  * 0.1 ) + ( int(large) * 0.25 )

print("Your total is $" + format(total, ".2f") )
