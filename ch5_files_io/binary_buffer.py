import os.path


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)     # reads contents into existing buffer, instead of allocating a new one like read()
    return buf


buf = read_into_buffer('ex_files/liverpool.png')
print(buf)
print()

buf_short = buf[0:10]
print(buf_short)

buf_short[0:5] = b'Hallo'
print(buf_short)
print()


# can also use memoryview to see memory information about the buffer
m1 = memoryview(buf_short)
m2 = m1[-5:]
print(m2)
m2[:] = b'WORLD'

print(buf_short)

# recv_into, pack_into, etc are also available to manipulate buffers
