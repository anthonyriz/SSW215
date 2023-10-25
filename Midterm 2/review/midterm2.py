#I pledge my honor that I have abided by the Stevens Honor System. xAnthony Rizzuto

#Problem 1

myList = input ("Enter integer numbers to place into a list:").split()
def del_element (q):
  t = list(dict.fromkeys(q)) 
  return t
print ("Problem 1 \n", del_element(myList))

#Problem 2

list_one = []
list_two = [1]

def prime_check (p, n):
    for number in range (1, 51):
        i = 0
        for j in range(2, (number//2 + 1)):
            if(number % j == 0):
                i =+1 
                n.append(number)
                break
        if (i == 0 and number != 1):
            p.append(number)
    return p, n
print ("Problem 2: \n", prime_check(list_one, list_two))


#Problem 3

import numpy as np
print ("Problem 3:")
X = np.zeros(18)
X[3] = 10
X[9] = 25
X[13] = 12
X[15] = 30
print ("Matrix X: \n" ,X)

Y = np.cos(X)
print ("Matrix Y: \n", Y)

Z = np.random.randint(80, 200, size = (5, 8))
G = np.random.randint(50, 180, size = (8, 6))
F = np.dot (Z, G)
print ("Matrix Z: \n" , Z)
print ("Matrix G: \n" , G)
print ("Matrix F:\n " , F)

#Problem 4

import numpy as np
import numpy.linalg as LA

A = np.array ([[2, 2, -1, 1], [4, 3, -1, 2], [8, 5, -3, 4], [3, 3, -2, 2]])
B = np.array ([4, 6, 12, 6])
C = LA.solve (A,B)
print ("Problem 4: \n", C)

