from plates import is_valid

def test_alpha():
    assert is_valid("1234") == False
    assert is_valid("12AB") == False
    assert is_valid("AB1") == True

def test_numplace():
    assert is_valid("ABCD1") == True
    assert is_valid("ABCD01") == False

def test_midnum():
    assert is_valid("AB1CD") == False
    assert is_valid("AB01CD") == False

def test_special():
    assert is_valid("AB!CD") == False
    assert is_valid("AB CD") == False
    assert is_valid("AB(CD)") == False
    assert is_valid("AB,CD") == False
    assert is_valid("AB;CD") == False
    assert is_valid("AB'CD") == False
