#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: Nafiseh
"""



# assignment model

# Define the model parameters 


# List containing officials
official_p = ['A', 'B', 'C', 'D'] 


# List containing game sites    
game_p = ['Raleigh', 'Atlanta', 'Durham', 'Clemson']  


  

# Dictionary containing distance information from every official to each game site
distance_t = {
    (official_p[0], game_p[0]): 210,
    (official_p[0], game_p[1]): 90,
    (official_p[0], game_p[2]): 180,
    (official_p[0], game_p[3]): 160,
    (official_p[1], game_p[0]): 100,
    (official_p[1], game_p[1]): 70,
    (official_p[1], game_p[2]): 130,
    (official_p[1], game_p[3]): 200,
    (official_p[2], game_p[0]): 175,
    (official_p[2], game_p[1]): 105,
    (official_p[2], game_p[2]): 140,
    (official_p[2], game_p[3]): 170,
    (official_p[3], game_p[0]): 80,
    (official_p[3], game_p[1]): 65,
    (official_p[3], game_p[2]): 105,
    (official_p[3], game_p[3]): 120
    }

print ("officials", official_p )
print ("game sites", game_p )


print ("distance", distance_t)

# Import gurobi
from gurobipy import *


# Create the model as an object
model = Model ("assignment")

# Mute the Gurobi
# model.setParam ('OutputFlag', False)


# Create the decison variables for each link from every official to every game site
X = model.addVars(official_p, game_p, vtype=GRB.BINARY, name="x")


# Supply constraints (each official should be assigned to each game site)
# Supply of each official is limited to one unit
for i in official_p:
    model.addConstr(quicksum(X[i,j] for j in game_p) == 1)

# Demand constraints (each game site sould be assignmed to each official)
# Demand of ecah game site is limited to one unit
for j in game_p:
    model.addConstr(quicksum(X[i,j] for i in official_p) == 1)

# Define the objective function
Z = quicksum(X[i,j] * distance_t[i,j] for i in official_p for j in game_p)

# Specify the type of the model: minimization or maximization
model.setObjective (Z, GRB.MINIMIZE)

# Update the model
model.update()

# Solve the model    
model.optimize()     
        
# Print out the optimal solutions: the decion variables values
model.printAttr ('x') 

# Print out the outputs
if model.status==GRB.OPTIMAL:
    print ("-----------------------------------------")
    print ("Optimal value:",model.objVal, "miles")
    print ("-----------------------------------------")
    print ("--- assignmnet (official to game site) ---")
    for i in official_p: 
        for j in game_p:
            print ("official",i, "is assigned to game site", j, X[i,j].X)
    