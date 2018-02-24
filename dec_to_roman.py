"""
Convert decimal number (0 <= x <= 4000) to roman number
"""
num = input("Print Number a <= 4000\n")


class InvalidNumberError(Exception):
    pass


d = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
array = [1000, 500, 100, 50, 10, 5, 1]


def check_value(num):
    if num.isalpha():
        raise InvalidNumberError("Not a number")

    number = int(num)
    if number > 4000:
        raise InvalidNumberError("Too large number")


def dec_to_rom(num):
    check_value(num)

    number = int(num)

    kee_ar = []
    i = len(num)
    while i > 0 and number > 0:
        divisor = 10 ** (i - 1)
        if (number - number % divisor) in d:
            kee_ar.append(d[number - number % divisor])
        else:
            k = 0
            while number < array[k]:
                k = k + 1
            if k == 0:
                m = (number - number % divisor) // array[k]
                while m != 0:
                    kee_ar.append(d[array[k]])
                    m = m - 1
            else:
                r1 = array[k - 1] - (number - number % (10 ** (len(str(number)) - 1)))
                if r1 == 1 or r1 == 10 or r1 == 100:
                    kee_ar.append(d[r1])
                    kee_ar.append(d[array[k - 1]])
                else:
                    kee_ar.append(d[array[k]])
                    r2 = number - array[k]
                    m1 = r2 // 10 ** (len(str(r2)) - 1)
                    while m1 != 0:
                        kee_ar.append(d[10 ** (len(str(r2)) - 1)])
                        m1 = m1 - 1

        number = number % divisor
        i = len(str(number))
    return "".join(kee_ar)


try:
    print(dec_to_rom(num))
except InvalidNumberError as ex:
    print("Input correct value. " + str(ex))
