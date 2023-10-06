import random

unpecked = []
iters = 3000

for _ in range(iters):

    chicks = [0 for i in range(100)]

    for i in range(100):
        l_r = random.choice([-1, 1])

        if i + l_r > 99:
            i = i - 100
        elif i + l_r < 0:
            i = i + 100

        chicks[i + l_r] = 1

    up = 0

    for chick in chicks:
        if chick == 0:
            up += 1

    unpecked.append(up)

total_up = 0

for i in unpecked:
    total_up += i

average = (total_up / 100) / len(unpecked) * 100

print(f"Average pecked over {iters} iterations: {average}%")
