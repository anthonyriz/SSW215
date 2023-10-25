#Example 1
"""import math

radius = int(input ("Enter the radius of the circle: "))

area = math.pi * pow(radius, 2)

print ("Area: ", area)"""

#Example 2

"""length  = int(input("Enter the length of a side: "))

surfaceArea = 6 * pow(length, 2)

print ("Surface Area: ", surfaceArea)"""

#Example 3

"""new = int(input("Enter number of new videos: "))

oldies = int(input("Enter number of oldies: "))

total = (3*new) + (2*oldies)

print ("Total: $", round(total, 2))"""

#Example 4

hourlyWage = int(input ("Hourly Wage: "))
regularHours = int(input ("Total Regular Hours: "))
overtimeHours = int(input ("Total Overtime Hours: "))

if overtimeHours > 1:
    weeklyPay = (hourlyWage * regularHours) + ((1.5 * hourlyWage)*overtimeHours)
else: 
    weeklyPay = hourlyWage * regularHours 

print ("Total Weekly Pay: ", weeklyPay)



