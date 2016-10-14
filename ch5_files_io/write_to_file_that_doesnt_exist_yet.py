import os

with open('ex_files/just_created.txt', 'w') as f:
    f.write('hi there dudes\n')

# the 'x' open mode only works in Python3!
try:
    with open('ex_files/just_created.txt', 'x') as f:
        f.write('hi again!')
except FileExistsError:
    print('File exists!')

# remove the file so this script works again next time ;)
os.remove('ex_files/just_created.txt')
