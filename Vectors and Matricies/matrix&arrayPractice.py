import random
from re import X
import secrets
import numpy as np
import numpy.random
import numpy.linalg as LA

'''print(random.randint(0,9))

print(random.randrange(2,20,2))

print(random.randrange(100,1000,3))

print(random.randrange(-50,-5))

print (random.sample(range(0,1000),10))

print(secrets.randbelow(10))

print(list(np.random.randint(low=1,high=100,size=500)))

x = np.array([0, 0.5, 1, 1.5])

print(x)

y = np.arange(0, 4, 0.5)

print (y)

z  = np.zeros(4)
z[0]  = 3.4
z[2] = 4

print(z)

a = np.eye(3)

print(a)

A = np.random.rand(5,5)
x = np.random.rand(5,1)
b = np.dot (A,x)

print (A)
print (x)
print (b)

D = np.array ([[2, 1, -2], [1, -1, -1], [1, 1, 3]])
F = np.array ([3, 0, 12])
E = LA.solve (D, F)
print (E)'''

#Practice 1
print (np.arange(5, 20, 2))

'''z = np.arange (0,10,1)
print (z)
print (np.cos(z))'''

#Practice random matrix
"""A = np.random.rand(7,5)
print("A: ", A)

B = np.random.rand(5,2)
print ("B: ", B)

C = np.dot (A,B)
print ('C: ', C)"""

#Practice system of equations
'''D = np.array ([[1, 1, -2, 1, 3, -1], [2, -1, 1, 2, 1, -3], [1, 3, -3, -1, 2, 1], [5, 2, -1, -1, 2, 1], [-3, -1, 2, 3, 1, 3], [4, 3, 1, -6, -3, -2]])
E = np.array ([4, 20, -15, -3, 16, -27])
F = LA.solve (D,E)

print (F)'''

