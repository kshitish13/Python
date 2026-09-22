import mysql.connector
from contextlib import contextmanager

@contextmanager
def get_db_cursor(commit=False):#by default commit is false whenever we insert or update the table we will do commit=true there
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kshitish#0709",
        database="expense_manager"
    )

    if connection.is_connected():
        print("Connected")
    else:
        print("Not connected")

    cursor = connection.cursor(dictionary=True)
    yield  cursor

    connection.commit() # whenever we are inserting something we need to commit
    cursor.close()
    connection.close()

def fetch_all_records():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()

        for expense in expenses:
            print(expense)




def fetch_expenses_for_date(expense_date):
    with get_db_cursor() as cursor:
        print("Date received:", expense_date)
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)


def insert_expense(expense_date,amount,category,notes):
    with get_db_cursor(commit=True) as cursor: # we do commit=True here as we are updating the table
        cursor.execute(
            "INSERT INTO expenses (expense_date,amount,category,notes) VALUES (%s,%s,%s,%s)",
            (expense_date,amount,category,notes)
        )

def delete_expense(expense_date):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))

if __name__ == "__main__":
    #fetch_all_records()
    #fetch_expenses_for_date("2024-08-02")
    insert_expense("2024-08-20", 300, "Food", "Panipuri")
    fetch_expenses_for_date("2024-08-20")