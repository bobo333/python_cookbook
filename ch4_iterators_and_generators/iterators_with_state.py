from collections import deque


class LineHistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


my_lines = ["line 1",
            "line 2",
            "line 3 python",
            "line 4",
            "line 5",
            "line 6",
            "line 7 python",
            "line 8"]

lines = LineHistory(my_lines)

for line in lines:
    if 'python' in line:
        for lineno, hline in lines.history:
            print('{}:{}'.format(lineno, hline))
print()

# next doesn't work though, must call iter() first
lines = LineHistory(lines)
try:
    print(next(lines))
except TypeError:
    print("type error")

my_iter = iter(lines)
print(next(my_iter))
print(next(my_iter))
