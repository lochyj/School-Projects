import random

ALPHA = 0.0172019

TOTAL = 0
UNINFECTED = 1
INFECTED = 2

class Actor:

    infected = False
    infected_time = 0
    infection_duration = 0

    socialization_rate = 20 # The default socialization rate.

    interactions = [0, 0, 0]
    
    def __init__(self, socialization_rate):
        self.socialization_rate = socialization_rate

    def infect(self):
        self.infected = True
        self.infection_duration = random.randint(7, 14)

    def tick(self):
        if self.infected:
            self.infected_time += 1
        
        if self.infected_time >= self.infection_duration:
            self.infected = False
            self.infected_time = 0
            self.infection_duration = 0
    
    def socialize(self, actor):
        if actor.is_infected():
            if random.random() < ALPHA:
                self.infect()
            else:
                self.interactions[INFECTED] += 1
        else:
            self.interactions[UNINFECTED] += 1

        self.interactions[TOTAL] += 1
    
    def is_infected(self):
        return self.infected

    def get_sociality(self):
        return self.socialization_rate
    
    def get_interactions(self):
        return self.interactions
