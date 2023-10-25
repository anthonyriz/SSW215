print ("\nProblem Three: \n")

variable = int(input ("Enter a number: "))

term1 = 0
term2 = 1
i = 0

while term1 <= variable:
    if term1 == variable:
        print('True')
        break
    i = term1
    term1 = term2
    term2 = i + term2
else: 
    print ("False")

