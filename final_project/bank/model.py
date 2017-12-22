import sqlite3

class Bank:

	def __init__(self):
		self.connection = sqlite3.connect("bank.db")

		self.cursor = self.connection.cursor()

	def createTables(self):
		self.cursor.execute('''CREATE TABLE user(
			id INTEGER PRIMARY KEY,
			username VARCHAR(256),
			password VARCHAR(256),
			address VARCHAR(256),
			phonenumber VARCHAR(256),
			email VARCHAR(256),
			balance REAL
			) ''')

		self.connection.commit()

	def closeConnection(self):
		self.connection.close()

	def insertRow(self, username, password, address, phonenumber, email):
		self.cursor.execute("INSERT INTO user(username,password,address,phonenumber,email,balance) VALUES (?,?,?,?,?,?)", (username,password,address,phonenumber,email, 0.0))
		self.connection.commit()

	def updateBalance(self, id, balance):
		self.cursor.execute("UPDATE user SET balance=? WHERE id=?",(balance,id) )
		self.connection.commit()

	def selectAll(self):
		self.cursor.execute("SELECT * FROM user")
		return self.cursor.fetchall()

	def selectById(self, id):
		#NOTE: when a tuple contains one item pytho will not treat it as a tuple
		#In order to force python to treat as a tuple put a comma at the end of the tuple
		self.cursor.execute("SELECT * FROM user WHERE id=?", (id,) )
		#														^ This comma makes it into a tuple
		return self.cursor.fetchone()


if __name__ == "__main__":
	database = Bank()
	database.createTables()
	database.closeConnection()