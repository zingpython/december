from random import randrange

random_list = []

for x in range(10):
	random_list.append( randrange( 1, 101 ) )

print(random_list)

highest = random_list[0]

for number in random_list:

	if number > highest:
		highest = number

print(highest)