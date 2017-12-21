import sqlite3

class Model:

	def __init__(self):
		self.connection = sqlite3.connect("shopping_list.db")

		self.cursor = self.connection.cursor()

	def createTable(self):
		self.cursor.execute("""CREATE TABLE shopping_list(
									id INTEGER PRIMARY KEY,
									item VARCHAR(100),
									checked VARCHAR(9)) """)

		self.connection.commit()

	def closeConnection(self):
		self.connection.close()

	def insertItem(self, item):
		self.cursor.execute("INSERT INTO shopping_list(item, checked) VALUES (?,?)", (item, "UNCHECKED"))

		self.connection.commit()

	def selectAllItems(self):
		self.cursor.execute("SELECT * FROM shopping_list")

		return self.cursor.fetchall()

	def updateChecked(self, id, new_checked):
		self.cursor.execute("UPDATE shopping_list SET checked=? WHERE id=?", (new_checked,id) )

		self.connection.commit()


if __name__ == "__main__":
	my_model = Model()
	my_model.createTable()
	my_model.closeConnection()