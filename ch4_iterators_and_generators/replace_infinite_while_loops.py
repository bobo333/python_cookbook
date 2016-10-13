import sys
CHUNK_SIZE = 8192


# code often looks like this:
def reader(s):
    while True:
        data = s.recv(CHUNK_SIZE)
        if data == b'':
            break
        process_data(data)


def process_data(data):
    pass


# but that can be replaced with
def reader_improved(s):
    for chunk in iter(lambda: s.recv(CHUNK_SIZE), b''):
        process_data(chunk)


# ex:
f = open('../.gitignore')
for chunk in iter(lambda: f.read(10), ''):
    print(chunk)

# iter can take a callable and a 'sentinel' value, it will call the callable over and over, yielding the value until
# the value equals the sentinel value
