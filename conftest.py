import os
#import shutil
from nltk.corpus import PlaintextCorpusReader
import pytest
#from authorship_part1 import *

@pytest.fixture(scope="session")
def test_directory(tmpdir_factory):
    #make test files
    test_file_1 = """This is a sentence you can be proud of.\ni can see everything."""
    #test_file_2 = """Wow! Amazing!! Dr. Clever, they're here..."""
    #corpus = [test_file_1, test_file_2] #bundle texts into corpus

    #put texts in pytest temp directory
    corpus_location = tmpdir_factory.mktemp("test_corpus").join("test_file_1.txt")
    corpus_location.write(test_file_1)

    #creates new files in a folder called "test_corpus based on "test_file_#" text
    #file_number = 1
    #for text in corpus:
    #writes the contents of test_file_# to test_file_#.txt
    #test_file_string = "test_file_" + str(file_number) + ".txt" #e.g.: "test_file_1"
    #tfs = corpus_location.join(test_file_string)
    #tfs.write_text(text, encoding='utf8')
    #go to next test_file
    #file_number += 1
    return corpus_location
'''
def teardown_module(module):
    #delete test files and folder with shell-util: remove tree
    testCorpus = None
    corpus_location = 'test_corpus/'
    shutil.rmtree(corpus_location)
'''
