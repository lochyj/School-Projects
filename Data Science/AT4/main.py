
# --------|
# Imports |
# --------|
import random

from src.constant import *

# -----|
# Code |
# -----|

days = 1009

breakdown = []

deltas = [12, 53, 74, 32, 75, 25, 82, 53]

infected = 7769783
#infected = 1000

r_value = random.uniform(1.4, 2.6)

breakdown.append(infected)

total = [infected]

for i in range(days):

    infected = int(infected * max(1, r_value / 2.2)) # This is half of the average time to infection, 4.2 is the actual value but it was too high...

    delta = infected - breakdown[i]

    r_value = random.uniform(1.4, 2.6)

    total.append(total[i] + delta)

    deltas.append(delta)

    if len(deltas) >= random.randint(10, 21):
        infected -= deltas.pop(0)

    breakdown.append(infected)
    print([delta, infected])

with open("./out/recovery.csv", 'w') as f:
    for i in breakdown:
        print(i, file=f)

with open("./out/extended_recovery.csv", 'w') as f:
    for i in total:
        print(i, file=f)
