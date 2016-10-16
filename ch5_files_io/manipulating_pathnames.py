import os

path = '/Users/steve/Data/data.csv'
dir_path = '/Users/steve/Data/'

# get the last component of the path
print(os.path.basename(path))
print(os.path.basename(dir_path))   # empty
print()

# get dir name
print(os.path.dirname(path))
print(os.path.dirname(dir_path))
print()

# join path components
print(os.path.join('tmp', 'data', os.path.basename(path)))
print()

# expand users's home directory
path = '~/Data/data.csv'
print(os.path.expanduser(path))
print()

# split the file extension
print(os.path.splitext(path))
