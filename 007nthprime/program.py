import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


array = []
nth = int(input("Give me ya num : "))
counter = 2
while len(array) != nth:
    if is_prime(counter):
        print(counter)
        array.append(counter)
    counter += 1
print(array)
print(array[-1])
