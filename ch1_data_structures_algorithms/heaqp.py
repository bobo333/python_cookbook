#! /usr/bin/python3
import heapq
from random import randint

numbers = [randint(0, 10) for i in range(10)]
print(numbers)

heapq.heapify(numbers)
print(numbers)

numbers2 = [randint(0, 10) for i in range(10)]
print(numbers2)

five_largest = heapq.nlargest(5, numbers2)
print(five_largest)

five_smallest = heapq.nsmallest(5, numbers2)
print(five_smallest)
