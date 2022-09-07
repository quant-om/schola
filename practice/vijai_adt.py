
# Python Abstract Data Types
# list, tuple, dict, set, frozenset

# 1. list = list of objects, objects are instances of any data type, it can be both basic data type and abstract data type. It can also be a user defined data type.
# A list is a list of objects (like int, str, list, class etc)
mylist = list()
mylist1 = [ 1, 2, 3, 4.5, True, "quantom", [4.5, False, "schola"], (3.4, True), {"one": 1, "two": 2} ]

print(f"111- list is {mylist}")
len_list = len(mylist)
print(f"111- list len is {len_list}")

mylist1.append(False)

print(f"111222- mylist is {mylist1}")
len_list = len(mylist1)
print(f"111222- mylist len is {len_list}")

mylist.append(1234)
mylist.append("quantom")

print(f"222- list is {mylist}")
len_list = len(mylist)
print(f"222- list len is {len_list}")

# dict
# A dictionary is a data type which holds key/value pair
# Keys should be only immutable objects, usually we give str as keys, value can be any object

# Empty dict
mydct = dict()
mydct1 = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4
}
print(f"333- mydct is {mydct1}")
len_dct = len(mydct1)
print(f"333- mydct len is {len_dct}")
mydct1["five"] = 5