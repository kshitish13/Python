

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kshitish#0709",
    database="expense_manager"
)

connection.is_connected()

if connection.is_connected():
    print("Connected")
else:
    print("Not connected")


cursor = connection.cursor(dictionary=True)
cursor.execute("SELECT * FROM expenses")
expenses=cursor.fetchall()
print(type(expenses))

print(expenses)

for expense in expenses:
    print(expense)

connection.close()