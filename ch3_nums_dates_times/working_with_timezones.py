# pytz is a very useful package for dealing with timezones on python, it provides the Olson time zone database, which is
# the gold standard for timezones

from datetime import datetime, timedelta
from pytz import country_timezones, timezone, utc

d = datetime(2012, 12, 21, 9, 30, 0)
print(d)

# localize the date for Chicago
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

# convert to Bangalore, India time
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)
print()

# if doing arithmetic with times, be cognizant of daylight savings time and other minutiae
# in the US in 2013, daylight savings time started on March 10 at 2am local time, at which point it skipped ahead an
# hour
d = datetime(2013, 3, 10, 1, 45)
loc_d = central.localize(d)
print(loc_d)
later = loc_d + timedelta(minutes=30)
print(later)    # WRONG ANSWER! does not account for the hour skipping ahead

# use the normalize method of the time zone:
later = central.normalize(loc_d + timedelta(minutes=30))
print(later)    # correct!
print()

# a standard approach to avoid confusion is to convert everything to UTC time and use that for storage and manipulation
print(loc_d)
utc_d = loc_d.astimezone(utc)
print(utc_d)
print()

# now normal datetime arithmetic can be used, and the result can be converted back to a local timezone afterwards. ex:
later_utc = utc_d + timedelta(minutes=30)
print(later_utc.astimezone(central))    # will account for daylight savings time
print()

# to find appropriate timezones, pytz.country_timezones can be used with the ISO 3166 country code as a key:
print(country_timezones['IN'])
