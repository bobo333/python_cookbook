# functools.partial allows for assigning a fixed value to one or more params of a function
from functools import partial
import logging
import math
from multiprocessing import Pool
from socketserver import StreamRequestHandler, TCPServer


def spam(a, b, c, d):
    print(a, b, c, d)

s1 = partial(spam, 1)
s1(2, 3, 4)
s1(4, 5, 6)
print()

s2 = partial(spam, d=42)
s2(1, 2, 3)
print()

s3 = partial(spam, 1, 2, d=55)
s3(3)
print()

# this is useful for making seemingly incompatible code work together
# ex:

points = [(1, 2), (3, 4), (5, 6), (7, 8)]


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)

# want to sort points based on their distance from some other point, but sort's key only accepts one value
pt = (4, 3)
points.sort(key=partial(distance, pt))
print(points)
print()


# good with tweaking callbacks and such to other libraries
# ex:
def output_result(result, log=None):
    if log is not None:
        log.debug('Got: %r', result)


# sample fxn
def add(x, y):
    return x + y


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('test')

p = Pool()
p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
p.close()
p.join()
print()


# socket server example
class EchoHandler(StreamRequestHandler):
    # ack is added keyword-only argument. *args, **kwargs are any normal params supplied (which are passed on)
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)

    def handle(self):
        for line in self.rfile:
            self.wfile.write(self.ack + line)


# can't plug into the TCPServer class now though, cause of the altered __init__, so use partial
serv = TCPServer(('', 15000), partial(EchoHandler, ack=b'RECEIVED:'))
serv.serve_forever()

# could also have used lambda, but it's less comprehensible:
# serv2 = TCPServer(('', 15000), lambda *args, **kwargs: EchoHandler(*args, ack=b'RECEIVED:', **kwargs))
