def my_fun():
    return 1, 2, 3


a, b, c = my_fun()

print(a, b, c)

# a tuple is actually being returned, and unpacked by the a, b, c syntax

my_tup = my_fun()

print(type(my_tup))
print(my_tup)
