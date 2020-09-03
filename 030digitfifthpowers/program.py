import time
import math

time1 = time.perf_counter()
power = 2
list = []
for i in range(2, int(math.pow(9,power))*power):
    sol = 0
    for letter in str(i):
        sol += int(math.pow(int(letter), power))
    if sol==i:
        list.append(i)

print(list)
print(sum(list))
print(time.perf_counter() - time1)