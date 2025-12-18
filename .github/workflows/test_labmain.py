# test_labmain.py
from labmain import sub

def test_sub():
    assert sub(8, 4) == 4
    assert sub(10, 5) == 5
    assert sub(0, 0) == 0
