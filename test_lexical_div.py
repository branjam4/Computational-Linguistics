# [[file:~/Documents/org/Archive.org::test_lexical_div.py][test_lexical_div.py]]
#TODO: Test case- make sure "This" "this" and "this," are the same word.
def test_lexical_div_1():
    assert lexical_div('test_file_1.txt') == (12 / 13)
def test_lexical_div_2():
    assert lexical_div('test_file_2.txt') == (6 / 6)
# test_lexical_div.py ends here
