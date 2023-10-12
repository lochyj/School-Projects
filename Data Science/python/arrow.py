arrow = [52, 39] # Vec of initial arrow velocity

arrow_pos = [0, 1.5] # In m

gravity = 9.8 # m/s/s

steps = 100 # In seconds

for step in range(steps):
    print(step, *arrow_pos)

    arrow_pos[0] += arrow[0] # * 1 second
    arrow_pos[1] += arrow[1] # * 1 second

    arrow[1] -= gravity