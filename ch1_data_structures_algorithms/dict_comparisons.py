a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 1,
    'y': 2,
    'z': 0
}

# keys() and items() support set operations (but values() does not because they're not guaranteed to be unique)

print("keys in common:")
print(a.keys() & b.keys())

print("keys in a but not in b:")
print(a.keys() - b.keys())

print("items in common:")
print(a.items() & b.items())


# remove some keys to make a new dictionary
c = {key: a[key] for key in a.keys() - {'x'}}
print("new dict:")
print(c)
