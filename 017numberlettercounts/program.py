import inflect

p = inflect.engine()

def number_in_words_count(n):
    sol = 0
    for char in p.number_to_words(n):
        if not char.isspace() and char != "-":
            sol += 1
    return sol

def func(n):
    sol = 0
    for i in range(1,n+1):
        #print(p.number_to_words(i))
        sol += number_in_words_count(i)

    return sol


n = int(input("Give me ya num : "))

print(func(n))