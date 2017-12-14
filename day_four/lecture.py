
# def add(number1, number2):
# 	sum = number1 + number2

# 	return sum

# user_input_1 = input("Enter a word:")
# user_input_2 = input("Enter a word:")

# result = add( user_input_1, user_input_2 )

# print(result)


class Car:
	#make will be a string that hold the make of a car
	#model will be a string that holds the model of a car
	#color will be a string that holds the color of a car
	#hp will be a integer that holds the horse power of a car

	def __init__(self, make, model, color, hp):
		self.make = make
		self.model = model
		self.color = color
		self.hp = hp

	def getColor(self):
		return self.color

	#Color needs a set because I expect my color to be changed
	def setColor(self, color):
		self.color = color

	# make and model do not need set function because I do not expect make and model to change
	def getMake(self):
		return self.make

	def getModel(self):
		return self.model

	def getHP(self):
		return self.hp

	#HP needs a set because I could change my horse power sometime in the future
	def setHP(self, hp):
		self.hp = hp

	#mudSplatter is neither a set nor a get but it is still a function of my classk
	def mudDrive(self):
		self.color = "Mud splattered " + self.color


my_car = Car("Toyota","Carolla","Red",200)

print( my_car.getColor() )

my_car.setColor("Blue")

print( my_car.getColor() )

my_car.mudDrive()

print( my_car.getColor() )

print(my_car.make)