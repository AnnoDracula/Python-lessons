"""
Implement caesar cipher
"""

abc = ' abcdefghijklmnopqrstuvwxyz'
index = input()
step = int(index)
phrase = input()
phrase = phrase.strip()
result = ""

i = 0
while i in range(len(phrase)):
    ind = step
    a = 0
    while phrase[i] != abc[a]:
        a = a+1
    while a+ind > len(abc)-1 or a+ind < 0:
        if a+ind > len(abc)-1:
            ind = ind - len(abc)
        if a+ind < 0:
            ind = len(abc)+ind
    result = result+abc[a+ind]
    i = i+1

print("Result:", '"{}"'.format(result))

