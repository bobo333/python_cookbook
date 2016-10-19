from socket import socket, AF_INET, SOCK_STREAM
import os
import sys

# wrap a file descriptor of an open I/O channel (file, pipe, socket, etc) with a higher-level Python file object

# open a low-level file descriptor
fd = os.open('ex_files/somefile.txt', os.O_WRONLY | os.O_CREAT)

# wrap in "proper" file
f = open(fd, 'wt')
f.write('hi there\n')
f.close()

# when the high-level file object is closed or destroyed, the underlying file descriptor will also be closed
# if this is not desirable, pass closefd=False to open()
# ex:
# f = open(fd, 'wt', closefd=False)


# on UNIX-based systems this is an example using sockets
# if cross-platform support is needed, use makefile() from sockets library instead, but if Unix is ok, this method
# is much more performant
def echo_client(client_sock, addr):
    print('got connection from', addr)

    # Make text-mode file wrappers for socket reading/writing
    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1', closefd=False)
    client_out = open(client_sock.fileno(), 'wt', encoding='latin-1', closefd=False)

    # echo lines back to the client using file I/O
    for line in client_in:
        client_out.write(line)
        client_out.flush()
    client_sock.close()


def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)


# can also use this as a way to alias an already open file and use it in a different way than how it was open
# here binary data is emitted on stdout, which is usually opened in text mode
bstdout = open(sys.stdout.fileno(), 'wb', closefd=False)
bstdout.write(b'Hello World\n')
bstdout.flush()

# keep in mind a lot of these are system-specific, and need to be tested to make sure the implementation will work
