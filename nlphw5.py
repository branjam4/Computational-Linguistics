'''
The goal of this problem is to use a dictionary to construct the equivalent
of a frequency distribution. Given a set of words, count the number of vowels
in each word. Create a dictionary where the key is a word and the value is
the number of vowels in that word. You can convert each word to lower case
first.
'''
def count_vowels(vocab):
    key = {v.lower() for v in vocab}
    keys = sorted(key) #I just wanted to sort
    vowel_counts = [len([v for v in word if v in 'aeiouAEIOU']) for word in keys]
    dict_vowel_counts = {k:v for (k,v) in zip(keys, vowel_counts)}
    return(dict_vowel_counts)
cv = ['one', 'two', 'three', 'fours', 'fives']
cv_vowel_count = count_vowels(cv)
print(cv_vowel_count['one'])
def longest_word_len(lst_words):
    '''
    Given a list of words, write a function to find and return the length of the
    longest word.
    '''
    key = {v.lower() for v in lst_words}
    keys = sorted(key) #I just wanted to sort
    counts = [len([v for v in word]) for word in keys]
    dict_word_counts = {k:v for (k,v) in zip(keys, counts)}
    return(max(dict_word_counts.values()))
print(longest_word_len(cv))

def longest_words(lst_words):
    '''
    Given a list of words, write a function to find all of the longest words, and
    return a set of those words.
    '''
    key = {v.lower() for v in lst_words}
    keys = sorted(key) #I just wanted to sort
    counts = [len([v for v in word]) for word in keys]
    dict_word_counts = {k:v for (k,v) in zip(keys, counts)}
    longest_word_length = max(dict_word_counts.values())
    long_words = [w for w in dict_word_counts if len(w) == longest_word_length]
    return(long_words)
print(longest_words(cv))
import nltk
from nltk.tokenize import word_tokenize
sent_1 = "one day I was walking through the woods and found a squirrel."
sent_2 = "tomorrow store green friendship running the layer"
sent_3 = "colorless green ideas sleep furiously"
sent_4 = "the dog saw the man in the park"
t1 = word_tokenize(sent_1)
t2 = word_tokenize(sent_2)
t3 = word_tokenize(sent_3)
t4 = word_tokenize(sent_4)
pos1 = nltk.pos_tag(t1)
pos2 = nltk.pos_tag(t2)
pos3 = nltk.pos_tag(t3)
pos4 = nltk.pos_tag(t4)
print(pos1 + pos2 + pos3 + pos4)
'''
For the grammatical sentences you wrote, create parse trees using either
nltk.app.rdparser() or
nltk.RecursiveDescentParser(grammar)
In either case, you should create a grammar, using the tags from pos_tag()
'''
'''
From Brandon:
Briefly went through this in an interactive shell,
but I know to use nltk.CFG.fromstring("" )
'''
'''
The goal is to compare the Porter and Lancaster stemmers.
This involves running them on a text and looking for differences.
'''
#porter = nltk.PorterStemmer()
#porter_stems = [porter.stem(t) for t in tokens]
#lancaster = nltk.LancasterStemmer()
#lancaster_stems = [lancaster.stem(t) for t in tokens]

#print the words that are stemmed differently for the two
print("one: one vs. on")
print("was wa vs. was")
