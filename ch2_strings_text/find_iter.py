import re

# use re.finditer instead of re.findall to get an iterator instead of a list of matches
date_pattern = re.compile('\d{4}-\d{2}-\d{2}')

text = 'Today is 2016-09-05, tomorrow is 2016-09-06'

dates = date_pattern.findall(text)
print(dates)

dates_iter = date_pattern.finditer(text)
print(dates_iter)
for d in dates_iter:
    print(d.group())
