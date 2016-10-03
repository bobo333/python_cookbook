from itertools import dropwhile, islice

lines = [
    "# comment1",
    "# comment2",
    "# comment3",
    "data 1",
    "data 2",
    "data 3"
]

for line in dropwhile(lambda l: l.startswith("#"), lines):
    print(line)
print()

# if the number of items to skip is known, can use islice
for x in islice(lines, 3, None):    # passing None indicates everything after the first 3 items is desired, like [3:]
    print(x)
