condition = 1000
def divide(a, b):

  assert b > 0
  integer = a // b
  remainder = a % b
  seen = {remainder: 0}  # Holds position where each remainder was first seen.
  digits = []
  while(True):  # Loop executed at most b times (as remainders must be distinct)
    remainder *= 10
    digits.append(remainder // b)
    remainder = remainder % b
    if remainder in seen:  # Digits have begun to recur.
      where = seen[remainder]
      return (integer, digits[:where], digits[where:])
    else:
      seen[remainder] = len(digits)

biggest = -1
for b in range(1,condition):
    (i, f, r) = divide(1, b)
    if len(r) > biggest:
        biggest = len(r) +1
    print("%d/%d = %d.%s(%s)" % (1, b, i, ''.join(map(str, f)), ''.join(map(str, r))))

print(biggest)