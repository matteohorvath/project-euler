def doespalindrom(num):
    string = "{0}"
    string = string.format(num)
    length = int(len(string))
    counter = 0
    counterminus = -1

    if length % 2 == 0:
        while counter <= length / 2:
            if string[counter] != string[counterminus]:
                return False
            counter += 1
            counterminus -= 1
    else:
        return False
    return True


def biggestpalindrom(length):
    palindrom = 0
    num1 = ""
    counter = 0
    while counter < length:
        num1 += "9"
        counter += 1
    num2 = int(num1)
    num1 = int(num1)
    norm = int(num1)
    print(num1)
    print(num2)
    print(num1 * num2)
    while num1 > 0:
        while num2 > 0:
            if doespalindrom(num1 * num2):
                cont = num1 * num2
                if cont > palindrom:
                    palindrom = num1 * num2

            print("%s %s" % (num1, num2))
            num2 -= 1

        num2 = norm
        num1 -= 1
    return palindrom


input = int(input("Hi : "))

print(biggestpalindrom(input))
