import os
import time

print(os.path.exists('/etc/passwd'))
print(os.path.exists('/tmp/spam'))
print()

print(os.path.isfile('/etc/passwd'))
print(os.path.isdir('/etc/passwd'))
print(os.path.islink('/usr/bin/python3'))
print(os.path.realpath('/usr/bin/python3'))
print()

# can also retrieve metadata
print(os.path.getsize('/etc/passwd'))
print(os.path.getmtime('/etc/passwd'))      # modification time
print(time.ctime(os.path.getmtime('/etc/passwd')))

# warning: must be aware of permissions
try:
    print(os.path.getsize('/etc/docker/key.json'))
except PermissionError:
    print('Permission error')
