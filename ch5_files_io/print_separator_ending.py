print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, end='!!!!!11111two\n')
print('ACME', 50, 91.5, sep=';', end='ZEE END')     # will not print newline at the end!

print()
print()

things = ['ACME', 50, 91.5]
print(*things)
