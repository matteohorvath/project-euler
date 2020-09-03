import math
import time

time1 = time.perf_counter()
def is_prime(n):
    if n <= 2:
        return False
    for i in range(2, (int(math.sqrt(n) + 1))):
        if n % i == 0:
            return False
    return True

def value_of_formula(a,b):
    n = 0
    while True:
        sol = n + a
        sol *= n
        sol += b
        if not is_prime(sol):
            break
        n += 1
    return n+1

num_range = 1000
biggest_n = 0
big_a = 0
big_b = 0
for a in range((num_range*2)-1):
    for b in range((num_range*2)+1):
        if biggest_n < value_of_formula(a-num_range,b-num_range):
            biggest_n = value_of_formula(a-num_range,b-num_range)
            big_a = a-num_range
            big_b = b-num_range
print(big_a*big_b)
print(big_a, big_b)

print(time.perf_counter() - time1)