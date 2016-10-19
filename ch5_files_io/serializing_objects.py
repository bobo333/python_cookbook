import time
import threading

import pickle


class Ball(object):
    def __init__(self, color=None):
        self.color = color

    def __repr__(self):
        return '<Ball: {}>'.format(self.color)

my_ball = Ball('green')
print(my_ball, id(my_ball))

# dump object to file
f = open('ex_files/pickle_dump', 'wb')
pickle.dump(my_ball, f)
f.close()

# dump object to string
s = pickle.dumps(my_ball)
print(s)

# recreate the object from a byte stream
f = open('ex_files/pickle_dump', 'rb')
my_new_ball = pickle.load(f)
f.close()
my_new_ball2 = pickle.loads(s)

print(my_new_ball, id(my_new_ball))
print(my_new_ball2, id(my_new_ball2))
print()

# multiple things can be pickled and unpickled from one file
with open('ex_files/multiple_pickle_dumps', 'wb') as f:
    pickle.dump([1, 2, 3], f)
    pickle.dump('hello', f)
    pickle.dump({'one': 1, 'two': 'your face'}, f)

with open('ex_files/multiple_pickle_dumps', 'rb') as f:
    print(pickle.load(f))
    print(pickle.load(f))
    print(pickle.load(f))
    try:
        print(pickle.load(f))
    except EOFError:
        print('EOFError, ran out of input as expected')

# functions, classes, and instances can be pickled, but name references will be copied only, not full packages and
# modules, it assumes they are in place correctly, so this can often require having access to the same source code

# note: only trusted data should be loaded with pickle, as arbitrary commands can be executed in this process


# __getstate__ and __setstate__ can be used to preserve state between pickling and unpickling, even for things that
# usually can not be pickled (like threads or other external dependencies on the system)
class Countdown:
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('T-minus:', self.n)
            self.n -= 1
            time.sleep(1)

    def __getstate__(self):
        return self.n

    def __setstate__(self, n):
        self.__init__(n)

# these should really be run in separate terminal windows, but this gets the idea across
c = Countdown(30)
time.sleep(5)
f = open('ex_files/cstate.p', 'wb')
pickle.dump(c, f)
f.close()

time.sleep(3)

f = open('ex_files/cstate.p', 'rb')
c_loaded = pickle.load(f)
f.close()
time.sleep(10)
