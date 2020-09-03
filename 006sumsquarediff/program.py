input = int(input("Give me ya num : "))
num1 = 0
num2 = 0
counter = 1

while counter <= input:
    num1 += counter * counter
    num2 += counter
    counter += 1

num2 *= num2

print("Num1 : %s, Num2 : %s, dif is : %s" % (num1, num2, num2 - num1))
