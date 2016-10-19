from tempfile import NamedTemporaryFile, TemporaryFile, TemporaryDirectory
import tempfile
import os

with TemporaryFile('w+t') as f:     # can also include encoding params and errors, just like normal open()
    # Read/write to the file
    f.write('Hello peoples\n')
    f.write('Testing\n')

    # seek back to beginning and read the data
    f.seek(0)
    data = f.read()

# temporary file is destroyed
print(data)

# can also provide a name (normal TemporaryFile has no name and no directory entry)
with NamedTemporaryFile('w+t') as f:
    print('file name is: ', f.name)
# automatically destroyed
# supplying delete=False prevents it from being automatically destroyed when closed

with TemporaryDirectory() as dirname:
    print('dirname is: ', dirname)

# can do similar things lower level, but provides less cleanup and niceties
# only returns a raw OS file descriptor, must then be turned into a proper file
# neither does any cleanup
fileno, filename = tempfile.mkstemp()
dir_name = tempfile.mkdtemp()

print(fileno, filename)
print(dir_name)

# can get location of temp directory that is being used
temp_dir_name = tempfile.gettempdir()
print(temp_dir_name)
tmp_contents = os.listdir(temp_dir_name)
print(tmp_contents)
print(os.path.basename(filename) in tmp_contents)   # these will both be True since no cleanup was done
print(os.path.basename(dir_name) in tmp_contents)

# it is also possible to supply prefix, suffix, and directory for temp files
with NamedTemporaryFile(prefix='feelsbadman', suffix='.jpg', dir='ex_files') as f:
    print(f.name)
