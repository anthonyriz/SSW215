from gurobipy import *


furniture_co = Model ("furniture_co")

x = furniture_co.addVar (vtype = GRB.INTEGER, lb = 0, name = "table_number")
y = furniture_co.addVar (vtype = GRB.INTEGER, lb = 0, name = "chair_number")

furniture_co.addConstr (5*x + 2*y <= 150, name = "constraint1")
furniture_co.addConstr (2*x + 3*y <= 100, name = "constraint2")
furniture_co.addConstr (4*x + 2*y <= 80, name = "constraint3")

Z = 12 * x + 8 * y

furniture_co.setObjective (Z, GRB.MAXIMIZE)

furniture_co.optimize()

if furniture_co.status == GRB.OPTIMAL:
    print ("Optimal Value is: ", furniture_co.objVal)

furniture_co.printAttr('X')
print ("Batch of tables: ", x.X)    
print ("Batch of chairs: ", y.X)