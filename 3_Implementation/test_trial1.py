import pytest
from bank_management import Depositwithdraw
obj = Depositwithdraw(1000, 200)
def _init_Deposit():
    k = obj._init_Deposit()
    assert k == None

