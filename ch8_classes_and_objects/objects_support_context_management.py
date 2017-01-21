# context management means using them in the "with" syntax
# must define __enter__ and __exit__ methods
from functools import partial
from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None

conn = LazyConnection(('www.python.org', 80))
# the connection is not opened yet

with conn as s:
    # conn.__enter__ executes, opening the connection
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    print(resp)
    # conn.__exit__ executes, closing the connection


# this currently only supports one socket in use at a time
# here is how to be able to use multiple nested at once
class LazyConnection2:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connections.pop().close()


conn2 = LazyConnection2(('www.python.org', 80))
with conn2 as s1:
    # do something
    print('independent sockets!')
    with conn2 as s2:
        # do a different thing
        print('in a nested context manager!')
