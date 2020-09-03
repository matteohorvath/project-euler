import math
import time

time1 = time.perf_counter()
list = []
n = 1000
for i in range(1,n+1):
    list.append(i)
list_sec = []

def divisors_sum(n):
    sum = 0
    numbers = []
    for i in range(1,math.floor(n / 2)+1):
        if n % i == 0:
            numbers.append(i)
            sum += i

    return sum

for i in list:
    # print(f"{i}, {divisors_sum(i)}, {divisors_sum(divisors_sum(i))}")
    if divisors_sum(divisors_sum(i)) == i:
        if i != divisors_sum(i):
            list_sec.append(i)
            list_sec.append(divisors_sum(i))
            list.remove(divisors_sum(i))
print(sum(list_sec))
print(time.perf_counter() - time1)