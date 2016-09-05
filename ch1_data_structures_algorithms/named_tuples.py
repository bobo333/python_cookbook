from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])

sub = Subscriber('bob@bob.com', '2016-03-26')
print(sub)
print(sub.addr)
print(sub.joined)
print()

# named tuple is still a tuple though!
print(len(sub))
print(sub[0])
print(sub[1])

addr, joined = sub
print(addr, joined)
print()

my_records = [
    ('AAPL', 700000, 50.3),
    ('IBM', 1000000, 203.5),
    ('FB', 300000, 20.5)
]


# another example!
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

print(compute_cost(my_records))

# could be rewritten as

Stock = namedtuple('Stock', ['name', 'shares', 'share_price'])


def better_compute_cost(records):
    total = 0.0
    for rec in records:
        # *rec unpacks the items in record one by one to use them as arguments
        stock = Stock(*rec)
        total += stock.shares * stock.share_price
    return total

print(better_compute_cost(my_records))
print()

# named tuples are more performant than dictionaries, but are immutable
# however, they have a _replace method to change values
a_stock = Stock('Steve Inc', 99999999, 999)
print(a_stock)

# but it returns a new named tuple it created, it does not edit in place
new_stock = a_stock._replace(share_price=9999)
print(a_stock)
print(new_stock)
print()

# replace can be used with a "template" named tuple and then update fields accordingly
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
prototype_stock = Stock('', 0, 0, None, None)


# function to convert dictionary to stock:
def dict_to_stock(the_dict):
    return prototype_stock._replace(**the_dict)

stock_a = {'name': 'a', 'shares': 55, 'price': 95.3}
stock_a = dict_to_stock(stock_a)
print(stock_a)
