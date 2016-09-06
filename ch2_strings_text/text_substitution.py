from calendar import month_abbr
import re

text = 'today is 2016-09-05'
# want to rewrite as 'today is 05/09/2016

# the \3, \1, and \2 refer to the capture group numbers
# the r in front of the second pattern mean it's a literally-interpreted string (the backslashes don't have to be
# escaped)
replaced = re.sub('(\d{4})-(\d{2})-(\d{2})', r'\3/\2/\1', text)
print(replaced)


# can also pass a callback to do the substitution
# note: group numbers are 1-indexed!
def change_date(match):
    month_name = month_abbr[int(match.group(2))]
    return '{} {} {}'.format(match.group(3), month_name, match.group(1))


date_pattern = re.compile('(\d{4})-(\d{2})-(\d{2})')
print(date_pattern.sub(change_date, text))


# to see how many substitutions were made, use the subn method
new_text, subs = date_pattern.subn(r'\3/\2/\1', text)
print(new_text)
print(subs)
