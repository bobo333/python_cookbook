numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# can use a list comprehension
odds = [x for x in numbers if x % 2]
print(odds)

# can use a generator expression
odds = (x for x in numbers if x % 2)

for odd in odds:
    print(odd)

# can use filter built-in function
def is_odd(x):
    return x % 2

# filter returns a generator
odds = filter(is_odd, numbers)

print(list(odds))
