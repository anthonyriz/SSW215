#I pledge my honor that I have abided by the Stevens Honor System. x: Anthony Rizzuto
import numpy as np
import numpy.linalg as LA
import pandas as pd
import matplotlib.pyplot as plt

#Problem 1
'''print ("Problem 1:")
A = np.random.randint(50, 120, size = (3, 5))
B = np.random.randint(10, 60, size = (5, 6))
C = np.dot (A, B)
R = C*10
print ("Matrix A: \n" , A)
print ("Matrix B: \n" , B)
print ("Matrix C:\n " , C)
print ("Matrix R: \n" , R)

#Problem 2
print ("Problem 2:")
D = np.array ([[4, -8, -2, 7], [-4, 1, -9, -4], [-2, -64, -6, 5], [-7, -8, -25, -2]])
E = np.array ([9, -5, 5, 2])
F = LA.solve (D, E)
print (F)'''

#Problem 3
print ("Problem 3:")
df1 = pd.read_csv('/Users/anthonyrizzuto/Library/CloudStorage/OneDrive-stevens.edu/Term 3/SSW 215/Data Frame/salary.txt', sep = ' ', names = ["Employee", "Salary", "Year", "Gender"])
print (df1)
print (df1.iloc[:,0:2])
grouped = df1.groupby('Gender')
print (grouped.describe())
df1.plot.scatter(x='Year', y='Salary')
plt.show()

