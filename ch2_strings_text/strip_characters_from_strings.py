import re

# strip can be used to remove whitespace

a_string = "   hi there   \n"

print(a_string)
print(a_string.strip())


# it can also strip other characters

b_string = "-----====lol -----=="

print(b_string)
print(b_string.strip('-='))


# lstrip and rstrip exist as well

c_string = "   hi    "

print(c_string)
print(c_string.lstrip())
print(c_string.rstrip())


# however, it doesn't apply to the middle of the string at all
d_string = "    hi       there    "
print(d_string.strip())

# to remove whitespace in the middle, use replace or a regex
print(d_string.replace(' ', ''))
print(re.sub('\s+', ' ', d_string))
