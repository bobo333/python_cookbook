import itertools


def count(n):
    while True:
        yield n
        n += 1


c = count(0)

try:
    print(c[10:20])
except TypeError:
    print("type error")
print()


# islice consumes and throws away all objects up to the point where it is told to start
for x in itertools.islice(c, 10, 20):
    print(x)
