# Dictionaries

band = {
  "vocals": "Plant",
  "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

#Access items in dictionaries

print(band['guitar'])
print(band.get('guitar'))

# List all keys
print(band.keys())

#list all values 
print(band.values())

# list of key value pairs as tuples
print(band.items())

#verify a key exist 
print("guitar" in band)
print("triangle" in band)

#Change values 
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# Remove items 
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) #tuple
print(band)

#delete and clear items 
band["drums"] = "Bonham"
print(band)
del band["drums"]
print (band)

band2.clear()
print(band2)

del band2

#copy dictionaries 

# band2 = band #creates a reference (i.e referring to the same dictionary and not a copy of the dictionary)
# print("Bad copy")
# print(band2)
# print(band)

# band2["drum"] = "Dave"
# print(band)

band2 = band.copy()
band2["drum"] = "Dave"
print("Good Copy")
print(band)
print(band2)

#or use the dict() constructor function
band3 = dict(band)
print("Good Copy") 
print(band3) 

# nested dictionaries
member1 = {
  "name": "Plant",
  "Instrument": "vocals"
}
member2 = {
  "name": "Page",
  "Instrument": "guitar"
}

band = {
  "member1": member1,
  "member2": member2
}

print(band)
print(band["member1"]["name"])


# Sets 
nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums2))
print(len(nums2))

#no duplicates allowed 
nums = {1, 2, 2, 3}
print(nums)

# true is a dupe of 1 and false is a dupe of 0 (Zero)
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if a value is in a set 
print(2 in nums)

#but you cannot refer to an element in the set using with an index position or key 

#add a new element to a set 
nums.add(8)
print(nums)

#add elements from one set to another 
more_nums = {5, 6, 7}
nums.update(more_nums)
print(nums)

#you can use update method with lists, tuples and dictionaries too

#merge two sets to create a new set 
one = {1, 2, 3}
two = {5, 6, 7}

my_new_set = one.union(two)
print(my_new_set)

#keep only duplicates 
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

#keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print("one",one)