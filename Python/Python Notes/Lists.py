#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: Nafiseh
"""

# Lists
# -------------------------------

[1951, 1969, 1984]                     # A list of integers
['apples', 'oranges', 'cherries']      # A list of strings
[]                                     # An empty list    
[[5, 9], [541, 78]]                    # A list of lists


# -------------------------------

import math
x = 2
[x, math.sqrt (x)]
[x + 1]

# ------------------------------
first = [1, 2, 3, 4]
second = list (range (1, 5))
first
second

third = list ("Hi there!")
third

len (first)
first [0]
first [2:4]


first + [5, 6]
first == second

# ------------------------------
print ("1234")
print ([1, 2, 3, 4])

# ------------------------------

for element in [1, 2, 3, 4, 5]:
 print (element)

# ------------------------------
3 in [1, 2, 3]

0 in [1, 2, 3]

# -----------------------------
example = [1, 2, 3, 4]
example

example [3] = 0
example

# -----------------------------

numbers = [2, 3, 4, 5]
numbers

index = 0
while index < len (numbers):
    numbers [index] = numbers [index] ** 2
    index += 1
numbers

numbers = [2, 3, 4, 5]
for index in range (len(numbers)):
    numbers [index] = numbers [index] ** 2
numbers    

# ---------------------------
sentence = "This homework has five questions."
words = sentence.split ()
words
for index in range (len (words)):
    words [index] = words [index].upper ()
words

# --------------------------
numbers = list (range (6))
numbers

numbers [0:3]= [11, 12, 13]
numbers

# --------------------------
example = [1, 2]
example

example.insert (1, 10)
example
example.insert (3, 25)
example

# -------------------------
example = [1, 2]
example

example.append (3)
example

example.extend ([11, 12, 13])
example

example + [14, 15]

example

# -------------------------
time_set = []       # equivalent to time_set = list()
time_span = 7
for t in range(1, time_span + 1):
    time_set.append(t)
print(time_set)
print(len(time_set))


node_set = []        # equivalent to node_set = list()
node_num = 5
for i in range(1, node_num + 1):
    node_set.append('n%s' % i)
print(node_set)

# --------------------------
example

example.pop ()         # Remove the last element

example

example.pop (0)      # Remove the first element

example
# -------------------------
mylist = ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave']
mylist.remove ('Alice')
print (mylist)

mylist.remove('Bob')
print (mylist)

# ---------------------------
mylist3= list (range(10))
del mylist3[0]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print (mylist3)

mylist3= list (range(10))
del mylist3 [2:5]
print (mylist3) # [0, 1, 5, 6, 7, 8, 9]
mylist3= list (range(10))
del mylist3 [:3]
print (mylist3) # [3, 4, 5, 6, 7, 8, 9]
mylist3= list (range(10))
del mylist3 [4:]
print (mylist3) # [0, 1, 2, 3]

# ---------------------------
aList = [34, 45, 67]
target = 45
if target in aList:
    print (aList.index (target))
else:
    print (-1)

mylist4 = [0, 1,2,3]
if 0 not in mylist4:
    print (mylist4)
else:
    print ("there is zero in this list")
# ---------------------------
example = [4, 2, 10, 8]
example

example.sort()
example
# ----------------------

vowels = ['e', 'a', 'u', 'o', 'i']    # vowels list
vowels.sort ()                        # sort the vowels 
print ('Sorted list:', vowels)        # print vowels 

vowels = ['e', 'a', 'u', 'o', 'i']                    # vowels list
vowels.sort (reverse=True)                 # sort the vowels 
print('Sorted list (in Descending) --- >', vowels)     # print vowels 

# --------------------------
bList = [1, 3, 2, 5]
bList.sort()
cList = bList.sort()
print (bList)        # [1, 2, 3, 5]
print (bList.sort()) # None
print (cList)        # None
# -------------------------
fruits = ("apple", "banana")
fruits

meats = ("fish","poultry")
meats

food = meats + fruits
food

veggies = ["celery", "beans"]
tuple (veggies)
print (tuple (veggies))














