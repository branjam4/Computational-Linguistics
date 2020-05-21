'''
Rewrite the following loop as a list comprehension:
>>> sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
>>> result = []
>>> for word in sent:
...     word_len = (word, len(word))
...     result.append(word_len)
>>> result
[('The', 3), ('dog', 3), ('gave', 4), ('John', 4), ('the', 3), ('newspaper', 9)]
'''
sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
result = [(word, len(word)) for word in sent]
return(result)
q = 'Write a for loop to print out the characters of a string, one per line.'
def print_char(string):
    for char in string:
        print(char)
print_char(q)
p13 = """What is the difference between calling split on a string with no argument or
with ' ' as the argument, e.g. sent.split() versus sent.split(' ')? What
happens when the string being split contains tab characters, consecutive
space characters, or a sequence of tabs and spaces? (In IDLE you will need to
use '\t' to enter a tab character.)"""
print(p13)
a13 = """split() by default has \twhitespace as a delimiter. split(' ') only will use
a space as a     delimiter. Results in empty strings and '\\t' being listed in the split"""
print(a13)
print(a13.split(' '))
