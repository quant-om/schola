# Python Abstract data types
# 1. List
mylist = list()
mylist1 = [1, 5.6, -1, 0]
len_list = len(mylist1)

mylist1.append("happy")
mylist1.append("Quantom")
mylist.append(True)
mylist.append(None)

len_list = len(mylist1)
len_list0 = len(mylist)

print(f"The elements of mylist1 are {mylist1}")
print(f"the length of mylist1 is {len_list}")
print(f"The list of mylist is {mylist}")


# 2. Tuple
mytuple = tuple()
mytuple1 = ()
mytuple1 = (1, 3, True, "happy", None)

print(f"Mytuple: {mytuple1}")

for val in mytuple1:
    print(f"The val = {val}")


# 3.Dictionary
dict1 = dict()
dict2 = {}
dict2 = {
    "zero" : 0,
    "one" : 1,
    "two" : 2,
    "three" : 3
}
print(f"dict2 = {dict2}")

all_keys = dict2.keys()
all_vals = dict2.values()

print(f"The keys are {all_keys}")
print(f"The values are {all_vals}")

for key in dict2 :
    print(f"The key = {key}, val = {dict2[key]}")

# Add a new element to dict2
dict2["four"] = 4
for keys in dict2 :
    print(f"Key = {keys}, val = {dict2[keys]}")





