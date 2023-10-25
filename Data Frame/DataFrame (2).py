#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: Nafiseh
"""

# -----------------------------
# Regression, data analysis, and data loading
# -----------------------------
'''import pandas as pd
df1 =pd.read_csv ('payroll-1.txt', sep =' ', header = None)
df2 =pd.read_csv ('payroll-1.txt', sep =' ')
df3 =pd.read_csv ('payroll-1.txt', sep =' ', names = ["Employee", "Salary", "Year", "Gender"])
df4 =pd.read_csv ('payroll-2.txt', sep =' ')

print (df1)
print ('\n',df2)
print ('\n', df3)
print ('\n', df4)'''

# ------------------------------
"""import pandas as pd
x=[]
y=[]
Z=[]
W=[]
ins = open("payroll-1.txt", "r")
for line in ins:
  items = line.split()
  x.append(items[0])
  y.append(items[1])
  Z.append(items[2])
  W.append(items[3])
df = pd.DataFrame({"Employee": x, "Salary": y, "Year": Z, "Gender": W} )
print (df.describe())"""

# ------------------------------
# practice 1
# ------------------------------
'''import pandas as pd
df1 =pd.read_csv ('data.txt', delimiter =',', header =None)
print (df1)
df2 =pd.read_csv ('data.txt', delimiter =',', names = ['A', 'B', 'C'])
print (df2)'''

# -----------------------------
'''import pandas as pd
# Load an Excel file
df = pd.read_excel("information.xlsx",'Sheet1')
print (df)

# Load a csv with no headers
df = pd.read_csv('document.csv', header=None)
print (df)

# Load a csv while specifying column names
df = pd.read_csv('document.csv', names=['UID', 'First Name', 'Last Name']) 
print (df)

# Load a csv with setting the index column to UID
df = pd.read_csv('document.csv', index_col='UID', names=['UID', 'First Name', 'Last Name']) 
print (df)

# Load a csv while setting the index columns to First Name and Last Name
df = pd.read_csv('document.csv', index_col=['First Name', 'Last Name'], names=['UID', 'First Name', 'Last Name'])
print (df)'''

# ------------------------
'''import numpy as np
import pandas as pd
df = pd.DataFrame (np.random.randint (20, 150, (3,2)),columns = ['A', 'B'])
df.to_csv ('mydata.csv')
print (df)'''

# ------------------------
'''import numpy as np
import pandas as pd
df = pd.DataFrame (np.random.randint (20, 150, (3,3)),columns = ['A', 'B', 'C'])
z= df.query ('A>B')   
#z= df[df.A> df.B]
print (df)
print (z)'''

# --------------------------
# Regression
# -------------------------
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
x = np.linspace(1, 7, 50)
y = 3 + 2*x + 1.5*np.random.randn(len(x))
df = pd.DataFrame({'xData':x, 'yData':y})
sns.regplot('xData', 'yData', data=df)
plt.show()

# --------------------------
# import numpy as np 
# import matplotlib.pyplot as plt 
# import pandas as pd 
# import statsmodels.api as sm 
# x = np.linspace(1, 7, 50)
# y = 3 + 2*x + 1.5*np.random.randn(len(x))
# df = pd.DataFrame({'xData':x, 'yData':y})
# model = sm.OLS(y,x).fit()    #OLS: Ordinary least square 
# predictions = model.predict(x) #make the predictions by the model 
# print (model.summary())

# --------------------------

'''import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({'Gender': ['f', 'f', 'm', 'f', 'm','m', 'f', 'm', 'f', 'm', 'm'],\
                      'TV': [3.4, 3.5, 2.6, 4.7, 4.1, 4.1,5.1, 3.9, 3.7, 2.1, 4.3]})

grouped = data.groupby('Gender')
print(grouped.describe())
grouped.boxplot()
plt.show()'''

# ----------------------------------
# practice 2: analyzing grouped data
# ----------------------------------

'''import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
# import statsmodels.api as sm

data = pd.DataFrame({'Gender': ['f', 'f', 'm', 'f', 'm','m', 'f', 'm', 'f', 'm', 'm'],\
                      'TV': [3.4, 3.5, 2.6, 4.7, 4.1, 4.1,5.1, 3.9, 3.7, 2.1, 4.3],\
                          'Race': ['W','W','B','H','W','A','B','H','W','A','W'],\
                              'Age': [20, 25, 17, 14, 14, 16,13, 21, 26, 28, 17]})
# sns.regplot(data['Age'], data['TV'], data=data)
# plt.show() 
grouped = data.groupby('Race')
print(grouped.describe()) 
# grouped.boxplot() 
# plt.show() 
# x=sm.add_constant(data['Age']) #Add an intercept to the regression model
# model = sm.OLS(data['TV'],x).fit() #OLS: Ordinary least square
# predictions = model.predict(x) #make the predictions by the model 
# print (model.summary())'''
















