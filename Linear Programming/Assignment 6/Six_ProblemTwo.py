from gurobipy import *

problem_two = Model ("problem 2")

#Part A
"""
x1: land allocation (in acres) of sugar beet crops in group 1
x2: land allocation (in acres) of sugar beet crops in group 2
x3: land allocation (in acres) of sugar beet crops in group 3
x4: land allocation (in acres) of cotton crops in group 1
x5: land allocation (in acres) of cotton crops in group 2
x6: land allocation (in acres) of cotton crops in group 3
x7: land allocation (in acres) of sorghum crops in group 1
x8: land allocation (in acres) of sorghum crops in group 2
x9: land allocation (in acres) of sorghum crops in group 3
"""

#Part B: Continuous because you can have a fraction (or decmimal) of land. (e.g. one can own a half of acre)
x1  = problem_two.addVar (vtype = GRB.CONTINUOUS, lb = 0, name = "a")
x2  = problem_two.addVar (vtype = GRB.CONTINUOUS, lb = 0, name = "b")
x3  = problem_two.addVar (vtype = GRB.CONTINUOUS, lb = 0, name = "c")
x4  = problem_two.addVar (vtype = GRB.CONTINUOUS, lb = 0, name = "d")
x5  = problem_two.addVar (vtype = GRB.CONTINUOUS, lb = 0, name = "e")
x6  = problem_two.addVar (vtype = GRB.CONTINUOUS, lb = 0, name = "f")
x7  = problem_two.addVar (vtype = GRB.CONTINUOUS, lb = 0, name = "g")
x8  = problem_two.addVar (vtype = GRB.CONTINUOUS, lb = 0, name = "h")
x9  = problem_two.addVar (vtype = GRB.CONTINUOUS, lb = 0, name = "i")


problem_two.addConstr (x1 + x4 + x7 <= 400, name = "Usable Land for group 1")
problem_two.addConstr (x2 + x5 + x8 <= 600, name = "Usable Land for group 2")
problem_two.addConstr (x3 + x6 + x9 <= 300, name = "Usable Land for group 3")
problem_two.addConstr (3*x1 + 2*x4 + x7 <= 600, name = "Water Allocation for group 1")
problem_two.addConstr (3*x2 + 2*x5 + x8 <= 800, name = "Water Allocation for group 2")
problem_two.addConstr (3*x3 + 2*x6 + x9 <= 375, name = "Water Allocation for group 3")
problem_two.addConstr (x1 + x2 + x3 <= 600, name = "Total Acerage of Sugar beets")
problem_two.addConstr (x4 + x5+ x6 <= 500, name = "Total Acerage of Cotton")
problem_two.addConstr (x7 + x8 + x9 <= 325, name = "Total Acerage of Sorghum")

Z = 1000*(x1 + x2 + x3) + 750*(x4 + x5 + x6) + 250*(x7 + x8+ x9)

#Part C

problem_two.setObjective (Z, GRB.MAXIMIZE)

problem_two.optimize()

print ("Optimal Solution is: ", problem_two.objVal)