import bz2
import gzip

with gzip.open('ex_files/ascii.gz') as f:
    text = f.read()
print(text)

try:
    with open('ex_files/ascii.gz') as f:
        print(f.read())
except UnicodeDecodeError:
    print('Unicode Decode Error!')
print()

# works with bzip2 files as well
with bz2.open('ex_files/ascii.bz2') as f:
    text = f.read()
print(text)

try:
    with open('ex_files/ascii.bz2') as f:
        print(f.read())
except UnicodeDecodeError:
    print('Unicode Decode Error!')

# writing works the same way, must specify 't' mode though, otherwise the default is binary data
with gzip.open('ex_files/write_gzip_to_me.gz', 'wt') as f:
    f.write('hahaha\n')

try:
    with open('ex_files/write_gzip_to_me.gz') as f:
        print(f.read())
except UnicodeDecodeError:
    print('Unicode Decode Error!')
print()

# when writing files, the compresslevel can be passed as a parameter, the default is 9, the max, for max compression
# lower values are more performant, but create less compression

# the also work on top of already open files, so it can work with sockets, pipes, and in-memory files
f = open('ex_files/ascii.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()
f.close()

print(text)
