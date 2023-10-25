#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: Nafiseh
"""

# 04 Examples
# ---------------------------------------

# Example 1
# ----------------------------------------

squares = {} 
for x in range (1, 16): 
	squares [x] = x*x 
print (squares)


# Example 2
# ----------------------------------------
my_dict1 = {'data1':100,'data2':-54,'data3':247} 
result=1 
for key in my_dict1: 
	result=result * my_dict1 [key] 
print (result)


# Example 3
# ----------------------------------------
letters = "abcabcdefghi"
frequencies = {} 
for c in letters:
	frequencies [c] = frequencies.get (c, 0) + 1
print (frequencies) 

for f in frequencies.items ():
	print (f)             
    

# Example 4
# ----------------------------------------
my_dict2 = {'data1':100,'data2':-54,'data3':247} 
print (sum (my_dict2.values()))


# Example 5
# ----------------------------------------    
from collections import Counter 
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400} 
d = Counter (d1) + Counter (d2) 
print(d)

# Example 6
# ----------------------------------------  

my_dict3 = {'x':500, 'y':5874, 'z': 560} 
key_max = max (my_dict3.keys (), key=(lambda k: my_dict3 [k]))
key_min = min (my_dict3.keys (), key=(lambda k: my_dict3 [k])) 
print ('Maximum Value: ',my_dict3 [key_max]) 
print ('Minimum Value: ',my_dict3 [key_min])

# Example 7
# ----------------------------------------  

import random

name_list = []
salary_list = []
report_dict = {}

for i in range (3):
    name = input ('Enter Name '+ str (i+1)+ ':') # Names should be unique
    salary = random.randint (45000, 110000) # Salary is randomely generated
    #salary = input ('Enter the salary for ' + name + ':')
    #salary = int (salary)
    name_list.append (name)
    salary_list.append( salary)
    report_dict[name]=salary
print ('The report of the salary is --->', report_dict)
