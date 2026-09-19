import pytest
from src.bank import BankAccount

def test_create_account():
    account = BankAccount("Kshitij",100)
    assert account.owner== "Kshitij"
    assert account.balance == 100

# Test for depositing money
def test_deposit():
    account =BankAccount("Kshitish")
    account.deposit(100)
    account.deposit(200)
    assert account.balance == 300

    with pytest.raises(ValueError):
        account.deposit(-100)

# Test for withdrawing money
def test_withdraw():
    account =BankAccount("Kshitij",1000)
    account.withdraw(100)
    assert account.balance==900

    with pytest.raises(ValueError):
        account.withdraw(2000)

# Test for checking the balance
@pytest.mark.skip(reason="Need to be implemented")
def test_balance():
    account =BankAccount("Kshitij",100)
    assert account.balance==100

