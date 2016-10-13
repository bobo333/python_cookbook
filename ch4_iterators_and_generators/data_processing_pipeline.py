# chaining generators together can create an iterative pipeline
from itertools import chain
import re
import os


def gen_finder():
    """
    Find all filenames in a directory tree
    """
    for path, dirlist, filelist in os.walk('./'):
        for filename in filelist:
            yield os.path.join(path, filename)


def gen_opener(filenames):
    """
    Open sequence of filenames one at a time producing a file object.
    """
    for filename in filenames:
        if re.search('iterat', filename):
            f = open(filename)
            yield f
            f.close()


def gen_concatenate(iterators):
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    """
    Look for a regex pattern in a sequence of lines
    """
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


filenames = gen_finder()
files = gen_opener(filenames)
# can also use chain.from_iterable instead of gen_concatenate
lines = gen_concatenate(files)
iter_lines = gen_grep('iter', lines)

for colon_line in iter_lines:
    print(colon_line)
print('---------------------------')

filenames = gen_finder()
files = gen_opener(filenames)
other_lines = chain.from_iterable(files)
iter_lines = gen_grep('iter', other_lines)
for colon_line in iter_lines:
    print(colon_line)
