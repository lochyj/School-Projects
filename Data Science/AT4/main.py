# A poorly commented attempt at a somewhat realistic covid-19 simulation

# --------|
# Imports |
# --------|
import random

from src.constant import *

# -----|
# Code |
# -----|

days        = 209 # The days between 8/6/2020 and the end of the 2020 year, 31/12/2020
breakdown   = [] # current cases, total infected, population, deaths, recovered. The indexes are defined in constants.py
deltas      = []
infected    = 7769783

INITIAL_INFECTIONS = infected

population  = BEGINNING_POPULATION - INITIAL_INFECTIONS

# -----------------|
# Helper functions |
# -----------------|

def do_infections():
    global infected # God i hate python's scope handling

    # We divide R by 2.2 because it makes the results look good
    infected = int(
        infected * max(1, r_value / 2.2) 
    )

def get_delta(day):
    global infected

    if day == 0:
        return infected - INITIAL_INFECTIONS

    return infected - breakdown[day - 1][CASES]

def do_deaths(day):
    global population
    global infected

    deaths = infected * DEATH_RATE
    population -= deaths

    breakdown[day][DEATH] = deaths

    return deaths

def do_recover(day):
    global deltas
    global infected
    global population

    if len(deltas) >= random.randint(10, 21):
        recovered = deltas.pop(0)

        if recovered <= 0: # Sometimes we have a negative delta...
            return 0

        infected -= recovered
        population += recovered

        breakdown[day][RECOVERED] = recovered

        return recovered

    return 0

def generate_r():
    return random.uniform(1.4, 2.6)

# -------------------|
# Init and Main Loop |
# -------------------|

r_value = generate_r()

for day in range(days):

    breakdown.append([0, 0, 0, 0, 0]) # Initialise the day's data

    do_infections(day)

    # New infection for day "day"
    delta = get_delta(day)

    deaths = do_deaths(day)
    delta -= deaths # Remove the deaths from the delta

    r_value = generate_r()

    recoveries = do_recover(day)

    population -= delta

    if population <= 0:
        delta += population
        infected += population

    deltas.append(delta)

    # Add some data points to the breakdown. (stuff to put on a graph)
    breakdown[day][CASES] = infected
    breakdown[day][POPULATION] = population

    if day != 0:
        breakdown[day][TOTAL] = delta + breakdown[day - 1][TOTAL]
    else:
        breakdown[day][TOTAL] = delta + INITIAL_INFECTIONS


with open("./out/out.csv", 'w') as file:

    print("Current Cases, Total Cases, Non-Infected Population, Deaths, Recoveries", file=file)

    for day in breakdown:

        print(f"{day[CASES]}, {day[TOTAL]}, {day[POPULATION]}, {day[DEATH]}, {day[RECOVERED]}", file=file)