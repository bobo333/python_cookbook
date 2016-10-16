import os
import sys

print(sys.getfilesystemencoding())


# write a file using a unicode filename
with open('ex_files/jalape\xf1o.txt', 'w') as f:
    f.write('Spicy!')

# directory listing (decoded filenames)
print(os.listdir('ex_files'))

# directory listing raw filenames
print(os.listdir(b'ex_files'))

# open file with raw filename
with open(b'ex_files/jalape\xc3\xb1o.txt') as f:
    print(f.read())
