import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

# cursor.execute(""" CREATE TABLE student(
# 	id INTEGER PRIMARY KEY,
# 	name VARCHAR(50),
# 	gpa REAL)""")

# connection.commit()

name = "Matthew"

cursor.execute(" INSERT INTO student(name,gpa) VALUES ( ?,? ) ", (name, 3.3) )

connection.commit()

cursor.execute(" SELECT * FROM student")

student_list = cursor.fetchall()

print(student_list)


connection.close()