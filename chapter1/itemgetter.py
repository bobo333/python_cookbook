from operator import itemgetter

# itemgetter is a bit more performant than using a lambda function for the key, it also accepts multiple keys to sort on

my_dicts = [
    {
        'fname': 'Brian',
        'lname': 'Jones',
        'uid': 1003
    },
    {
        'fname': 'David',
        'lname': 'Beazley',
        'uid': 1002
    },
    {
        'fname': 'John',
        'lname': 'Cleese',
        'uid': 1001
    },
    {
        'fname': 'Big',
        'lname': 'Jones',
        'uid': 1004
    }
]

sorted_by_fname = sorted(my_dicts, key=itemgetter('fname'))
sorted_by_uid = sorted(my_dicts, key=itemgetter('uid'))

print(sorted_by_fname)
print(sorted_by_uid)

sorted_by_lnfn = sorted(my_dicts, key=itemgetter('lname', 'fname'))
print(sorted_by_lnfn)

min_id = min(my_dicts, key=itemgetter('uid'))
max_id = max(my_dicts, key=itemgetter('uid'))
print(min_id)
print(max_id)
