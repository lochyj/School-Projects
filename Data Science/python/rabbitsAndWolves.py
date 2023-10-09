rabbits = 100
rabbit_birth = 1.1
rabbit_death = 0.05

rabbit_max = 1000

wolves = 20
wolf_birth = 1.1
wolf_death = 0.05

wolf_kill = 0.9 # / wolf

total_generations = 51

for i in range(1, total_generations):
    print() # \n
    # Wolves
    Nwolf_birth = wolf_birth * rabbits / wolves
    dead_wolf = wolf_death * wolves
    wolves = int(wolves * Nwolf_birth - dead_wolf)
    print(f"wolves: {i}:{wolves}")

    eaten_rabbit = wolves * wolf_kill

    # Rabbits
    Nrabbit_birth = rabbit_birth * (1 - rabbits / rabbit_max)
    dead_rabbit = rabbit_death * rabbits + eaten_rabbit
    rabbits = int(rabbits * Nrabbit_birth - dead_rabbit)
    print(f"rabbits: {i}:{rabbits}")
