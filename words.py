"""
Show words lengths statistic
"""
from itertools import groupby

sentence = input()
words = sentence.split(" ")

words_len = []
for i in range(len(words)):
    words_len.append(len(words[i]))

min_len = min(words_len)
sort_len = []
index = len(words_len)
while index != 0:
    sort_len.append(min(words_len))
    words_len.remove(min(words_len))
    index = len(words_len)

# loop
result = {}
n = 0
while n < len(sort_len):
    amount = 0
    key = sort_len[n]
    k = n
    while k < len(sort_len) and key == sort_len[k]:
        amount = amount + 1
        k = k + 1
    n = k
    result[key] = amount


# recursion
def amount_calc(kee, ind, sort_array, res):
    amount1 = 0
    while ind < len(sort_array):
        if kee == sort_array[ind]:
            amount1 = amount1 + 1
        else:
            res[kee] = amount1
            kee = sort_array[ind]
            return amount_calc(kee, ind, sort_array, res)
        ind = ind + 1
    res[kee] = amount1
    return res


# groupby
for group, value in groupby(sort_len):
    print(group, ":", len(list(value)))

print(amount_calc(sort_len[0], 0, sort_len, {}))
print(result)
