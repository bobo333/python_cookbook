# variables are bound at runtime, not definition time

x = 10
a = lambda y: x + y

x = 20
b = lambda y: x + y

print(a(10))    # prints 30, not 20!
print(b(10))    # prints 30
print()

# to get the intended behavior by saving the value of x at definition time, do this:
x = 10
a = lambda y, x=x: x +  y

x = 20
b = lambda y, x=x: x + y
print(a(10))    # prints 20
print(b(10))    # prints 30
print()

# comes up a lot when using for loops to create lambda functions. ex:
funcs = [lambda x: x + n for n in range(5)]
for f in funcs:
    print(f(0))     # prints all 4's

print()
funcs2 = [lambda x, n=n: x + n for n in range(5)]
for f in funcs2:
    print(f(0))     # prints 0, 1, 2, 3, 4
