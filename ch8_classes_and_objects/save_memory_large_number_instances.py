# using the __slots__ attribute can greatly reduce memory footprint
class Date:
    # __slots__ changes how the instances are represented in memory, they are no longer dicts with keys as attributes,
    # instead they are built around a fixed-size array and the attributes are mapped to specific indices in that array
    # this is much more efficient, however it means additional attributs can no longer be added to those instances, it
    # is limited to what is already in __slots__
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


my_date = Date(2017, 'January', 13)
print(my_date)

# although the memory footprint is reduced, this should be avoided if possible because much of python's tools rely
# on the dictionary representation of objects. For instance, using __slots__ means that class can no longer use
# multiple inheritance
