# [[file:~/Documents/org/Archive.org::test_avg_word_length.py][test_avg_word_length.py]]
from avgWordLength import *
#We can choose whether to include or exclude punctuation and whitespace.
def test_awl_1(test_directory):
    #expected_awl = ((4 + 2 + 1 + 8 + 3 + 3 + 2 + 5 + 2 + 1 + 3 + 3 + 10) / 13)
    expected_awl = 60/13 #assuming we include whitespace/punctuation
    #assert avg_word_length('test_file_1.txt', test_directory) == expected_awl
    assert avg_word_length('test_file_1.txt', test_directory) == expected_awl
#def test_awl_2(test_directory):
    #assert avg_word_length('test_file_2.txt', str(test_directory)) == ((3 + 7 + 2 + 6 + 6 + 4) / 6)
    #assert avg_word_length('test_file_2.txt') == (42 / 6) #assuming we include whitespace/punctuation
# test_avg_word_length.py ends here
