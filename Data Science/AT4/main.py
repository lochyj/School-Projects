
# --------|
# Imports |
# --------|
import random

from src.constant import *

# -----|
# Code |
# -----|

days = 209

breakdown = []

deltas = []

infected = 7769783

breakdown.append(infected)

for i in range(days):
    infected *= 1 + R

    delta = infected - breakdown[i]

    deltas.append(delta)

    if len(deltas) > random.randint(10, 14):
        infected -= deltas.pop(0)

    breakdown.append(infected)
    print([delta, infected])

with open("./out/recovery.csv", 'w') as f:
    for val in breakdown:
        print(val, file=f)
