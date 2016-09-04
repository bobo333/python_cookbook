str_to_slice = "1234StevenCipriano1989"

LEADING_NUMBERS = slice(4)
FIRST_NAME = slice(4, 10)
LAST_NAME = slice(10, 18)
BIRTH_YEAR = slice(18, 22)

nums = str_to_slice[LEADING_NUMBERS]
print(nums)
print()

first_name = str_to_slice[FIRST_NAME]
print(first_name)
print()

last_name = str_to_slice[LAST_NAME]
print(last_name)
print()

birth_year = str_to_slice[BIRTH_YEAR]
print(birth_year)

# indices will give the proper range for a slice to not violate the bounds of a string
print(LAST_NAME.indices(len("hi")))
