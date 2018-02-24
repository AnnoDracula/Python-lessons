"""
Show words statistic case insensitive
"""
# from itertools import groupby
import collections

text = input().lower()
words = text.split()

for word, count in collections.Counter(words).most_common():
    print("{}: {}".format(word, count))

# key = lambda x: x.lower()
# words = sorted(words, key=key)
#
# for word, group in groupby(words, key):
#     print(word, len(list(group)))

