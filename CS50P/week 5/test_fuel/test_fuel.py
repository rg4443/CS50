from fuel import convert, gauge
import pytest

def test_convert():
    # Test valid input
    assert convert("1/2") == 50
    assert convert("3/4") == 75

    #raise errors
    with pytest.raises(ValueError):
        assert convert("w/e")

    with pytest.raises(ZeroDivisionError):
        assert convert("3/0")



def test_gauge():
    # Test percentage values
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"

