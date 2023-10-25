# Problem 1

print("Problem 1:")
numbers = input ("Enter numbers seperated by a space: ").split()

for n in range(len(numbers)):
    numbers[n] = int(numbers[n])


print ("The sum of the numbers you entered is: ", sum(numbers))
print ("The average of the numbers you entered is: ", sum(numbers)/len(numbers))

# Problem 2

print("Problem 2:")

salary = input ("Enter the starting salary: ")
percent = input("Enter the percentage increase: ")
years = input ("Enter the number of years: ")

salary = int(salary)
percent = int(percent) / 100
years = int(years)

year = 1

print (["Year Number:", "Salary:"])

for p in range(years):
    schedule = ["     ", year, "         ", salary]
    salary = salary * (1 + percent)
    salary = round(salary, 2)
    year += 1
    print (*schedule)

# Problem 3

import random
print ("Problem 3: ")

pot = input("How much money do you want to put in the pot?")
pot = int(pot)
maxPot = 0

rolls = 0
while pot != 0:
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    dice = die1 + die2
    if pot > maxPot:
        maxPot = pot
    if dice == 7:
     pot += 4
     rolls += 1
    else:
      pot -= 1
      rolls += 1

print ("No more money in pot. Game Over.")
print ("Number of rolls: ", rolls)
print ("Maximum money that was in the pot: ", maxPot)
