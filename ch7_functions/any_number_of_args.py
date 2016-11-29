import html


# rest is a tuple of all the remaining positional arguments. The code treats it as a sequence
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


print(avg(1, 2))
print(avg(1, 2, 3, 4))


# accept any number of keyword arguments
def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(name=name, attrs=attr_str, value=html.escape(value))
    return element


print(make_element('item', 'Albatross', size='large', quantity=6))
print(make_element('p', '<spam>'))


# to get any positional and keyword args, use these in combinations
def any_args(*args, **kwargs):
    print(args)     # tuple
    print(kwargs)   # dict


any_args()


# * argument can only be the last positional argument
# ** argument can only be the last keyword argument
# the following is allowed, but y is a keyword-only argument
def weird(x, *args, y, **kwargs):
    pass
