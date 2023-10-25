#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: Nafiseh
"""

# Loops and selection statements

# -------------------------------------
for i in range (4):
    print("This HW has 3 questions!")
    

# ----------------------
number = 2
exponent = 3
product = 1
for i in range (exponent):
    product = product * number
print ("product --->", product)
    

# ------------------------
for count in range (4):
    print (count)
    

# ------------------------
product = 1
for count in range (4):
    product = product * (count + 1)
print ("product --->", product)
    

# ------------------------
product = 1
for count in range (1, 5):
      product = product * (count)
print ("product --->",product)


# ------------------------
lower = int (input ("Enter the lower bound: "))
upper = int (input ("Enter the upper bound: "))
sum = 0
for count in range (lower, upper + 1) :
    sum = sum + count
print ("sum --->", sum)   


# -------------------------
list (range (4))

list (range (1, 5))

# -------------------------
list (range (1, 6, 1))     

list (range (1, 6, 2))     

# -------------------------
test = list (range (4))
# test = [0,1,2,3] 
for i in test :
    print ("This is i---> ", i)

# -------------------------
for count in range (10, 0, -1):
    print ("this is count --->", count)
 
# -------------------------
test = list (range (10, 0, -1))
print (test)

# --------------------------
a = 17
s = "hi "
a += 3      # Equivalent to a = a + 3
print (a)  
a -= 3      # Equivalent to a = a − 3
print (a)  
a *=3       # Equivalent to a = a * 3
print (a)  
a /=3      # Equivalent to a = a / 3
print (a)  
a %=3     # Equivalent to a = a % 3
print (a)  
s +="there"
print (s)  
  

# -------------------------
import math
area = float (input ("Enter the area: "))
if area > 0:
    radius = math.sqrt (area / math.pi)
    print ("The radius is ---> ", radius)
else:
    print ("Error: the area must be a positive number")


# ----------------------------------
# if and if-else statements: example
#-----------------------------------
grade = float (input ("Enter the numeric grade: "))
if grade < 0 or grade > 100:
    print ("Error: grade must  be  between 100 and 0")
elif grade >89:
    print ("the grade letter is ----> A")
elif grade >79 and grade <90:
    print ("the grade letter is ----> B")
elif grade >69 and grade <80:
    print ("the grade letter is ----> C")
else:
    print ("the grade letter is ----> D")

# --------------------------
A = True
B = False

A and B
A or B
not A

# --------------------------
# Summation with a for loop
sum = 0
for count in range (1, 100001):
    sum += count
print ("this is sum --->",sum)

# Summation with a while loop
sum = 0
count = 1
while count <= 100000:
    sum += count
    count += 1
print ("this is sum --->", sum)


# --------------------------
# printing out the count with a for loop
for count in range (10, 0, -1):
    print ("this is count--->", count)

# printing out the count with a while loop
count = 10
while count >= 1:
    print ("this is count --->", count)
    count -= 1
    
# -------------------------
sum = 0
while True:
    data = input ("Enter a number  or just enter to  quit:  ")
    if data  == "" :
        print ("Number is not entred")
        print ("The sum is--->", sum)
        break
    number = float (data)
    sum += number
    print ("The sum is--->", sum)
    
# --------------------------
while True:
    number = float (input ("Enter the numeric grade: "))
    if number >= 0 and number <= 100:
         break
    else:
         print ("Error: grade must  be  between 100 and 0")
print ("the grade is ---->", number)



