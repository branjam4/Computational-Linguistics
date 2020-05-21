import os
import shutil
from nltk.corpus import PlaintextCorpusReader
#from authorship_part1 import *

def test_create_directory(tmpdir):
    #make test files
    test_file_1 = """This is a sentence you can be proud of.\ni can see everything."""
    test_file_2 = """Wow! Amazing!! Dr. Clever, they're here..."""
    corpus = [test_file_1, test_file_2] #bundle texts into corpus

    #make directory to put texts in with os: make directory
    corpus_location = 'test_corpus/' #may need to be checked on other operating systems
    tmpdir.mkdir(corpus_location)

    #creates new files in a folder called "test_corpus based on "test_file_#" text
    file_number = 1
    for text in corpus:
        test_file_string = corpus_location + "test_file_" + str(file_number) #e.g.: "test_file_1"

        #writes the contents of test_file_# to test_file_#.txt
        file = open(test_file_string + '.txt','w')
        file.write(text)
        assert file.read() == text
        file.close()

        #go to next test_file
        file_number += 1
'''
def teardown_module(module):
    #delete test files and folder with shell-util: remove tree
    testCorpus = None
    corpus_location = 'test_corpus/'
    shutil.rmtree(corpus_location)
'''
