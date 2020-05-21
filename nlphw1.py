result=""": ============================= test session starts ==============================
: platform linux -- Python 3.7.1, pytest-4.0.1, py-1.7.0, pluggy-0.8.0
: rootdir: /home/branjam4/Documents/org, inifile:
: collected 1 item
:
: test_vocab.py .                                                          [100%]
:
: ========================== 1 passed in 22.94 seconds ===========================
"""
import nltk
from nltk.book import *

word_count = len(text1)
distinct_word_count = len(set(text1))
print("words in text2 = " + str(word_count))
print("distinct words = " + str(distinct_word_count))
import nltk
from nltk.book import *

vocab = sorted(set(sent1 + sent2 + sent3 + sent4 + sent5 + sent6 + sent7 + sent8))
print("Sorted vocabulary for sents 1-8:")
print(vocab)
import nltk
from nltk.book import *

words = text2[-2:]
print("last two words in text 2:")
print(words)

import nltk
from nltk.book import *

ize_words = [w for w in text6 if w.endswith('ize')]
print(ize_words)
import nltk
from nltk.book import *
print("here are words containing the letter 'z' in text6:")
z_words = [w for w in text6 if 'z' in w]
print(z_words)
import nltk
from nltk.book import *
print("here are words containing the letters 'pt' in text6:")
pt_words = [w for w in text6 if 'pt' in w]
print(pt_words)
import nltk
from nltk.book import *
print("here are titlecase words in text6:")
titlecase_words = [w for w in text6 if w.istitle()]
print(titlecase_words)
sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
print(sent)
#Now write code to perform the following tasks:

[print(w + ' begins with sh') for w in sent if w.startswith('sh')]
[print(w + ' is longer than 4 characters') for w in sent if len(w) > 4]

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
print(result)
