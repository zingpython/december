import csv
import sqlite3


connection = sqlite3.connect("contacts.db")

cursor = connection.cursor()

# cursor.execute(""" CREATE TABLE user(
# 						id INTEGER PRIMARY KEY,
# 						name VARCHAR(50),
# 						country VARCHAR(50),
# 						email VARCHAR(100) ) """)

# connection.commit()

# cursor.execute(""" CREATE TABLE phone_number(
# 						id INTEGER PRIMARY KEY,
# 						phone VARCHAR(20),
# 						user_id INTEGER,
# 						FOREIGN KEY (user_id) REFERENCES user(id) ) """)

# connection.commit()

with open("employees.csv", "r") as csv_file:
	lines = csv.reader( csv_file )
	for line in lines:
		cursor.execute("INSERT INTO user(name,country,email) VALUES (?,?,?) ", (line[0], line[5], line[4] ) )

		last_id = cursor.lastrowid

		cursor.execute("INSERT INTO phone_number(phone,user_id) VALUES (?,?) ", (line[1], last_id) )
		cursor.execute("INSERT INTO phone_number(phone,user_id) VALUES (?,?) ", (line[2], last_id) )
		cursor.execute("INSERT INTO phone_number(phone,user_id) VALUES (?,?) ", (line[3], last_id) )
		
		connection.commit()

connection.close()