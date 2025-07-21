# immutable objects can be hashed so they can be stored in sets and be keys in dicts

#hashable: int, str, tuple of immutables
#list and dict and set are not hashable


# how to make yopur own class hashable:
# define __hash__(self): and __eq__(self, other):