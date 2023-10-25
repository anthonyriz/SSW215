from gurobipy import *

def myFunction(b_one, b_two):
    pottery_co = Model("pottery_co")
    pottery_co.setParam ('OutputFlag', False)

    x = pottery_co.addVar (vtype=GRB.INTEGER, lb = 0, name = 'bowls_no')
    y = pottery_co.addVar (vtype=GRB.INTEGER, lb = 0, name = 'mugs_no')

    pottery_co.addConstr (1 * x + 2 * y <= b_one, name = 'labor constraint')
    pottery_co.addConstr (4 * x + 3 * y <= b_two, name = 'clay constraint')

    Z = 40 * x + 50 * y

    pottery_co.setObjective (Z, GRB.MAXIMIZE)

    pottery_co.optimize()

    pottery_co.printAttr ('X')
    number_of_mugs  = x.X
    number_of_bowls = y.Y
    objective_value = pottery.co.objVal
    return number_of_mugs, number_of_bowls, objective_value

myFunction(40,120)


