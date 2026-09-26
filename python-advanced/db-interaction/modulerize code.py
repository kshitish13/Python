import mysql.connector

def get_db_cursor():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOURPASSWORD",
        database="expense_manager"
    )

    if connection.is_connected():
        print("Connected")
    else:
        print("Not connected")

    cursor = connection.cursor(dictionary=True)
    return connection,cursor

def fetch_all_customers():
    connection,cursor=get_db_cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    for expense in expenses:
        print(expense)

    cursor.close()
    connection.close()


def fetch_expenses_for_date(expense_date):
    connection,cursor = get_db_cursor()
    print("Date received:", expense_date)
    cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
    expenses = cursor.fetchall()
    for expense in expenses:
        print(expense)

    cursor.close()
    connection.close()

if __name__ == "__main__":
    #fetch_all_customers()
    fetch_expenses_for_date("2024-08-02")



'''Here also some code are repeating like
    cursor.close()
    connection.close()
so lets modulerize these in modulerize_2.py file'''


# or

# def get_db_connection():
#     connection = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="Kshitish#0709",
#         database="expense_manager"
#     )
#
#     return connection
#
#
# def fetch_all_expenses():
#     connection = get_db_connection()
#
#     cursor = connection.cursor(dictionary=True)
#
#     cursor.execute("SELECT * FROM expenses")
#
#     expenses = cursor.fetchall()
#
#     cursor.close()
#     connection.close()
#
#     return expenses
#
#
# expenses = fetch_all_expenses()
#
# for expense in expenses:
#     print(expense)
#
