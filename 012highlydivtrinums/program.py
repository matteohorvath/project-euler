def get_factors(n):
    factors = []
    for x in range(n + 1):
        if x != 0:
            if n % x == 0:
                if x not in factors:
                    factors.append(x)
    print("%s %s" % (n, len(factors)))
    return len(factors)


def func(n):
    counter = 0
    turn = 0
    while get_factors(counter) <= n:
        counter += turn
        turn += 1
    return counter


input = int(input("Give me ya num : "))

print(func(input))
