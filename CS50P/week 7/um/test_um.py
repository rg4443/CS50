import pytest

from um import count

def test_words():
    assert count("Mum") == 0

def test_whitespace():
    assert count("   um  ") == 1

def test_case_sensitive():
    assert count("UM") == 1
