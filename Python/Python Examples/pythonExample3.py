# Example 1
"""list_one = [1, -2, 5, 6, 0, 5, 0, 3]
result = []
for number in list_one:
    if number !=0:
        result.append (number)
        print (result)
print (result) """

#Example 2

"""list_one = [1, -2, 5, 6, 0, 5, 0, 3]

list_one.sort(reverse=True)

print (list_one[0])"""

#Example 3

"""x = int(input("Enter a number: "))
for i in range (1,11):
    print (x, '*', i, '=', x*i) """

#Example 4

"""number = int(input ("Enter number you want facotrial of:"))
factorial = 1

for i in range(1, number + 1):
       factorial = factorial*i

print ("Factorial of ", number, " is: ", factorial)"""

#Example 5

listOne = [3, 4, 2, 2, 5, 1, 20, 20, 6, 3, 1, 3, 8, 10]
duplicates = []

for i in range (len(listOne)):
    k = i + 1
    for j in range (k, len(listOne)):
        if listOne[i] == listOne [j] and listOne[i] not in duplicates:
            duplicates.append(listOne[i])

print (duplicates)

#Example 6

