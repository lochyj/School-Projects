
# An unnecessarily complex file for simulating the simple covid cases

# Maybe next time just make this part of the assessment a S/N and not 4 full marks

# --------|
# Imports |
# --------|
from io import TextIOWrapper

# The global constants file also used by the advanced implementation
from src.constant import *

# ----------------|
# Data structures | The python way :)
# ----------------|

# Yes, I know about dataclasses, they don't really 
# fit this situation where we have hidden data. (case_breakdown)

class World:
    current_cases: int
    case_breakdown: list[int]

    def __init__(self, initial_cases):
        self.current_cases = initial_cases
        self.case_breakdown = []

        self.case_breakdown.append(self.current_cases)

    def add_cases(self, new_cases):
        self.current_cases = new_cases

        print(new_cases)

        self.case_breakdown.append(self.current_cases)

    def get_current_cases(self):
        return self.current_cases

    def get_case_breakdown(self):
        return self.case_breakdown

# -----------------|
# Helper functions |
# -----------------|

def simulate_day(world: World):
    infected: int = world.get_current_cases()
    new_infections: int = int(infected * (1 + ALPHA)) # We dont want 1.0000000000001 cases...

    world.add_cases(new_infections)

def export_case_breakdown(world: World, file: TextIOWrapper):

    for val in world.get_case_breakdown():
        
        print(val, file=file) # This is the best thing about python ngl
    
# ----------|
# Main loop |
# ----------|

days        = 206
infected    = 7769783

world       = World(initial_cases=infected)

for _ in range(days):
    simulate_day(world=world)

with open("./out/simple.csv", 'w') as file:
    export_case_breakdown(world=world, file=file)