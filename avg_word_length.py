def avg_word_length(file_id):
    num_words = len(gutenberg.words(file_id))
    num_char = len(gutenberg.raw(file_id))
    avg_div = num_char / num_words
    return avg_div
