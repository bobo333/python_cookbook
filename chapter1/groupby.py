from itertools import groupby
from operator import itemgetter


rows = [
    {'address': '5412 N CLARK', 'date': '7/01/2012'},
    {'address': '5148 N CLARK', 'date': '7/04/2012'},
    {'address': '5800 E 58TH', 'date': '7/02/2012'},
    {'address': '2122 N CLARK', 'date': '7/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '7/02/2012'},
    {'address': '1060 W ADDISON', 'date': '7/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '7/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '7/04/2012'}
]

# sort by desired field to group (date in this case)
rows.sort(key=itemgetter('date'))

# iterate in groups
# groupby only works on sequential items that are the same, so it's important to sort first
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('     ', i)
