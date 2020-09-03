nth = int(input("How many do you want : "))

sum = 2 # because the b is normally 2, and that isnt added in the while.
counter = 1
a = 1
b = 2
while counter <= nth:
    if counter % 2 == 0:
        b = a + b
        print(a)
        if b % 2 == 0:
            sum += b
    else:
        a = a + b
        print(b)
        if a % 2 == 0:
            sum += a
    counter += 1

print("The sum is %s" % sum)
