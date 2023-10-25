# -*- coding: utf-8 -*-
"""


@author: Nafiseh
"""
# Array and matrix
# ----------------------------

import numpy as np
# -----------------------------
x = np.array ([0 , 0.5 , 1, 1.5])
print (x)

x = np.arange (0, 4, 0.5)
print (x)

x = np.zeros (4)
print (x)

x = np.zeros (4)
x [0] = 3.4
x [2] = 4
print (x)
print ("\n")

x = np.eye (3)
print ("\n", x)
# ---------------------------
x = np.arange (0, 3, 0.5)
print (x)
print (x + 10)
print (x ** 2)
print (np.sin (x))
print ("\n")

# --------------------------
x = np.array ([[1 , 2, 3], [4, 5, 6]])
print (x)
x = np.zeros ((5 , 4))
print (x)
print (x.shape)
print ("\n")

# --------------------------
x=np.array ([[1 , 2, 3], [4, 5, 6]])
print (x)
print (x[0, 0])	
print (x[0, 1])		
print (x[0, 2])		
print (x[1, 0])	
print (x[:, 0])		
print (x[0 ,:])	
print ("\n")

# -------------------------
import numpy as np
import numpy.random
A = np.random.rand (5, 5)
print (A) 
x = np.random.rand (5,1) 
print ("\n",x)
b = np.dot (A, x)
print ("\n", b)

# -------------------------
import numpy.linalg as LA
import numpy as np
D = np.array ([[2,1,-2], [1,-1,-1], [1,1,3]])
F = np.array ([3,0,12])
E = LA.solve (D,F)
print ("\n", E)

# ------------------------
import numpy
import numpy.linalg as LA
A = np.eye (3) 
print ("\n",A)
e_values , e_vectors = LA.eig (A)
print (e_values, e_vectors)

import numpy
import numpy.random
import numpy.linalg as LA
A = numpy.random.rand (3,3)
print ("\n",A)
e_values,e_vectors= LA.eig (A)
print (e_values, e_vectors)















