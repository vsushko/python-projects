from collections import defaultdict
from collections import Counter
txt = "This is a vast world you can't traverse world in a day"

counts = Counter(txt.split())

print(counts)

# query for the most frequent words
print(counts.most_common(2))

# get the frequency of a specific word
print(counts['world'])

# get back the total number of occurrences
print(sum(counts.values()))

print(Counter(["hello", "world"]) + Counter(["hello", "you"]))

print(Counter(["hello", "world"]) & Counter(["hello", "you"]))

# How it works
counts = dict(hello=0, world=0, nice=0, day=0)

for word in 'hello world this is a very nice day'.split():
    if word in counts:
        counts[word] += 1

counts

for word in 'hello world this is a very nice day'.split():
    counts[word] = counts.get(word, 0) + 1

counts

counts = defaultdict(int)
for word in 'hello world this is a very nice day'.split():
    counts[word] += 1

counts

import os
from collections import ChainMap

commnad_line_options = {}
config_file_options = {'optname': 'somevalue'}

options = ChainMap(commnad_line_options, os.environ, config_file_options)
value = options.get('optname', 'default-value')
print(value)

options = ChainMap(commnad_line_options, os.environ, config_file_options, defaultdict(lambda: 'default-value'))
value = options['optname']
value2 = options['other-option']

value
value2

