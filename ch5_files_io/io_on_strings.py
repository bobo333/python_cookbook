from io import BytesIO, StringIO

s = StringIO()
ret_val = s.write('Hi there!')
print(ret_val)

print('This is a test', file=s)

print(s.getvalue())

# can also treat StringIO like a file interface
s.seek(0)
print(s.read(6))
print(s.read())


# similar functionality exists for binary data
s = BytesIO()
s.write(b'binary dataz')
print(s.getvalue())

# however, they won't work with something that requires real system-level things like pipes or sockets
