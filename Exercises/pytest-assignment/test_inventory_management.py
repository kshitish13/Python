import pytest
from inventory_management import Inventory

def test_add_stock():
    inventory = Inventory()
    inventory.add_stock("Apple", 10)
    assert inventory.stock["Apple"] == 10
    inventory.add_stock("Apple", 10)
    assert inventory.stock["Apple"] == 20
    assert len(inventory.stock) == 1

def test_remove_stock():
    inventory=Inventory()
    inventory.add_stock("Apple",20)
    inventory.remove_stock("Apple",15)
    assert inventory.stock['Apple']==5
    with pytest.raises(ValueError):
        inventory.remove_stock("Apple",10)

def test_check_availability():
    inv = Inventory()
    inv.add_stock("widget", 5)
    assert inv.check_availability("widget", 3) is True
    assert inv.check_availability("widget", 6) is False
