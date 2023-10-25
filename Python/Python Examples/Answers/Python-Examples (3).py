
# 03 Examples
# ---------------------------------------

# Example 1
# ---------------------
data = [1, -2, 5, 6, 0, 5, 0, 3]
result = []
for number in data:
    if number !=0:
        result.append (number)

print ("Updated list is --->", result)



# ---------------------
# Example 2
# ---------------------
N = int(input("Enter a number: "))
mylist1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
mylist1.sort(reverse=True)
print (mylist1)
final_list=mylist1[:N]
print (final_list)


# ---------------------
# Example 3
# ---------------------
# ---------------------
num2 = int(input("Display multiplication table of? "))
for i in range(1, 11):
   print(num2, 'x', i, '=', num2*i)

# ---------------------
# Example 4
# ---------------------
num1 = int(input("Enter a number: "))
factorial = 1
if num1 < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num1 == 0:
   print("The factorial of 0 is ---> 1")
else:
   for i in range(1,num1 + 1):
       factorial = factorial*i
print("The factorial of",num1,"is --->",factorial)

# --------------------
# Example 5
# ---------------------

mylist2 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
size = len (mylist2)
repeated = []
for i in range(size):
    k = i + 1
    for j in range(k, size):
        if mylist2[i] == mylist2[j] and mylist2[i] not in repeated:
            repeated.append(mylist2[i])
print (repeated)

# ---------------------
# Example 6
# ---------------------

f = open ("Python/Python Examples/median.txt", 'r')
numbers = []
for line in f:
    words = line.split ()
    for word in words:
        numbers.append (float(word))

# sort the list and print the number at its midpoint
numbers.sort ()
midpoint = len(numbers)
if midpoint % 2 == 0:
    median1 = numbers [midpoint//2]
    median2 = numbers [midpoint//2-1]
    median = (median1 + median2)/2

else:
    median = numbers [midpoint//2]
print ("sorted numbers", numbers)
print ("total numbers in the list --->", len(numbers))
print ("Here is the median --->", median)

# ---------------------
# Example 7
# ---------------------

NumList = []
positive =[]
negative = []
j = 0

Number = int (input("Please enter the total number of list elements:"))
for i in range (1, Number +1):
    value = int (input ("please enter the value of %d element:" %i))
    NumList.append (value)
    
while (j < Number):
    if (NumList[j]>=0):
        positive.append (NumList[j])
    else:
        negative.append(NumList[j])
    j =j+1    
    
print ("Element in positive list is:",positive)    
print ("Element in negative list is:",negative)

# note that {} is a replacement filed for num    


# ---------------------
# Example 8
# ---------------------

num = int (input ("Enter a number: "))
if (num%2)== 0:
    print ("{0} is Even".format(num))
else:
    print ("{0} is Odd".format(num))    

# ---------------------
# Example 9
# ---------------------

number = int(input ("Enter the number"))

p=0

for i in range (2, number):
    if number%i==0:
        p = 1
        break

if p==0:
    print ("{0} is a prime number".format(number)) 
else:
    print ("{0} is not a prime number".format(number)) 
    

for Number in range (1, 101):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')