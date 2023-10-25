#Part A
df1 = open('Final Exam - Anthony Rizzuto/Exam file_1.txt', 'r')
mylist = []
for i in df1:
    list = i.split()
    for j in list:
        mylist.append(float(j))
print ("\nProblem Two:\n \nPart A:\n \n Here is the list of numbers: ", mylist)

#Part B
def median_fun (mylist):
    mylist.sort()
    midpoint = len(mylist)
    if midpoint % 2 == 0:
        median1 = mylist[midpoint//2]
        median2 = mylist[midpoint//2-1]
        median = (median1 + median2)/2

    else:
        median = mylist [midpoint//2]
    return median
    
def mean_fun(mylist):
    sum = 0 
    for i in mylist:
        sum += i  
    mean = sum / len(mylist)
    return mean

print ("\nPart B:\n \n The median is: ", median_fun(mylist), "\n The mean is: ", mean_fun(mylist))