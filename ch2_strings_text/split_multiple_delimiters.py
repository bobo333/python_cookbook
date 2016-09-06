import re

the_string = "hi there; today, is,a     day"

pieces = re.split(r'[;,\s]\s*', the_string)
print(pieces)


# to capture the delimiters
pieces_and_delims = re.split(r'(;|,|\s)\s*', the_string)
print(pieces_and_delims)
reformed = ''.join(pieces_and_delims)
print(reformed)     # note the extra spaces have not been retained, as they were not in the capture group
