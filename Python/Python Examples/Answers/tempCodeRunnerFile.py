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