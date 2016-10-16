import os
import mmap


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


desired_size = 1000000
des_filename = 'ex_files/binary_data.bin'
with open(des_filename, 'wb') as f:
    f.seek(desired_size - 1)
    f.write(b'\x00')


m = memory_map(des_filename)
len(m)
print(m[0:10])
print(m[0])

# reassign a slice
m[0:11] = b'Hello World'
m.close()

# verify the changes were made
with open(des_filename, 'rb') as f:
    print(f.read(11))
print()

# mmap object returned by mmap() can also be used as a context manager
# don't need to modify it, so ACCESS_READ is ok here, ACCESS_COPY allows for local modification without writing back to
# original file
with memory_map(des_filename, mmap.ACCESS_READ) as m:
    print(len(m))
    print(m[:11])
print(m.closed)
print()

# memory exposed by mmap() looks like a bytearray, but it can be interpreted in different ways
m = memory_map(des_filename)
# memory view of unsigned integers
v = memoryview(m).cast('I')
print(v[0], v[1], v[2])
v[0] = 7
print(m[:11])
m[0:4] = b'\x07\x01\x00\x00'
print(v[0])

# memory maps can be shared across python interpreters, but care must be taken to synchronize this

