import time

time1 = time.perf_counter()
num_range = 1001
diagonals_sum = 1
current_num = 1
for i in range(1, int((num_range-1)/2)+1):
    for loop in range(4):
        current_num += 2*i
        diagonals_sum += current_num


print(diagonals_sum)
print(time.perf_counter() - time1)