from gurobipy import *

problem_three = Model ("problem 3")

#Part A
"""
xAR: Officals Team A to Raleigh
xAA: Officals Team A to Atlanta
xAD: Officals Team A to Durham
xAC: Officals Team A to Clemson
xBR: Officals Team B to Raleigh
xBA: Officals Team B to Atlanta
xBD: Officals Team B to Durham
xBC: Officals Team B to Clemson
xCR: Officals Team C to Raleigh
xCA: Officals Team C to Atlanta
xCD: Officals Team C to Durham
xCC: Officals Team C to Clemson
xDR: Officals Team D to Raleigh
xDA: Officals Team D to Atlanta
xDD: Officals Team D to Durham
xDC: Officals Team D to Clemson
"""
#Part B: Binary because the assignment says there can only be one team of officals for every game, 
# therefore there can either be zero teams of officals or one

xAR  = problem_three.addVar (vtype = GRB.BINARY, lb = 0, name = "AR") 
xAA  = problem_three.addVar (vtype = GRB.BINARY, lb = 0, name = "AA")
xAD  = problem_three.addVar (vtype = GRB.BINARY, lb = 0, name = "AD")
xAC  = problem_three.addVar (vtype = GRB.BINARY, lb = 0, name = "AC")
xBR  = problem_three.addVar (vtype = GRB.BINARY, lb = 0, name = "BR")
xBA  = problem_three.addVar (vtype = GRB.BINARY, lb = 0, name = "BA")
xBD  = problem_three.addVar (vtype = GRB.BINARY, lb = 0, name = "BD")
xBC  = problem_three.addVar (vtype = GRB.BINARY, lb = 0, name = "BC")
xCR  = problem_three.addVar (vtype = GRB.BINARY, lb = 0, name = "CR")
xCA  = problem_three.addVar (vtype = GRB.BINARY, lb = 0, name = "CA")
xCD  = problem_three.addVar (vtype = GRB.BINARY, lb = 0, name = "CD")
xCC  = problem_three.addVar (vtype = GRB.BINARY, lb = 0, name = "CC")
xDR  = problem_three.addVar (vtype = GRB.BINARY, lb = 0, name = "DR")
xDA  = problem_three.addVar (vtype = GRB.BINARY, lb = 0, name = "DA")
xDD  = problem_three.addVar (vtype = GRB.BINARY, lb = 0, name = "DD")
xDC  = problem_three.addVar (vtype = GRB.BINARY, lb = 0, name = "DC")

problem_three.addConstr (xAR + xAA + xAD + xAC == 1, name = "Group A")
problem_three.addConstr (xBR + xBA + xBD + xBC == 1, name = "Group B")
problem_three.addConstr (xCR + xCA + xCD + xCC == 1, name = "Group C")
problem_three.addConstr (xDR + xDA + xDD + xDC == 1, name = "Group D")
problem_three.addConstr (xAR + xBR + xCR + xDR == 1, name = "Galeigh")
problem_three.addConstr (xAA + xBA + xCA + xDA == 1, name = "Atlanta")
problem_three.addConstr (xAD + xBD + xCD + xDD == 1, name = "Durham")
problem_three.addConstr (xAC + xBC + xCC + xDC == 1, name = "Clemson")

Z = 210*xAR + 90*xAA + 180*xAD + 160*xAC + 100*xBR + 70*xBA + 130*xBD + 200*xBC + 175*xCR + 105*xCA + 140*xCD + 170*xCC + 80*xDR + 65*xDA + 105*xDD + 120*xDC

#Part C

problem_three.setObjective (Z, GRB.MINIMIZE)

problem_three.optimize()

print ("Optimal Assignment of Teams of Officals to Games:")
print(problem_three.printAttr('X'))

#Part D

print ("Total Miles Traveled by All 4 Teams: ", problem_three.objVal)