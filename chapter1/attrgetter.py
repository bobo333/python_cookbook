from operator import attrgetter

# similar to itemgetter, but used for attributes of objects


class Person(object):
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return "Person: {}".format(self.user_id)


people = [Person(23), Person(3), Person(99)]
print(people)

sorted_by_id = sorted(people, key=attrgetter('user_id'))
print(sorted_by_id)

max_id = max(people, key=attrgetter('user_id'))
print(max_id)
