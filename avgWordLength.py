def avg_word_length(file_id, corpus_dir):
    from nltk.corpus import PlaintextCorpusReader
    try:
        corpus_location = corpus_dir.dirname
        gutenberg = PlaintextCorpusReader(corpus_location, '.*') #
    except:
        from nltk.corpus import gutenberg
    num_words = len(gutenberg.words(file_id))
    num_char = len(gutenberg.raw(file_id))
    avg_div = num_char / num_words
    return avg_div
