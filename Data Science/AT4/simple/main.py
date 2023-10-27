import random

from lib.Actor import Actor

population = 1000
infected = 5

days = 10

actors: list[Actor] = [Actor(random.randint(10, 30)) for _ in range(population)]

for i in range(infected):
    actors[i].infect()

random.shuffle(actors)

for _ in range(days):

    for actor in actors:
        actor.tick()

    for actor in actors:
        interactions = actor.get_sociality()

        for i in range(interactions):
            interaction = actors[i]
            if actor == interaction:
                continue
            
            actor.socialize(interaction)
            interaction.socialize(actor)
    
    infected = 0
    for actor in actors:
        if actor.is_infected():
            infected += 1
