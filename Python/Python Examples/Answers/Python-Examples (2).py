#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: Nafiseh
"""


# 02 Example 
# -----------------------------------------
side1 = int (input ("Enter the first side: "))
side2 = int (input ("Enter the second side: "))
side3 = int (input ("Enter the third side: "))
square1 = side1 ** 2
square2 = side2 ** 2
square3 = side3 ** 2
if side1 == side2 and side2 == side3:
    	print("The triangle is equilateral.")
elif square1 + square2 == square3 or \
     	square2 + square3 == square1 or \
     	square1 + square3 == square2:
        print("The triangle is a right triangle.")
else:
        print ("The triangle is not a right triangle or equilateral.")