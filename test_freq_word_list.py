from nltk.corpus import gutenberg as berg
from nltk import FreqDist
import pytest
'''
  Create a list of all words that start with 'wh',
  convert words to lower case, and print the frequency distribution for those
  words. '''
wh_words = [w.lower() for w in berg.words('austen-emma.txt') if w.startswith('wh')]
print(FreqDist(wh_words).most_common())

#b) Write a function that takes a list of words and returns a FreqDist
def function_b(word_list):
    if word_list isinstance[list]:
        return(FreqDist(word_list))
    else:
        raise TypeError('This function requires a list')
    #TODO: check that list contains only words

def test_function_b():
    assert 'FreqDist' in str(type(function_b(['test', 'list'])))
