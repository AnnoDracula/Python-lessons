"""
Find indexes of the simple continued fraction
"""
num = input("Number")
n = num.split("/")
a = int(n[0])
b = int(n[1])
result = []


def calculation(a, b, result):
    var = divmod(a, b)
    result.append(var[0])
    a = b
    b = var[1]
    if b == 0:
        return result
    else:
        return calculation(a, b, result)


unswer = calculation(a, b, result)
print(" ".join(str(i) for i in unswer))
