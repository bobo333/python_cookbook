from datetime import datetime

# parse strings to datetime objects
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print(repr(diff))
print()

# format datetime objects as strings
print(repr(z))
str_z = datetime.strftime(z, '%A %B %d, %Y')
print(str_z)
print()


# strptime is pretty inefficient because it has to deal with lots of system locale settings etc
# if the format is known, it may be better to write a custom parser
def parse_ymd(s):
    """For parsing date strings of the format YYYY-MM-DD"""
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))

print(repr(parse_ymd('2016-01-13')))
