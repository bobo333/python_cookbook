from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds)
print(c.seconds / 3600)
print(c.total_seconds() / 3600)
print()

a = datetime(2012, 9, 23)
print(a + timedelta(days=10))
b = datetime(2012, 12, 21)
d = b - a
print(d.days)
now = datetime.today()
print(now)
print(now + timedelta(minutes=10))
print()

# datetime is aware of leap years
a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
print((a - b).days)
c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
print((c - d).days)
print()

# more complex things can be done with the dateutil module, datetime is often sufficient for simpler tasks
a = datetime(2012, 9, 23)
try:
    a + timedelta(months=1)
except TypeError as e:
    print("type error: {}".format(e.args[0]))

print(a + relativedelta(months=1))
print()

# time between two dates
b = datetime(2012, 12, 21)
d = b - a
print(repr(d))
d = relativedelta(b, a)
print(repr(d))
print(d.months)
print(d.days)

