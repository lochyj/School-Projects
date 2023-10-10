import random

rabbits = 100
wolves = 10

total_generations = 5000

def gen_rabbits(out):
    global rabbits

    # Breeding
    rabbits *= 1.05

    # Death
    rabbits /= 1.1

    # Eaten
    rabbits -= max(1 , wolves)

    # Randomly joining the generation
    rabbits += random.randint(0, 4)

    # We dont want to go under 1
    rabbits = max(1, rabbits)

    print(f"{rabbits},", file=out, end='')

def gen_wolves(out):
    global wolves

    # Breeding
    wolves *= 1.1 + (rabbits / (rabbits / 1.05)) / 100

    # Deaths
    wolves /= 1.004

    # Deaths due to starvation
    wolves /= 10 / max(1, abs(rabbits))

    # We dont want to go under 1
    wolves = max(1, wolves)

    print(f"{wolves}", file=out)

with open('squares.csv', 'w') as out:

    for i in range(1, total_generations):
        print(f"{i},", file=out, end='')
        gen_rabbits(out)
        gen_wolves(out)

