import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('Final Exam - Anthony Rizzuto/Exam file_2-2.csv', names = ["Customer ID", "Gender", "Age", "Annual Income", "Spending Score"])
print("\nProblem 4: \n\n", df1)

#Part A
df2 = pd.read_csv('Final Exam - Anthony Rizzuto/Exam file_2-2.csv', names = ["Customer ID", "Gender", "Age", "Annual Income", "Spending Score"], index_col = "Spending Score")
sorted_df2 = df2.sort_values(by= "Spending Score")
print ("\nPart A:\n" , sorted_df2)

#Part B
print ("\nPart B: \n" , df1.loc[:, ["Gender", "Annual Income"]])

#Part C
grouped = df1.groupby('Gender')
print ("\nPart C: \n" , grouped.describe())

#Part D
df1.plot.scatter(x='Annual Income', y='Age')
plt.show()



#I pledge my honor that I have abided by the Stevens Honor System. x: Anthony Rizzuto