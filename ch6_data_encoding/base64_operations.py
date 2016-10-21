import base64

s = b'hello'
a = base64.b64encode(s)
print(a)

d = base64.b64decode(a)
print(d)
print()

# it's only meant to be used on byte-oriented data like byte strings and byte arrays
# the output of encoding is always a byte string. May need to perform an extra decoding
# step if working with unicode data

a_bin = base64.b64encode(s)
a_uni = base64.b64encode(s).decode('ascii')
print(a_bin)    # is a binary string
print(a_uni)    # is a unicode string
