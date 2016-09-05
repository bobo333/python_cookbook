import os

# get sum of squares efficiently
# use a generator expression argument
# note the 2nd set of parentheses is not needed when a generator expression is used
numbers = [1, 2, 3, 4, 5]
square_sum = sum(x * x for x in numbers)
# same as square_sum = sum((x * x for x in numbers))
# but extra parens are not required
print(square_sum)
print()


# see if any .py files exist in a directory
files = os.listdir('.')
if any(name.endswith('.py') for name in files):
    print('Found the snake!')
print()


# output tuple as csv
s = ('ACME', 50, 123.5)
print(','.join(str(x) for x in s))
print()


# Data reduction across fields of a data structure
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name:': 'YHOO', 'shares': 20},
    {'name': 'AOL', 'shares': 12},
    {'name': 'SCOX', 'shares': 30}
]

min_shares = min(x['shares'] for x in portfolio)
print(min_shares)

# can also use the key argument for min, which will return the entire dictionary instead of just the shares value
min_shares = min(portfolio, key=lambda x: x['shares'])
print(min_shares)
