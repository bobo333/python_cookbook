

# place the desired keyword args after a * argument, or an unnamed *
def recv(maxsize, *, block):
    """receives a message. *block* is a keyword-only argument"""
    pass


try:
    recv(1024, True)    # error
except TypeError:
    print('type error')
recv(1024, block=True)  # ok


def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


print(minimum(1, 5, 2, -5, 10))
print(minimum(1, 5, 2, -5, 10, clip=0))

# forcing certain args (especially boolean flags) to be keyword only can improve code clarity
