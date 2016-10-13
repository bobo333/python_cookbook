import heapq

a = [1, 4, 7, 10]
b = [2, 5, 6, 11]

# NOTE: requires that all input sequences be sorted already
for c in heapq.merge(a, b):
    print(c)
