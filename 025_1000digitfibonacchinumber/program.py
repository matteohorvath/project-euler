import time

time1 = time.perf_counter()

list = [1, 1]
loop = True
condition = 5


def test_condition(n):
    print(n)
    return True


def next_fibo():
    size = len(list)
    list.append(list[size - 1] + list[size - 2])
    test_condition(list[size])
    if len(str(list[size])) < condition:
        next_fibo()


next_fibo()
print(len(list))
print(time.perf_counter() - time1)
