#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: Nafiseh
"""

# Dictionaries
# ---------------------------------------
"""
info = {} 
info ["name"] = "Sandy" 
info ["occupation"] = "hacker"
print (info)

# --------------------------------
info ["occupation"] = "manager"
print (info)

# ------------------------------------
print (info ["name"])

# print (info ["job"])  # an error is raised, key is not present in dictionary 

if "job" in info: 
	print (info ["job"]) 
else:
	print ("None")

# ------------------------------------
info = {'name':'Sandy','occupation':'manager'} 
print (info.get ("family_name", 0))      # the defual value could be None
print (info.get ("occupation", None))

# -------------------------------
print (info.pop ("occupation"))
print (info)

# -------------------------------
grades = {'John':'A', 'Emily':'A+', 'Betty':'B', 'Mike':'C'}
grades_new = {'John':'B', 'Sam':'A', 'Betty':'A'}
grades.update (grades_new)
print (grades)

# -------------------------------
grades2 = {'John':'A', 'Emily':'A+', 'Betty':'B', 'Mike':'C'}
for i in grades2:
    print (i)

# -------------------------------    
for key in info:
	print (key, info [key]) 
    
mygrades = {90:'A', 80:'B', 70:'C'} 
list (mygrades.items ())

for (key, value) in mygrades.items (): 
	print (key, value)
print (list ((mygrades.items())))


# --------------------------------
# Sort a dictionary using a for loop

dict1 = {1: 1, 2: 9, 3: 4}
sorted_values = sorted(dict1.values()) # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in dict1.keys():
        if dict1[k] == i:
            sorted_dict[k] = dict1[k]
            break

print(sorted_dict)

# ------------------------------
# Sort dictionary using the sorted () function

dict1 = {1: 1, 2: 9, 3: 4}
sorted_dict = {}
sorted_keys = sorted(dict1, key=dict1.get)  # [1, 3, 2]

for w in sorted_keys:
    sorted_dict[w] = dict1[w]

print(sorted_dict) # {1: 1, 3: 4, 2: 9}

# --------------------------------
# Sort dictionary using a lambda function

dict1 = {1: 1, 2: 9, 3: 4}
sorted_tuples = sorted(dict1.items(), key=lambda item: item[1])
print(sorted_tuples)  # [(1, 1), (3, 4), (2, 9)]

sorted_dict = {k: v for k, v in sorted_tuples}
print(sorted_dict)  # {1: 1, 3: 4, 2: 9}

# -------------------------------
d = {"Pierre": 42, "Anne": 33, "Zoe": 24}
sorted_d = sorted(d.items(), key=lambda x: x[1])
print (sorted_d)"""
# -------------------------------
my_info = {'name':'Sandy','occupation':'manager', 'age': '38'} 
theKeys = list (my_info.keys ())
theKeys.sort()
print (theKeys)

for key in theKeys: 
    print (key, my_info [key]) 
    
