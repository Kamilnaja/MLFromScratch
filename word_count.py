from collections import defaultdict

document = ['hello', 'world', 'hello', 'mars', 'hello', 'world']

word_count = defaultdict(int)
for word in document:
    word_count[word] += 1
