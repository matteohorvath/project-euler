import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


array = []
sum = 0
nth = int(input("Give me ya num : "))
if nth <= 2:
    exit("Sorry not allowed data")
counter = 2
while counter != nth:
    if is_prime(counter):
        array.append(counter)
    counter += 1
for x in array:
    sum += x

print("The sum is %s" % sum)
