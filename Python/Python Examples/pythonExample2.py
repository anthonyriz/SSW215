#Example 1
side1 = int(input("Enter Side 1: "))
side2 = int(input ("Enter Side 2: "))
side3 = int(input ("Enter Side 3: "))

if side1 == side2 and side2 == side3:
	print ("Triangle is equilateral.")
elif pow(side1,2 ) + pow(side2, 2) == pow(side3, 2) or pow(side1,2 ) + pow(side3, 2) == pow(side2, 2) or pow(side3,2 ) + pow(side2, 2) == pow(side1, 2):
	print ("Triangle is a Right Triangle.")
else:
	print ("The triangle is neither a right triangle nor equilateral.")


