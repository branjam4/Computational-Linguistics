from nltk.corpus import brown

brown_tagged = brown.tagged_words(tagset='modals')
sort_bt = sorted(set(brown_tagged))
print(sort_bt)
