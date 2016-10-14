import array

with open('../.gitignore', 'rb') as f:
    data = f.read()

# will print byte values
for c in data:
    print(c)

# will print the "binary string"
print(data)

try:
    with open('ex_files/write_binary_to_me.bin', 'wb') as f:
        f.write('Hi there!')    # look, pycharm is even complaining!
except TypeError:
    print('Type Error')

with open('ex_files/write_binary_to_me.bin', 'wb') as f:
    f.write(b'Hi there!')   # must supply a binary string, normal string will fail

with open('ex_files/write_binary_to_me.bin') as f:
    print(f.read())
print()

# be sure to decode binary data
with open('ex_files/write_binary_to_me.bin', 'rb') as f:
    x = f.read(16)
print(x)
print(x.decode('utf-8'))

# and encode when writing to binary
with open('ex_files/write_binary_to_me2.bin', 'wb') as f:
    f.write('Hi there!'.encode('utf-8'))
print()

# arrays and C structures can be used for writing without intermediate conversion to bytes, because it exposes a buffer
# that can work with it
nums = array.array('i', [1, 2, 3, 4])
with open('ex_files/write_binary_array_to_me.bin', 'wb') as f:
    f.write(nums)

# can also read binary data into these objects that support buffers (like arrays)
a = array.array('i', [0, 0, 0, 0, 0, 0])
with open('ex_files/write_binary_array_to_me.bin', 'rb') as f:
    f.readinto(a)

print(a)

# however, be careful doing this, as certain things may be platform specific like word size and byte ordering
# (big-endian vs small-endian)
