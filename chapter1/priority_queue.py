#! /usr/bin/python3
import heapq


class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # the index is used for tie-breakers of equal priority. It maintains the order in which items were inserted.
        # It is particularly useful when unhashable (objects or dictionaries) items are inserted.
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('soda'), 3)
q.push(Item('beer'), 5)
q.push(Item('water'), 1)

print(q.pop())
print(q.pop())
print(q.pop())
