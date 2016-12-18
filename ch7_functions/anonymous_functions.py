# lambdas are anonymous functions

add = lambda x, y: x + y

print(add(5, 3))

# usually used in combination with some other operation, like sort
names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
print(sorted(names, key=lambda name: name.split()[-1].lower()))
