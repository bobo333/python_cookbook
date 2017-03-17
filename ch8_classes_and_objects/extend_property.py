class Person:
    def __init__(self, name):
        self._name = name

    # getter fxn
    @property
    def name(self):
        return self._name

    # setter fxn
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    # Deleter fxn
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    """
    Extends the name property and functionality
    """
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        # to get the parent's implementation of the setter, control needs to go through the __set__ method of the
        # name property. However, the only way to get to that is as a class variable, not an instance variable, hence
        # why super is used in this way
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


s = SubPerson('Guido')
print(s.name)

s.name = 'Larry'

try:
    s.name = 42
except TypeError:
    print('Type error dude!')


print()


# to override just one method
class SubPersonDeux(Person):
    @Person.name.setter
    def name(self, value):
        print('setting name to: ', value)
        super(SubPerson, SubPerson).name.__set__(self, value)


s2 = SubPersonDeux('guido')
s2.name = 'harry'
