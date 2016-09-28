import struct

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data))

little = int.from_bytes(data, 'little')
print(little)

big = int.from_bytes(data, 'big')
print(big)

print()

x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))
print()

# can also use struct, but it's somewhat more limited
hi, lo = struct.unpack('>QQ', data)
print((hi << 64) + lo)
print()

# 'little' vs 'big' indicates if bytes are listed from least to most significant or the other way around. Ex:
x = 0x01020304
print(x.to_bytes(4, 'big'))
print(x.to_bytes(4, 'little'))

# unpacking an integer to a byte string won't work because it won't fit
x = 523 ** 23
print(x)
print()
try:
    print(x.to_bytes(16, 'little'))
except OverflowError:
    print("overflow error")

# can use bit_length to determine how many bits are required to store the value
bit_length = x.bit_length()
nbytes, rem = divmod(bit_length, 8)
if rem:
    nbytes += 1

print(x.to_bytes(nbytes, 'little'))
