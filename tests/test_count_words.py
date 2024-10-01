import pytest
from lib.count_words import *

# Empty string
def test_not_string():
    with pytest.raises(Exception) as e:
        error_check = count_words(9)
        assert str(e.value) == "Input must be a string!"

def test_empty_string():
    assert count_words("") == 0

# One word
def test_one_word():
    assert count_words("one") == 1

# Two words
def test_two_words():
    assert count_words("Hello you") == 2

# Three words
def test_three_words():
    assert count_words("Go awway, you!") == 3

# Five words
def test_five_words():
    assert count_words("Hello my friend, you're great!") == 5
# Ten words
def test_twelve_words():
    assert count_words("You're so on the money about Stacey, she's definitely giving side eye") == 12
# 15 words
def test_15_words():
    assert count_words("hello hello hello hello hello he ju isj jhu ki ja lol wrte ujru wrte") == 15

def test_ignores_numbers():
    assert count_words("Hello my 15 friends") == 3

def test_ignore_double_space():
    assert count_words("Hello  my  friends") == 3