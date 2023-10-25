#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""



@author: Nafiseh
"""


# Python-Examples (5)
# --------------------------

# Example #1

def recur_factorial (n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n-1)
    
num = int (input ("Enter the number: "))  
if num < 0:
    print ("sorry, factorial does not exist for negative numbers")   
elif num == 0:
    print ("The factorial of 0 is 1") 
else: 
    print (" The factorial of", num, "is", recur_factorial (num))    
    

# Example 2    

def Euler_1 (number): 
    value = 1
    for i in range(terms):
        value = value+ (1/recur_factorial(i+1))
    return value  

terms = int (input ("Enter the number of terms for compute the value of Euler's number : "))  
print ("Euler value for", terms, "terms --->", Euler_1 (terms)) 
