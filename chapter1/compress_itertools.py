from itertools import compress

# compress takes a list of items and a corresponding list of booleans and returns the items in the first list whose
# corresponding boolean is True

people = ['Steve', 'James', 'Donald Trump', 'Bernie Sanders', 'Kobe']
is_cool = [True, True, False, True, False]

cool_people = compress(people, is_cool)

# compress returns an iterator
print(list(cool_people))
