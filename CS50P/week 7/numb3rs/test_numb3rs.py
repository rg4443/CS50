import pytest
from numb3rs import validate

def test_valid_ipv4():
    assert validate("192.168.1.1") is True

def test_invalid_ipv4():
    assert validate("256.0.0.1") is False

def test_invalid_format():
    assert validate("1.1.1.1.1") is False

def test_valid_ipv4_with_five_bytes():
    assert validate("192.168.1.1.1") is False

if __name__ == "__main__":
    pytest.main()
