import time
import math

time1 = time.perf_counter()

def remove_duplicates(x):
  return list( dict.fromkeys(x) )

num_range = 100
old_list = []
for a in range(2,num_range+1):
    for b in range(2, num_range+1):
        old_list.append(int(math.pow(a,b)))

list = remove_duplicates(old_list)
print(len(list))
print(time.perf_counter() - time1)