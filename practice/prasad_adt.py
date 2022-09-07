# Abstract Data Types
# 1) list[]
list = list()   # list = []
print(f"the list is: empty {list}")

# creating values in list
new_list = [5,-20.5,"hi",True, None]
print(f"the list is {new_list}")
print(f"the lenth of the list is {len(new_list)}")

# adding one name in list 
new_list.append("quantom")
print(f"the list is {new_list}")
print(f"the lenth of the list is {len(new_list)}")

# adding small list in list
slist = [-0, 9.999, "great"]
add_small_list = [5, -20.5, 'hi', True, None, 8, 'quantom', slist]
print(f"the list is {add_small_list}")
print(f"the lenth of the list is {len(add_small_list)}")

# finding Index values in list
mylist = [5, -20.5, 'hi', True, None, 8, 'quantom', slist]
print(f"the 3rd object of index is {mylist[2]}")

# Negative Indexing
mylist = [5, -20.5, 'hi', True, None, 8, 'quantom', slist]
print(mylist[-1])
print(mylist[-3])

# Range of Indexes  # Index starts with 0
mylist = [5, -20.5, 'hi', True, None, 8, 'quantom', slist]
print(mylist[2:5])
print(mylist[:4])    # from the beginning Indexing

# Remove Specified Item
mylist = [5, -20.5, 'hi', True, None, 8, 'quantom', slist]
mylist.remove(8)
print(mylist)

# Remove Specified Index
mylist = [5, -20.5, 'hi', True, None, 8, 'quantom', slist]
mylist.pop(3)
print(mylist)

# 2) tuple

thistuple = ("apple", "banana")
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Different data types in tuple
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

# Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)


# 3) dict

# a = dict(one=1, two=2, three=3)
# b = {'one': 1, 'two': 2, 'three': 3}
# c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
# d = dict([('two', 2), ('one', 1), ('three', 3)])
# e = dict({'three': 3, 'one': 1, 'two': 2})
# f = dict({'one': 1, 'three': 3}, two=2)

# all ways are equals   a == b == c == d == e == f





# 4) set
# 5) frozenset
