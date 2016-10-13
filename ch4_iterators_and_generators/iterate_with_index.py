my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)
print()

# can also pass a start value
for idx, val in enumerate(my_list, 5):
    print(idx, val)
print()

# can enumerate any iterable
with open('../.gitignore') as f:
    for lineno, line in enumerate(f, 1):
        line = line.replace('\n', '')
        print(lineno, line)

# enumerate() returns an enumerate object, which is an iterator
print()

# be careful when using enumerate with data that is also being unpacked
data = [(1, 2), (3, 4), (5, 6), (7, 8)]

for n, (x, y) in enumerate(data):
    print(n, x, y)
print()

# not
try:
    for n, x, y in enumerate(data):
        print(n, x, y)
except ValueError:
    print('ValueError!')
