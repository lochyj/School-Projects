arrow = [52, 39] # Vec of initial arrow velocity

arrow_pos = [0, 1.5] # In m

gravity = 9.8 # m/s/s

air_resistance = 1.45

steps = 100 # In seconds

step = 0.0001

print(*arrow_pos)

while arrow_pos[1] >= 0:

    arrow_pos[0] += arrow[0] * step
    arrow_pos[1] += arrow[1] * step

    arrow[0] -= air_resistance if arrow[0] > 0 else (-air_resistance)
    arrow[1] -= air_resistance if arrow[1] > 0 else (-air_resistance)

    arrow[1] -= gravity

    print(*arrow_pos)