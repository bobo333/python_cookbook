import sys

try:
    sys.stdout.write(b'Hello\n')
except TypeError:
    print('Type error, must be str, not bytes')

# can't use write directly with bytes, but can use the underlying buffer just fine
# the IO system is built of layers, the top layer is an encoding / decoding layer that handles Unicode, using the
# buffer attribute bypasses the top layer and access the underlying buffered binary-mode file
sys.stdout.buffer.write(b'Hello\n')
