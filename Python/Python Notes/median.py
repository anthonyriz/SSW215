import statistics
list = input("Enter list of numbers: ").split()

median = open("median.txt", 'w')
median.write(str(list))

median.close()

print(statistics.median([list])
