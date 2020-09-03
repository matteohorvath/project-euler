max = int(input("Give me the max num"))
sum = 0
counter = 0

while counter<max:

    if counter%3==0 or counter %5==0:
        sum += counter

    counter += 1
print("The sum is %s" % sum)
