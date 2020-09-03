def aUnderB(a,b):
    sol = 1
    for i in range(0,a):
        sol *= (b-i)
        sol /= (a-i)
    return sol

def func(n):
    return aUnderB(n,2*n)

n = int(input("Give me ya num : "))

print(func(n))