import pytest
from working import convert

def test_print_hour():
    assert convert("10:00 PM to 8:00 AM") == "22:00 to 08:00"

def test_raise_value_error():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
def test_str():
    with pytest.raises(ValueError):
        convert("to")
def test_range():
    with pytest.raises(ValueError):
        convert("40:60 to 50:60")
