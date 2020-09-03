import math


def function(sum):
    a = 1
    b = 1
    c = 1

    while a <= sum:
        while b <= sum - a:
            while c <= sum - a - b:
                if a + b + c == sum:

                    if math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2):
                        print("%s * %s * %s = %s" % (a, b, c, a * b * c))
                c += 1
            c = 1
            b += 1
        b = 1
        c = 1
        a += 1


int = int(input("Give me ya num : "))

print(function(int))
