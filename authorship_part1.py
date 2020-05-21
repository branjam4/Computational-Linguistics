# -*- coding: utf-8 -*-
"""
template for authorship_part1.py
You can print out a table with one row for each files,
and the columns are the features, e.g.lexical diversity.
You can add your own features. Each feature should have its own function.

"""
'''
This project is about finding the authors signature through
these functions. This program finds the authors signature
that wrote it.
'''

import nltk
#from nltk.book import *
from nltk.corpus import gutenberg
from nltk.probability import FreqDist

emma = nltk.corpus.gutenberg.words('austen-emma.txt')
def lexical_div(file_id):
    '''
    compute the lexical diversity for a files in
    the gutenberg corpus.
    '''
    n_words = len(gutenberg.words(file_id))
    n_vocab = len(set(gutenberg.words(file_id)))
    l_div = n_vocab / n_words
    return l_div

def hapax_legomana_ratio(file_id):
    '''
    Hapax Legomana Ratio is similar to the lexical diversity Ratio in that it
    is a ratio using the total number of words as the denominator.
    The numerator for the Hapax Legomana Ratio is the number of words
    occurring exactly once in the text.
    '''
    fdist = FreqDist(gutenberg.words(file_id))
    words_that_occur_once = 0
    for word, frequency in fdist.most_common():
        if frequency == 1:
            words_that_occur_once = words_that_occur_once + 1
            total_number_of_words_in_text = len(gutenberg.words(file_id))
            hlr = words_that_occur_once / total_number_of_words_in_text
    return hlr

def avg_word_length(file_id): #this boy determines avg word length correctly #sig 1
    num_words = len(gutenberg.words(file_id))
    num_char = len(gutenberg.raw(file_id))
    avg_div = num_char / num_words
    return avg_div

def words_per_sent(file_id):
    num_words = len(gutenberg.words(file_id))
    num_sents = len(gutenberg.sents(file_id))
    return num_words / num_sents

def compare_signatures(sig1, sig2, weight):
    ''' Return a non-negative real number indicating the similarity of two
    linguistic signatures. The smaller the number the more similar the
    signatures. Zero indicates identical signatures.
    sig1 and sig2 are 6 element lists with the following elements
    0 : author name (a string)
    1 : average word length (float)
    2 : TTR (float)
    3 : Hapax Legomana Ratio (float)
    4 : average sentence length (float)
    5 : average sentence complexity (float)
    weight is a list of multiplicative weights to apply to each
    linguistic feature. weight[0] is ignored.
    '''
    n_fields = len(sig1)
    score = 0.0
    for i in range(1,n_fields):
        score += abs(sig1[i] - sig2[i])*weight[i]

    return score


if __name__ == '__main__':
    sigs = []
    weights = [11, 33, 50, 0.4, 4]
    for fid in gutenberg.fileids():
        # compute features, make a list of features
        features = []
        features.append(lexical_div(fid))
        features.append(words_per_sent(fid))
        features.append(hapax_legomana_ratio(fid))
        features.append(avg_word_length(fid))
        sigs.append(features)
        print(fid, features)
        #print(hapax_legomana_ratio(file_id))
