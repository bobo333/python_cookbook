import os
import re

data = b'Hello World!'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))
print()

data = bytearray(b'Hello World')
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))
print()

data = b'FOO:BAR,SPAM'
try:
    print(re.split('[:,]', data))
except TypeError:
    print('type error')

print(re.split(b'[:,]', data))
print()

# some differences:
a = 'Hello World'   # text string
print(a[0])
print(a[1])

b = b'Hello World'  # byte string
print(b[0])
print(b[1])
print(chr(b[0]))
print(chr(b[1]))
print()

s = b'Hello World'
print(s)
print(s.decode('ascii'))    # will remove the 'b' when printing
print()

# no string formatting for byte strings
try:
    print(b'%10s %10d %10.2f' % (b'ACME', 100, 490.1))
except TypeError:
    print('type error')

try:
    print(b'{} {} {}'.format(b'ACME', 100, 490.1))
except AttributeError:
    print('type error')

print('{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii'))
print()

# Write a utf-8 file name
with open('jalape\xf10.txt', 'w') as f:
    f.write('spicy')

print(os.listdir('.'))      # names are decoded since this is a normal string
print(os.listdir(b'.'))     # names are left as bytes
