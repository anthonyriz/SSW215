#Problem 1      which choices outputs numbers 1-10? Select all (Given a piece of paper with 5 choices)

    #Choice 2
n = 1           
while n <= 10:
    print (n)
    n = n+1

    #Choice 4
for n in range (0,10):     
    print (n + 1)

    #Choice 5
n = 1       
while n != 11:
    print (n)
    print (n+1)
    n = n +2

#Problem 2                      Let user enter in two numbers and dislay larger number using multiway if statement

num1 = int(input ("Enter first number: "))
num2 = int(input ("Enter second number: "))

if num1 > num2:
    print ("Larger number: ", num1)
elif num2 > num1: 
    print ("Larger number: ", num2)
else:
    print ("Numbers are equal.")

#Problem 3                  Display all prime numbers from 1-100

primeNumbers = []
for number in range (1, 101):
    i = 0
    for j in range(2, (number//2 + 1)):
        if(number % j == 0):
            i =+1 
            break
    if (i == 0 and number != 1):
        primeNumbers.append(number)

print ("Prime Numbers from 1 - 100: ", primeNumbers)


#Problem 4              Q: allow user to enter elements of a list and display the original list and the list reversed WITHOUT using the reverse method 

originalList = []
reverseList = []   

entries = int(input("How many entries will you like to enter? "))
if entries <= 1:
    print("Need at least 2 entries.")
else:
    for a in range(entries):
        element = int(input ("Enter number " + str(a+1)+ ": "))
        originalList.append(element)


reverseList = originalList.pop()

print("Original List: ", originalList)
print ("Reversed List: ", reverseList)


