"""
Convert roman number to decimal number
"""
num = input("Print Number")
d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

if num.isalpha():
    i = 0
    while i < len(num):
        if num[i] not in d:
            print("Invalid number")
            exit()
        else:
            i = i+1
else:
    print("Invalid number")
    exit()

i = 0
array = []
while i < len(num):
    array.append(d[num[i]])
    i = i + 1

number = array[len(array)-1]
m = len(array) - 1
while m != 0:
    if (array[m] > array[m -1]):
        number = number - array[m - 1]
    else:
        number = number+ array[m -1]
    m = m - 1

print(number)