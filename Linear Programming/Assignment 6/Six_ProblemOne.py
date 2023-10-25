from gurobipy import *

problem_one = Model ("problem_one")

x  = problem_one.addVar (vtype = GRB.INTEGER, lb = 0, name = "x1")
y = problem_one.addVar (vtype  = GRB.INTEGER, lb = 0, name = "x2")

problem_one.addConstr (x + 2 * y >= 10, name = "constraint_1")
problem_one.addConstr (2 * x - 3 * y <= 6, name ="constraint_2")
problem_one.addConstr (x + y >= 6, name = "constraint_3")

Z = 15 * x + 20 * y

problem_one.setObjective (Z, GRB.MAXIMIZE)

problem_one.optimize()

#Part A
print ("Optimal Value is: ", problem_one.objVal)

#Part B
problem_one.printAttr('X')
print ("x1 = ", x.X)    
print ("x2 = ", y.X)