import base64
import binascii

# for simple encoding and decoding of hex digits, use binascii
s = b'hello'
hexed = binascii.b2a_hex(s)
print(hexed)

# decode back
print(binascii.a2b_hex(hexed))
print()

# similar functionality exists in the base64 module
hexed = base64.b16encode(s)
print(hexed)
print(hexed.decode('ascii'))

# can accept either bytes or unicode strings, but the strings must contain only
# ASCII encoded hexadecimal digits
