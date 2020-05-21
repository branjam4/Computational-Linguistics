<<nltkbook>>
import pytest

def vocab_size(text):
    #assumes we only get a tokenized list
    try:
        clean_up = sorted([t.lower() for t in text if t.isalpha()])
        vocab = len(set(clean_up)) / len(clean_up)
        return vocab
    except ZeroDivisionError:
        return 0

def test_vocab_size():
    t1 = ['I', 'like', 'and', 'I', 'will', 'make', 'food', 'and', 'such', '.']
    t2 = ['You', 'you', 'they', 'tomato']
    t3 = ['.']
    t4 = []
    assert vocab_size(t1) == (7 / 9)
    assert vocab_size(t2) == (3 / 4)
    assert vocab_size(t3) == 0
    assert vocab_size(t4) == 0
