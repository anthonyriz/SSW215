# I pledge my honor that I have abided by the Stevens Honor System. x Anthony Rizzuto

#Problem 1
print ("Problem 1:")

n = int(input ("Number of terms of the Fibonacci Sequence you would like to see: "))

fibonacci = 0
term1 = 0
term2 = 1
i = 0

print ("The Fibonacci Sequence up to the", n, "term is:")

while i < n:
    print (term1)
    fibonacci = term1 + term2
    term1 = term2
    term2 = fibonacci
    i += 1

#Problem 2

print ("Problem 2:")

myDict = {}

import random

myDict ["A"] = random.randint(-100, 100)               #Was not sure if you wanted user to input numbers or use the myDict Sample
myDict ["B"] = random.randint(-100, 100)
myDict ["C"] = random.randint(-100, 100)
myDict ["D"] = random.randint(-100, 100)
myDict ["E"] = 95


print (myDict)

for i in myDict:
    if myDict[i] > 1:
        for b in range(2, myDict[i]):
            if (myDict[i] % b) == 0:
                print (i, "is not prime.")
                break
            else:
                print (i, "is prime.")
                break
    else:
        print (i, "is not prime.")

#Problem 3

print ("Problem 3:")

number = int(input ("Enter a number: "))
exponent = int(input ("Enter the exponent: "))

if exponent < 0:
    print ("Exponent cannot be a negative.")
    exit()
else:
    def expo(number, exponent):
        product = 1
        for a in range(exponent):
            product = product * number
        return product
        
print ("Answer: ", expo(number, exponent))
        