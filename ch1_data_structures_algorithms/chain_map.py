from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

chain_map = ChainMap(a, b)
print(chain_map['x'])   # prints 1 from a
print(chain_map['z'])   # prints 3 from a, as it checks a first since it's first in the ChainMap constructor params
print(chain_map['y'])   # prints 2 from b, since it's not in a
print()


# chain maps support most of the standard dictionary operations, but don't make a new dictionary, instead it keeps a
# list of which dictionaries to check and checks them sequentially

print(len(chain_map))
print(list(chain_map.keys()))
print(list(chain_map.values()))
print()


# operations that mutate the mappings always affect the first mapping listed
chain_map['w'] = 5
chain_map['z'] = 99
del chain_map['x']
print(a)
print(b)

try:
    del chain_map['y']
except KeyError:
    print("Key not found")
print()

# ChainMap is particularly useful for working with scoped values, like variables in a programming language
# (locals, global, etc)
values = ChainMap()
values['x'] = 1
# add a new mapping
values = values.new_child()
values['x'] = 2
# add a new mapping
values = values.new_child()
values['x'] = 3
print(values)
values['x'] = 909
print(values)
# discard the last mapping
values = values.parents
print(values)
print(values['x'])
# discard last mapping
values = values.parents
print(values)
print()


# an alternative could be merging dictionaries, but it has some limitations
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

merged = dict(b)
merged.update(a)

print('x:', merged['x'])
print('y:', merged['y'])
print('z:', merged['z'])

# it requires a new dictionary, and also if any of the original dictionaries get altered, it wont make it into the
# merged result, whereas it would with a ChainMap
a['x'] = 13
print(merged['x'])  # it's still 1

# vs
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = ChainMap(a, b)

a['x'] = 42
print(merged['x'])  # will print 42
