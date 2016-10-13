from itertools import combinations, combinations_with_replacement, permutations

my_list = ['a', 'b', 'c']

for p in permutations(my_list):
    print(p)
print()

# can get smaller size as well
for p in permutations(my_list, 2):
    print(p)
print()

# combinations will give unique groups where order doesn't matter (combinations, not permutations)
for c in combinations(my_list, 3):      # note: size of the desired combinations is required
    print(c)
print()

for c in combinations(my_list, 2):
    print(c)
print()

# by default duplicate elements are filtered and replaced, but that can be disabled
for c in combinations_with_replacement(my_list, 3):
    print(c)
print()

for c in combinations_with_replacement(my_list, 4):
    print(c)
