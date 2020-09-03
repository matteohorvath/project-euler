def biggestpower(num, maxnum):
    array = []
    while num <= maxnum:
        array.append(num)
        if num == 0 or num == 1:
            num += 1
        num *= num
    print(array)
    return max(array)


def smallestmultiple(num):
    counter = 1
    value = 1
    while num >= counter:
        if value % biggestpower(counter, num) != 0:
            value *= biggestpower(counter, num)
        counter += 1
    return value


input = int(input("Give me ya num : "))
print(smallestmultiple(input))
