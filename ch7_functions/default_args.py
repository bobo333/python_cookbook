

# default arguments must appear last
def spam(a, b=42):
    print(a, b)


spam(1)
spam(1, 2)

# if the default value is supposed to be a mutable container, such as a list, set, or dict, use None as the default and
# set the value inside the function. Otherwise, the container will be created once when the function is declared, and
# the the SAME container will be used for all calls of the function, so it will not yield expected results.


# ex:
def bad_job(a, b=[]):
    b.append(a)
    return b


first = bad_job(1)
print(first)

second = bad_job(2)
print(second)   # is [1, 2] instead of the expected [2]


def good_job(a, b=None):
    if b is None:
        b = []
    b.append(a)
    return b


first_good = good_job(1)
print(first_good)

second_good = good_job(2)
print(second_good)  # will be [2] as expected
print()

# can check for no interesting value like so:
# this is an intentionally useless object, can't even set attributes. Useful for testing
# identity like here
_no_value = object()


def interest(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')


interest(1)     # this is the only one that prints the statement
interest(1, 2)
interest(1, None)

# note there is a difference between passing None and no value at all

print()

# default values are assigned only at function definition time. ex:
x = 55


def fifty_five(p=x):
    print(p)


fifty_five()

x = 99

fifty_five()    # still prints 55
print()

# rather than using if not [var], use if [var] is None to avoid problems:


def bad_none_check(a=None):
    if not a:
        print('NOT a')


bad_none_check()    # prints
bad_none_check('')  # prints
bad_none_check([])  # prints
print()


def good_none_check(a=None):
    if a is None:
        print('NOT a')


good_none_check()       # prints
good_none_check('')     # does NOT print
good_none_check([])     # does NOT print
