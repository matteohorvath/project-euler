import math
def func(n):
    sol = 0
    for elem in str(int(math.pow(2,n))):
        sol += int(elem)
    return sol

n = int(input("Give me ya num : "))

print(func(n))