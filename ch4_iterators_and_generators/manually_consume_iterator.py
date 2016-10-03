# without using a for loop, use "next" and catch the StopIteration exeption

x = iter([1, 2, 3])

try:
    while True:
        thing = next(x)
        print(thing)
except StopIteration:
    pass
    print()

# tell next to return a final value, instead of throwing an exception
x = iter([1, 2, 3])

while True:
    thing = next(x, None)
    if thing is None:
        break
    print(thing)
