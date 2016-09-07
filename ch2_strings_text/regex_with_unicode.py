import re

num = re.compile('\d+')     # \d matches number digits
print(num.match('123'))

# Arabic digits
print(num.match('\u0661\u0662\u0663'))
print()

# unicode characters can be used directly in regexes
arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

# however, you can get into trouble with combinations of flags and normalizations
pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
print(pat.match(s))             # matches
print(pat.match(s.upper()))     # doesn't match
print(s.upper())                # case folds

# if you really have to mix unicode and regex, installing the 3rd party library "regex" may be useful
