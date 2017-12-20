import sqlite3
import csv

class Model:

	def __init__(self):
		self.connection = sqlite3.connect("contact.db")

		self.cursor = self.connection.cursor()

	def createTables(self):
		self.cursor.execute( """ CREATE TABLE user(
			id INTEGER PRIMARY KEY,
			name VARCHAR(50),
			country VARCHAR(50),
			email VARCHAR(100) )""" )

		self.cursor.execute( """ CREATE TABLE phone_number(
			id INTEGER PRIMARY KEY,
			phone VARCHAR(20),
			user_id INTEGER,
			FOREIGN KEY (user_id) REFERENCES user(id)) """)

		self.connection.commit()

	def closeConnection(self):
		self.connection.close()

	def insertUser(self, name, email, country):
		self.cursor.execute("INSERT INTO user(name,email,country) VALUES (?,?,?) ", (name, email, country) )

		self.connection.commit()

	def insertPhone(self, user_id, phone):
		self.cursor.execute("INSERT INTO phone_number(phone,user_id) VALUES (?,?) ", (phone, user_id) )

		self.connection.commit()

	def getLastRowID(self):
		return self.cursor.lastrowid

	def selectAllUsers(self):
		self.cursor.execute("SELECT * FROM user")

		return self.cursor.fetchall()

	def selectAllPhones(self):
		self.cursor.execute("SELECT * FROM phone_number")

		return self.cursor.fetchall()

	def selectPhonesByUser(self, user_id):
		self.cursor.execute("SELECT * FROM phone_number WHERE user_id=?", (user_id,) )

		return self.cursor.fetchall()

	def readFile(self, filename):
		with open(filename, "r") as csv_file:
			lines = csv.reader(csv_file)

			new_lines = []

			for line in lines:
				new_lines.append(line)

			return new_lines


#Only run this code when directly running this file
if __name__ == "__main__":
	#Create the tables in the database contact.db when you directly run model.py
	print(__name__)
	my_model = Model()
	my_model.createTables()
	my_model.closeConnection()