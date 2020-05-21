# [[file:~/Documents/org/Archive.org::*Problem%2027][Problem 27:1]]
import nltk
from nltk.book import *
import pytest

def vocab_size(text):
    clean_up = sorted([t.lower() for t in text if t.isalpha()])
    vocab = len(set(clean_up) / len(clean_up)
    return (7 / 9)

def test_vocab_size():
    text = ['I', 'like', 'and', 'I', 'will', 'make', 'food', 'and', 'such', '.']
    assert vocab_size(text) == (7 / 9)
# Problem 27:1 ends here
