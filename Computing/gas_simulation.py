import random
import pygame
import math
from time import sleep

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (255, 100, 110)

MAX_RADIUS = 10
MIN_RADIUS = 2
NUMBER_OF_PARTICLES = 100

RANDOM_PRECISION = 1

pygame.init()

def initialise_window() -> None:

    pygame.display.set_caption("Gas Simulation")

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    window.fill(BLACK)

    return window

class Particle:
    def __init__(self, renderer):
        self.pos: list[int] = self.get_random_pos()
        self.velocity: list[ int] = self.get_random_velocity()
        self.radius: int = self.get_random_radius()
        self.renderer = renderer
        self.color = LIGHT_BLUE # May or may not actually not be light blue...

    def get_random_velocity(self) -> list[float, float]:
        return [
            (random.random() - 0.5) * 20,
            (random.random() - 0.5) * 20
        ]

    def get_random_pos(self) -> list[int]:
        return [
            random.randrange(0, WINDOW_WIDTH, RANDOM_PRECISION),
            random.randrange(0, WINDOW_HEIGHT, RANDOM_PRECISION)
        ]

    def get_random_radius(self) -> int:
        return random.randrange(MIN_RADIUS, MAX_RADIUS, RANDOM_PRECISION)

    def draw(self) -> None:
        pygame.draw.circle(self.renderer, self.color, self.pos, self.radius, 0)

    def move(self) -> None:
        self.pos[0] += math.floor(self.velocity[0])
        self.pos[1] += math.floor(self.velocity[1])

        # Wall bounds:
        if (self.pos[0] < self.radius):
            self.pos[0] = self.radius
            self.velocity[0] = -self.velocity[0]

        elif (self.pos[0] > WINDOW_WIDTH - self.radius):
            self.pos[0] = WINDOW_WIDTH - self.radius
            self.velocity[0] = -self.velocity[0]

        if (self.pos[1] < 0):
            self.pos[1] = self.radius
            self.velocity[1] = -self.velocity[1]

        elif (self.pos[1] > WINDOW_HEIGHT):
            self.pos[1] = WINDOW_HEIGHT - self.radius
            self.velocity[1] = -self.velocity[1]


class Simulation:
    def __init__(self, renderer) -> None:
        self.renderer = renderer
        self.particles: list[Particle] = [Particle(self.renderer) for i in range(NUMBER_OF_PARTICLES)]

    def update(self):

        for particle in self.particles:
            particle.move()

        # O(n^2) collision detection algorithm
        for p1 in self.particles:
            for p2 in self.particles:
                if p1 == p2:
                    continue

                pos1 = p1.pos
                pos2 = p2.pos

                v = [pos1[0] - pos2[0], pos1[1] - pos2[1]]

                dist_raw = abs(v[0] * v[0] + v[1] * v[1])
                min_dist = p1.radius + p2.radius

                if (dist_raw < min_dist * min_dist):
                    dist = math.sqrt(dist_raw) if math.sqrt(dist_raw) != 0 else 0.0001

                    n = [v[0] / dist, v[1] / dist]
                    mr1 = p1.radius / (p1.radius + p2.radius) # Mass ratio 1
                    mr2 = p1.radius / (p1.radius + p2.radius) # Mass ratio 2
                    delta = (dist - min_dist)

                    p1.pos[0] -= n[0] * (mr2 * delta)
                    p1.pos[1] -= n[1] * (mr2 * delta)
                    p1.velocity[0] -= n[0] * (mr2 * delta)
                    p1.velocity[1] -= n[1] * (mr2 * delta)

                    p2.pos[0] += n[0] * (mr1 * delta)
                    p2.pos[1] += n[1] * (mr1 * delta)
                    p2.velocity[0] += n[0] * (mr1 * delta)
                    p2.velocity[1] += n[1] * (mr1 * delta)

    def draw_all(self):
        for particle in self.particles:
            particle.draw()

def main():

    window = initialise_window()

    sim = Simulation(window)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        sim.update()
        sim.draw_all()

        pygame.display.update()
        window.fill(BLACK)

        # This is here to give the cpu a break :)
        sleep(0.01)

if __name__ == "__main__":
    main()
