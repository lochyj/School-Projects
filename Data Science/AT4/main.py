
# --------|
# Imports |
# --------|
import random

from src.constant import *

# -----|
# Code |
# -----|

days = 2009 # 209, 29

breakdown = [] # current cases, total infected, population, deaths, recovered

deltas = [12, 53, 74, 32, 75, 25, 82, 53]

infected = 7769783
#infected = 1000

population = POPULATION - infected

r_value = random.uniform(1.4, 2.6)

breakdown.append(infected)

total = [infected]

for i in range(days):

    # New infections
    infected = int(infected * max(1, r_value / 2.2)) # This is half of the average time to infection, 4.2 is the actual value but it was too high...

    # New infections on the day "i"
    delta = infected - breakdown[i]

    population -= delta

    # Deaths handling
    deaths = int(delta * DEATH_RATE)
    delta -= deaths
    infected -= deaths

    r_value = random.uniform(1.4, 2.6)

    total.append(total[i] + delta)

    deltas.append(delta)

    if len(deltas) >= random.randint(10, 21):
        recovered = deltas.pop(0)
        infected -= recovered
        population += recovered

    breakdown.append(infected)
    print([delta, infected])

with open("./out/recovery.csv", 'w') as f:
    for i in breakdown:
        print(i, file=f)

with open("./out/extended_recovery.csv", 'w') as f:
    for i in total:
        print(i, file=f)
