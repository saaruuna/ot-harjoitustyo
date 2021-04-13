import pygame
from lab import Lab
from game_loop import GameLoop
from event_queue import EventQueue
from renderer import Renderer
from clock import Clock

LAB_MAP =   [[1, 1, 1, 1, 1],
             [1, 0, 0, 0, 1],
             [1, 3, 2, 4, 1],
             [1, 1, 1, 1, 1]]

CELL_SIZE = 25


def main():
    height = len(LAB_MAP)
    width = len(LAB_MAP[0])
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE

    # alustetaan ikkuna
    display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("LabRat")

    lab = Lab(LAB_MAP, CELL_SIZE)
    event_queue = EventQueue()
    renderer = Renderer(display, lab)
    clock = Clock()
    game_loop = GameLoop(lab, renderer, event_queue, clock, CELL_SIZE)

    # alustetaan Pygamen moduulit
    pygame.init()
    game_loop.start()

if __name__ == "__main__":
    main()
