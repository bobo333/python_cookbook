# if hashable, can use set directly
# maintains the order of the items


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


my_items = [3, 5, 11, 7, 3, 5, 9]

deduped = list(dedupe(my_items))
print(deduped)


# if not hashable, use a key function to make them hashable
def dedupeunhashable(items, key):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield val
            seen.add(val)


my_items2 = [{'x': 1, 'y': 2}, {'x': 3, 'y': 2}, {'x': 1, 'y': 2}]
deduped2 = dedupeunhashable(my_items2, key=lambda x: (x['x'], x['y']))
print(list(deduped2))
