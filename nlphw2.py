data=[["ʃ", "SH", "wish"], ["θ", "TH", "breath"], ["æ", "AE", "sat"], ["ɑ", "AA", "calm"], ["ð", "DH", "breathe"], ["ə", "AX", "southern"], ["ɛ", "EH", "net"], ["ɔ", "AO", "bow"], ["ŋ", "NG", "wing"]]
import nltk
from nltk.corpus import cmudict as cmu
table = data
import nltk
from nltk.corpus import cmudict as cmu
print("The CMU Pronouncing Dictionary contains multiple pronunciations for certain words.")
print("How many distinct words does it contain?")
words = [w[0] for w in cmu.entries()]
distinct_words = set(words)
distinct_word_count = len(set(words))
print(distinct_word_count)
#What fraction of words in this dictionary have more than one possible pronunciation?
dup_words = nltk.FreqDist(words).most_common()
dup_words_count = [d[0] for d in dup_words if d[1] > 1]
return(str(len(dup_words_count)) + ' / ' + str(distinct_word_count))
#Note that if e is an entry in the dictionary, e[0] will give you just the word.  Figure out a way to use set().
import nltk
from nltk.corpus import cmudict as cmu
#use the CMU dictionary to find the number of phones in
to_lookup = ['handsome', 'clever', 'and', 'rich', 'with', 'a', 'comfortable', 'home']
''' You can look up each word in the CMU dictionary, but some may have more than
one pronunciation.  Choose the first one. '''
lookup_with_cmu = {w[0]: w[1] for w in cmu.entries() if w[0] in to_lookup}
counts = [(w, len(lookup_with_cmu[w])) for w in lookup_with_cmu]
return(counts)
