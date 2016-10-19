# requires 3rd-party pyserial to be installed
import serial

# note this will not work in pycharm
# note, this will do funky things to the terminal
ser = serial.Serial('/dev/stdout',  # device name varies
                    baudrate=9600,
                    bytesize=8,
                    parity='N',
                    stopbits=1,
                    timeout=5)      # including timeout so it won't freeze the terminal waiting for something to read
                                    # however, it will still mess up that terminal

ser.write(b'G1 X50 Y50\r\n')
resp = ser.readline()
print(resp)

# communication must always be binary
# struct module can be useful if binary-coded commands or packets are needed
