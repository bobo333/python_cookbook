import urllib.request
import io
import sys


u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()
print(text)

# detach can be used ot change the encoding of an already opened text-mode file
# here the encoding of stdout is changed from the default to latin-1
print(sys.stdout.encoding)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
print(sys.stdout.encoding)
print()
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')    # change it back to default

# the IO system is built on layers, they can be seen a such:
f = open('ex_files/sample.txt', 'w')
print(f)                # text-handling layer that encodes and decodes Unicode
print(f.buffer)         # buffered IO layer that handles binary data
print(f.buffer.raw)     # raw file representing low-level file descriptor in the OS

print()

# it's not safe to mess with the different layers directly
f = io.TextIOWrapper(f.buffer, encoding='latin-1')
print(f)
try:
    f.write('hello')
except ValueError:
    # throws the error because the original value of f got destroyed and closed the underlying file in the process
    print('Value error - IO operation on closed file')
print()

f = open('ex_files/sample.txt', 'w')
print(f)
b = f.detach()
print(b)
try:
    f.write('hello')
except ValueError:
    print('value error - underlying buffer has been detached')

# but once detached a new layer can be added on top of it, in this case with a new encoding
f = io.TextIOWrapper(b, encoding='latin-1')
print(f)
print()

# this can also change line handling, error policy, etc
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='ascii', errors='xmlcharrefreplace')
print('Jalape\u00f1o')
