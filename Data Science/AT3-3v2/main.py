# ---------|
# Includes |
# ---------|

# ---------
# 3rd Party
# ---------

import random

# ---------
# Home made
# ---------

from lib.graph import Graph

from src.solver import SP_Djikstras
from src.generator import prims_maze_generator

# -----|
# Init |
# -----|


test = Graph()

test.generate_graph(5)

test.connect(0, 1)
test.connect(1, 2)
test.connect(2, 3)
test.connect(3, 4)

print(SP_Djikstras(test, 0, 4))
