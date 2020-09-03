number = 75
sol = 1
res = 0
for i in range(1, number + 1):
    sol *= i
for i in str(int(sol)):
    res += int(i)

print(res)