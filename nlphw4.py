import re
from re import findall
regexa = r'[a-zA-Z]+'
print(findall(regexa, 'Doctor doctor'))
regexb = r'[A-Z][a-z]*'
print(findall(regexb, 'Csharp'))
regexc = r'p[aeiou]{,2}t'
print(findall(regexc, 'pout'))
regexd = r'\d+(\.\d+)?'
print(findall(regexd, '123.456'))
regexe = r'([^aeiou][aeiou][^aeiou])*'
print(findall(regexe, 'bat'))
regexf = r'\w+|[^\w\s]+'
print(findall(regexf, '   two-fold   '))
regexg = r'\w+(ing|ed)\b'
print(findall(regexg, 'working.'))
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
import re
from re import findall
regex = r'([do]+)([n\'t]+)|(\w+)'
print(findall(regex, 'don\'t really want to finding don\'t'))
import re
#Write a function to convert a word to Pig Latin.
def word_to_PL(word):
    '''
    def test_word_to_PL():
        assert word_to_PL('Pig') == 'Igpay'
        assert word_to_PL('queen') == 'eenquay'
        assert word_to_PL('style') == 'ylestay'
    '''
    if len(word) < 2:
        return(word + 'ay')
    ''' keep qu together (i.e. so that quiet becomes ietquay)
    detect when y is used as a consonant (e.g. yellow)
    vs a vowel (e.g. style). '''
    r = re.findall(r'(qu|Qu|[^aeiouyAEIOUY]+|[^aeiouAEIOU]*)([\w]+)', word)
    e = ''.join(r[0][1].strip() + r[0][0].strip().lower() + 'ay')

    #Extend it further to preserve capitalization
    if word.istitle():
        return(e.title())

    return(e)

# Write code that converts text, instead of individual words.
def text_to_PL(text):
    t = text.split()
    r = [word_to_PL(w) for w in t if w.isalpha()]
    e = ' '.join(r)
    return(e)
print(text_to_PL('Pig Latin is a simple transformation of English'))
words = """
Write code to initialize a two dimensional array of sets called word_vowels and
process a list of words, adding each word to word_vowels [l] [v] where l is the
length of the word and v is the number of vowels it contains.
"""
lst_words = words.lower().split()
'''
Algorithm:
1. make array of sets called word_vowels.
2. For each word in the list, get the length of that word...
3. ...and that word's vowel count.
4. Find the index matching the length of the word for the row,
and the amount of vowels in the word for column, and add that word to it.
'''

#1
word_vowels = [[set() for i in range(15)] for j in range(15)]

for word in lst_words:
    l = len(word) #2
    vowel_count = len([v for v in word if v.lower() in 'aeiou']) #3
    word_vowels[l][vowel_count].add(word) #4
print(word_vowels)
