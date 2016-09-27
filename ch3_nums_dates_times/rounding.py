print(round(1.234, 1))
print(round(1.234, 2))
print(round(-1.278, 2))
print()

# rounding numbers halfway between rounds to the nearest EVEN number:
print(round(1.5))
print(round(2.5))
print()

# negative numbers round to 10s places
num = 125679
print(round(num, -1))
print(round(num, -3))
print()

# don't confuse this with number formatting for output
num = 1.234567
print(format(num, "0.2f"))
print(format(num, "0.5f"))  # this will round it to 1.23457
