from functools import partial


def apply_async(func, args, *, callback):
    # compute the result
    result = func(*args)

    # invoke the callback with the result
    callback(result)


def print_result(result):
    print('Got: ', result)


def add(x, y):
    return x + y


apply_async(add, (2, 3), callback=print_result)
apply_async(add, ('hello', 'world'), callback=print_result)
print()


# to hold state for a callback, can use a bound method
class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))


r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)
apply_async(add, ('hello', 'world'), callback=r.handler)
print()


# can also use a closure
def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence   # nonlocal declaration required here because the value is modified in the inner fxn
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

    return handler


handler = make_handler()
apply_async(add, (2, 3), callback=handler)
apply_async(add, ('hello', 'world'), callback=handler)
print()


# can also use a coroutine
def make_handler_coro():
    sequence = 0

    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


# for a coroutine, use its send method as a callback:
handler = make_handler_coro()
next(handler)   # advance the yield
apply_async(add, (2, 3), callback=handler.send)
apply_async(add, ('hello', 'world'), callback=handler.send)
print()


# lastly, can use an extra argument & partial function
class SequenceNo:
    def __init__(self):
        self.sequence = 0


def handler(result, seq):
    seq.sequence += 1
    print('[{}] Got: {}'.format(seq.sequence, result))


seq = SequenceNo()
apply_async(add, (2, 3), callback=partial(handler, seq=seq))
apply_async(add, ('hello', 'world'), callback=partial(handler, seq=seq))

