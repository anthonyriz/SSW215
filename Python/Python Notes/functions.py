from tkinter import N, Y


def square_1(x):
    y = x*x
    return y
print (square_1(7))


mylist = [4, 3, 3, 12]
def average(mylist):
    theSum = 0
    for i in mylist:
        theSum += i
        Ave = theSum / float(len(mylist))
    return Ave

print(average(mylist)) """

"""def main():
    number = int(input("Enter a number: "))
    result = square_2(number)
    print ("The square of", number, "is", result)

def square_2(x):
    return x*x

main()"""

"""def displayRange (lower, upper):
    if lower <= upper:
        print(lower)
        displayRange (lower + 1, upper)
displayRange(2,5)"""

'''def summation(lower, upper):
    if lower > upper:
        return 0
    else:
        return lower + summation(lower+1, upper)
print (summation(4,9))'''


'''n =  input("Enter number you want factorial of:")
def fact(n):
    if n==1:
        return n
    else:
        return n * fact(n-1)

print (fact(n))'''


