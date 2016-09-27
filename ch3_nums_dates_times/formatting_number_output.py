x = 1234.56789

# two decimal places of accuracy
print(format(x, '0.2f'))

# right justified in 10 chars, one-digit of accuracy
print(format(x, '>10.1f'))

# left justified
print(format(x, '<10.1f'))

# centered
print(format(x, '^10.1f'))

# inclusion of thousands separator
print(format(x, ','))

# can use exponential notation by using e or E instead of f
print(format(x, 'e'))
print(format(x, '0.2E'))
print()

# these format codes also work when formatting strings
print('The value is {:0,.2f}'.format(x))

# thousands representation (with the comma) is not locale-aware. Can use the translate function to switch to periods
swap_separators = {
    ord('.'): ',',
    ord(','): '.'
}

print(format(x, ',').translate(swap_separators))

# % can also be used to format python strings
print('%0.2f' % x)
print('%10.1f' % x)
