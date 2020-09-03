import math


def doesprime(num):
    if num > 0:
        sqrt = math.floor(math.sqrt(num))
        print("Num is : %s, Sqrt is : %s" % (num, sqrt))
        counter = 3

        while counter <= sqrt:
            if num % counter == 0:
                print("Counter : %s" % (counter))
                return False
            counter += 1

    return True


num = int(input("Which num wanted to be factorized : "))
counter = 1
biggestPrimeFactor = 1
primes = [1]
while counter <= num:
    if num == 2:
        biggestPrimeFactor = num
    if num % counter == 0:
        if doesprime(counter):
            if biggestPrimeFactor < counter:
                biggestPrimeFactor = counter
            primes.append(counter)
    counter += 1

print("The primes are %s and the biggest is %s" % (primes, biggestPrimeFactor))
