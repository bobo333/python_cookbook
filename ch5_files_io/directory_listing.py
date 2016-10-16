import glob
from fnmatch import fnmatch
import os

home = os.path.expanduser('~/')
names = os.listdir(home)
print(names)
print()

# get all regular files
file_names = [name for name in os.listdir(home) if os.path.isfile(os.path.join(home, name))]
print(file_names)

# get all dir names
dir_names = [name for name in os.listdir(home) if os.path.isdir(os.path.join(home, name))]
print(dir_names)
print()

# filter with startswith() or endswith()
txt_files = [name for name in os.listdir('ex_files/') if name.endswith('.txt')]
print(txt_files)
print()

# glob or fnmatch can also be used
txt_files_glob = glob.glob('ex_files/*.txt')
print(txt_files_glob)
print()

txt_files_fnmatch = [name for name in os.listdir('ex_files') if fnmatch(name, '*.txt')]
print(txt_files_fnmatch)
print()

# os.stat also gives information about files
file_metadata = [(name, os.stat(name)) for name in txt_files_glob]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)
