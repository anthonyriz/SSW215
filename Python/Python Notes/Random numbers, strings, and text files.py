#!/usr/bin/env python3
# -*- coding: utf-8 -*-



#@author: Nafiseh


# Random numbers, strings, and text files

# ---------------------------------------
#import random
#for roll in range (10):
#    print (random.randint (1, 6))

# ----------------------------------------
import random
smaller = int (input ("Enter the smaller number: "))
larger = int (input ("Enter the larger number: "))
myNumber = random.randint (smaller, larger)
count = 0
while True:
    count += 1
    userNumber = int (input ("Enter your guess: "))
    if userNumber < myNumber:
        print ("Too small!")
    elif userNumber > myNumber:
        print ("Too large!")
    else:
        print ("Congratulations! You've got it in", count,"tries!")
        break

# -------------------------------------------
A = len ("Hi there!")
print ("This is A --->", A)

B = len (" ")
print ("This is B --->", B)

# ------------------------------------------
name = "Tom leader"

name [0]                  # Examine the first character
name [4]                  # Examine the fourth character
# name [len (name)]         # Oops! An index error!
name [len (name) - 1]     # Examine the last character
name [-1]                 # Shorthand for the last one

# ------------------------------------------
data = "Hi there!"
for index in range (len (data)):
    print (index, data[index])

# ------------------------------------------
name = "myfile.txt"
name [0:]              # The entire string
name [0:1]             # The first character
name [0:2]             # The first two characters
name [:len (name)]     # The entire string
name [-3:]             # The last three characters

# ------------------------------------------
mylist = [2,4,6,8,10]
for i in range (len (mylist)):
    mylist[i]= mylist [i]+3
print ("Here is the new list ---> ", mylist)    


# ------------------------------------------
fileList = ["myfile.txt", "myprogram.exe", "yourfile.txt"]
for i in fileList:
    if ".txt" in i:
        print (i)

"myfile.txt".split ('.')
"myfile.py".split ('.')

# ------------------------------------------
f = open ("Test.txt", 'w')
f.write ("First line.\nSecond line.\n")
f.close ()

# -----------------------------------------
# outFileName = ("/Users/Nafiseh/My-Files/OU-Spring 2021/myfile.txt")
# outFile = open(outFileName, "w")
# outFile.write("""Hello my name is Tom""")
# outFile.close()

# -----------------------------------------
import random
f = open ("integers.txt", 'w')
for count in range (500):
    number = random.randint (1, 500)
    f.write (str (number) + "\n")
f.close ()

#-----------------------------------------
f = open ("Test.txt", 'r')
text = f.read ()
text
print (text)

# -----------------------------------------
f = open ("Test.txt", 'r')
for line in f:
    print (line)

# -----------------------------------------
f = open ("Test.txt", 'r')
while True:
    line = f.readline ()
    if line =="":
        break
    print (line)

# -----------------------------------------
f = open ("integers.txt", 'r')
sum = 0
for line in f:
    line = line.strip ()
    number = int (line)
    sum += number
print ("The sum is", sum)






