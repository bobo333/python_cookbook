

# can annotate function args for clarity
# these do NOT affect the python interpreter at all, it does NOT introduce a type check or anything else, just info
# for the user
def add(x: int, y: int) -> int:
    return x + y


help(add)

# annotations are stored in the functions __annotations__ attribute
print(add.__annotations__)
