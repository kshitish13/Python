import pytest
from customers_db import CustomersDB

def test_insert_customer():
    db=CustomersDB()
    db.connect()

    db.insert_customer("Kshitij","kshitij@gmail.com")
    customer=db.get_customer_by_name("Kshitij")

    assert customer is not None
    assert customer['name'] == "Kshitij"
    assert customer['email'] == "kshitij@gmail.com"

    db.clear_customers()
    db.close()


def test_get_all_customers():
    db=CustomersDB()
    db.connect()

    db.insert_customer("Kshitij","kshitij@gmail.com")
    db.insert_customer("Kshitish","kshitish@gmail.com")

    customers=db.get_all_customers()
    assert len(customers)==2

    db.clear_customers()
    db.close()


'''here we are repeating the 
db=CustomersDB()
db.connect()
in every function so to avoid that we have a method pytest fixtures
which we will see in test_customers_db_2.py file'''
