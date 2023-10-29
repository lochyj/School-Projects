
# --------|
# Imports |
# --------|
from src.constant import *

# -----|
# Code |
# -----|

days = 29

breakdown = []

infected = 7769783

breakdown.append(infected)

for i in range(days):
    infected *= 1 + ALPHA
    
    breakdown.append(infected)
    print(infected)

with open("./out/simple.csv", 'w') as f:
    for val in breakdown:
        print(val, file=f)
