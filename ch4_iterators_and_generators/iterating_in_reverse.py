a = [1, 2, 3, 4]

for x in reversed(a):
    print(x)
print()

# can customize this, implementing __reversed__ is much more efficient than converting the iterator to a list and then
# going backwards


class Countdown:
    def __init__(self, start):
        self.start = start

    # forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

my_countdown = Countdown(5)
for i in my_countdown:
    print(i)

print('now reversed')

for i in reversed(my_countdown):
    print(i)
