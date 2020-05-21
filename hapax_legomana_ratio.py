# [[file:~/Documents/org/Archive.org::test_hapax_legomana_ratio.py][test_hapax_legomana_ratio.py]]
def test_hlr_1():
    assert hapax_legomana_ratio('test_file_1.txt') == (11 / 13)
def test_hlr_2():
    assert hapax_legomana_ratio('test_file_2.txt') == (6 / 6)
# test_hapax_legomana_ratio.py ends here
