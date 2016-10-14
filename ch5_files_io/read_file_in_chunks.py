from functools import partial

RECORD_SIZE = 32

with open('../.gitignore', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)

# note: the last chunk may not have a full 32 bytes if the file size is not an exact multiple of the RECORD_SIZE

# this uses iter to repeatedly call the provided function over and over until the sentinel value is reached (b'')
# partial is used to create a function that repeatedly calls read() on the file object, passing RECORD_SIZE each time
# this approach will work in non-binary mode as well, but when reading a file as text, it's more common to read it
# line by line (the default iterator for a file object in python)
