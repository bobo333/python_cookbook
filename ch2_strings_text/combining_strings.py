# .join
parts = ['hi', 'there', 'mr', 'guy']
print(' '.join(parts))

# +, but why? + is very inefficient
print('hi' + ' ' + 'there')

# smush them
a = 'hi ' 'there'
print(a)

# consider other options depending on the situation
a = 'a'
b = 'b'
c = 'c'
print(a + ':' + b + ':' + c)    # bad
print(':'.join([a, b, c]))      # slightly better
print(a, b, c, sep=':')         # good
print()


# consider using a generator if building input from lots of small strings
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

print(''.join(sample()))
for part in sample():
    print(part)
