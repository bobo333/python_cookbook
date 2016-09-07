import re

text = "hello steve Steve STEVE"

# re.IGNORECASE gives a case-insensitive regular expression match
print(re.sub('steve', 'AWESOME', text, flags=re.IGNORECASE))
