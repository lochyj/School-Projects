import random
import pygame
from time import sleep

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (255, 100, 110)

MAX_RADIUS = 10
NUMBER_OF_PARTICLES = 20

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
        self.velocity: list[int, int] = (0.1, 0.1)
        self.radius: int = self.get_random_radius()
        self.renderer = renderer
        self.color = LIGHT_BLUE # May or may not actually not be light blue...

    def get_random_pos(self) -> tuple[int, int]:
        return (
            random.randrange(0, WINDOW_WIDTH, RANDOM_PRECISION),
            random.randrange(0, WINDOW_HEIGHT, RANDOM_PRECISION)
        )

    def get_random_radius(self) -> int:
        return random.randrange(0, MAX_RADIUS, RANDOM_PRECISION)

    def draw(self) -> None:
        pygame.draw.circle(self.renderer, self.color, self.pos, self.radius, 0)

    def move(self) -> None:
        self.pos[0] = self.velocity[0]
        self.pos[1] = self.velocity[1]

        self.velocity[0] *= 0.9
        self.velocity[1] *= 0.9

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

                if (pos2[0]-pos1[0])^2 + (pos2[1]-pos1[1])^2 <= (p1.radius+p2.radius)^2:
                    print("E")

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
