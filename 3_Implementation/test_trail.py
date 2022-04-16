import pytest
from bank_management import User
obj = User(1, "Pratibha", 1000, "SA")
def createuser():
    k = obj.createuser()
    assert k == None

