from bank import value

def test_zero():
    assert value("Hello") == 0


def test_twenty():
    assert value("Hey") == 20

def test_hundred():
    assert value("Good Morning") == 100
