#Example 1
"""myDict = {}

for i in range (1,16):
    myDict [i] = i*i

print (myDict)"""

#Example 2
"""myDicti = {2:2, 1:4, 4:1, 6:9}
product = 1

for i in myDicti:
    product = product * myDicti[i]

print (product)"""

#Example 3

"""letters = "aabcdefghi"

frequencies = {}

for c in letters:
    frequencies [c] = frequencies.get (c,0) + 1

for f in frequencies.items():
    print (f)"""

#Example 4

"""myDictionary = {2:2, 1:4, 4:1, 6:9}
sum = 0

for i in myDictionary:
    sum = sum + myDictionary[i]

print (sum)"""

#Example 5

"""from collections import Counter

dict_one = {2:2, 1:4, 4:1, 6:9}
dict_two = {1:6, 2:8, 3:16, 9:10}

dict_new = {Counter(dict_one) + Counter(dict_two)}

print (dict_new)        #fix"""

#Example 6

"""dict_six = {{2:2, 1:4, 4:1, 6:9}}

key_max = max (dict_six.keys(), key = (lambda k: dict_six [k]))
key_min = min (dict_six.keys(), key = (lambda k: dict_six [k]))"""
#fix

#Example 7

import random

employ_dict = []
salary_list = []
report_dict = {}

for i in range(3):
    name = input ("Enter the employee's name: ")
    salary = random.randint(5000,25000)
    employ_dict.append(name)
    salary_list.append(salary)
    report_dict [name] = salary

print("Report: ", report_dict)




