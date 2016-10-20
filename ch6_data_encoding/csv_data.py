import csv
from collections import namedtuple
import re

with open('data_files/stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # process row
        print(row)
print()

# since the tuples in row are indexed with number, namedtuple can be useful to make it clearer
with open('data_files/stocks.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        # process row
        print(row)
print()

# can also read rows as a series of dictionaries
with open('data_files/stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        # process row
        print(row)
print()

# DictWriter also exists that writes headers, one row at a time, or a sequence of rows

# delimiter can be set in order to read tab delimited data (or anything else)
with open('data_files/stocks.tsv') as f:
    f_tsv = csv.reader(f, delimiter='\t')
    for row in f_tsv:
        print(row)
print()

# if headers include invalid python identifier characters (like spaces or hyphens) they may have to be scrubbed by
# substituting underscores
with open('data_files/bad_stocks.csv') as f:
    f_csv = csv.reader(f)
    headings = [re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv)]
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        # process row
        print(row)
print()

# note: csv will parse everything as a string, if other types are desired they must be explicitly converted
col_types = [str, float, str, str, float, int]
with open('data_files/stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        row = tuple(convert(value) for convert, value in zip(col_types, row))
        print(row)
print()

# can also convert selected fields of a dictionary
field_types = [('Price', float),
               ('Change', float),
               ('Volume', int)]
with open('data_files/stocks.csv') as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key])) for key, conversion in field_types)
        print(row)
