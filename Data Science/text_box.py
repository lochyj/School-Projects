import pygame

from constants import *

font_32 = pygame.font.Font('freesansbold.ttf', 32)
font_24 = pygame.font.Font('freesansbold.ttf', 24)
font_12 = pygame.font.Font('freesansbold.ttf', 12)

class textBox:
    def __init__(self, x_position: int, y_position: int, width: int, height: int, font_size: int):  # Font size ∈ {32, 24, 12}
        self.position = (x_position, y_position)
        self.size = (width, height)
        self.colour = WHITE
        self.contents = ""
        match font_size:
            case 32:
                self.font = font_32
            case 24:
                self.font = font_24
            case 12:
                self.font = font_12
            case _: # Possibly make this other
                print(f"[ ERROR ] Font size of {font_size} is unknown, supply either 32, 24 or 12.\nThe font will default to 24px.")
                self.font = font_24

        self.text = self.font(self.contents, ANTIALIAS, BLACK)
        self.selected = False
        self.surface =
        self.rect = pygame.Rect(x_position, y_position, width, height)

    def redraw_self(self):
        ...
    def draw_to_surface(self, surface):
        surface.blit(self.text, (self.surface.x, self.surface.y))

    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            ...

class Matrix:
    def __init__(self, width, height, x, y, elements: list[list[]]):
        ...