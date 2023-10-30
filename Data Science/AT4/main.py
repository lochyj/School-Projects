
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

r_value = random.uniform(1.4, 2.4)

breakdown.append(infected)

for i in range(days):

    infected = infected * r_value / 2.2

    delta = infected - breakdown[i]

    r_value = random.uniform(1.4, 2.4)

    deltas.append(delta)

    if len(deltas) >= random.randint(10, 21):
        infected -= deltas.pop(0)

    breakdown.append(infected)
    print([delta, infected])

with open("./out/recovery.csv", 'w') as f:
    for val in breakdown:
        print(val, file=f)
