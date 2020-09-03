import string
import time
time1 = time.perf_counter()
list = ['I', 'REPEAT', 'THIS', 'IS', 'ONLY', 'A', 'TEST']
word_scores = []
list.sort()

for i in list:
    word_value = 0
    for letter in i:
         word_value += string.ascii_uppercase.index(letter)+1
    word_scores.append(word_value * (list.index(i)+1))
print(sum(word_scores))

print(time.perf_counter() - time1)