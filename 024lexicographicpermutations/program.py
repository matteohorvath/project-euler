import time
from itertools import permutations

time1 = time.perf_counter()

permutations_list = []


def lexicographical_permutation(str):
    perm = sorted(''.join(chars) for chars in permutations(str))
    for x in perm:
        permutations_list.append(x)

lexicographical_permutation("0123456789")

print(permutations_list[999999])
print(time.perf_counter() - time1)
