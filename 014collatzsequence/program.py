def get_collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            steps += 1
        elif n % 2 == 1:
            n = n * 3 + 1
            steps += 1
    return steps + 1  # +1 cause of the last 1 is countered too


def func(n):
    biggest = [0,0]
    x = 1
    while x < n:
        print(x)
        if get_collatz_steps(x) > biggest[0]:
            biggest[0] = get_collatz_steps(x)
            biggest[1] = x
        x += 1
    return biggest


n = int(input("Give me ya num : "))

print(func(n))
