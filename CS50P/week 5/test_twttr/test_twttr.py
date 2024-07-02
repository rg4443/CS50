import pytest

from twttr import shorten

def test_lower():
    assert shorten("hello") == "hll"
    assert shorten("world") == "wrld"
    assert shorten("Goodbye") == "Gdby"

def test_upper():
    assert shorten("HELLO") == "HLL"
    assert shorten("RAFAEL") == "RFL"
