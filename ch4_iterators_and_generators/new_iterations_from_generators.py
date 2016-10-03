# use a generator to define a custom iterator


def float_range(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

for n in float_range(0, 4, .5):
    print(n)

print(list(float_range(0, 1, .125)))
print()

x = iter(float_range(0, 1, .3))
while True:
    thing = next(x, None)
    if thing is None:
        break
    print(thing)
