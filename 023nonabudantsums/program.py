import math

import time
time1 = time.perf_counter()
n = 28123
def divisors_sum(n):
    sum = 0
    numbers = []
    for i in range(1,math.floor(n / 2)+1):
        if n % i == 0:
            numbers.append(i)
            sum += i

    return sum

list_abundant = []
list_notDoubleAbundant = []
for i in range(1,n+1):
    if divisors_sum(i) > i:
        list_abundant.append(i)

for i in range(1, n+1):
    print(f"now {i}")
    print(sum(list_notDoubleAbundant))
    double_aboundant = True
    for abundant in list_abundant:
        if abundant > i:
            break
        if (i-abundant) in list_abundant:
            double_aboundant = False
    if double_aboundant:
        list_notDoubleAbundant.append(i)
print(sum(list_notDoubleAbundant))

print(time.perf_counter() - time1)