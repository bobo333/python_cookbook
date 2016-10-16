import os
import sys

filename = '[bad, non-standard encoded name]'


def bad_filename(filename):
    return repr(filename)[1:-1]


try:
    print(filename)
except UnicodeDecodeError:
    print(bad_filename(filename))


# create a file whose name is not valid unicode
with open('ex_files/bäd.txt'.encode('latin-1'), 'w') as f:
    f.write('hi')
print()

filenames = os.listdir('ex_files')
try:
    for fn in filenames:
        print(fn)
except UnicodeEncodeError:
    print('Error message about surrogates not allowed')
    print('UnicodeEncodeError')
    print(bad_filename(fn))
print()

# can also re-encode the name somehow to get it to print correctly
for fn in filenames:
    try:
        print(fn)
    except UnicodeEncodeError:
        temp = fn.encode(sys.getfilesystemencoding(), errors='surrogateescape')
        print(temp.decode('latin-1'))
