from lib.make_snippet import *

def test_empty_string():
    assert make_snippet("") == ""


def test_snip_one_word():
    assert make_snippet("one") == "one"

def test_snip():
    assert make_snippet("Hello to all the people") == "Hello to all the people"
    

def test_snip_punctuation():
    assert make_snippet("Hello, my name is John") == "Hello, my name is John"

def test_snip_long():
    assert make_snippet("Hello, my name is John Procter") == "Hello, my name is John..."
