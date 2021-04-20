import pygame
from ui.lab import Lab
from ui.game_loop import GameLoop
from ui.renderer import Renderer
from ui.event_queue import EventQueue
from ui.clock import Clock


LAB_MAP =   [[1, 1, 1, 1, 1],
             [1, 0, 0, 0, 1],
             [1, 3, 2, 4, 1],
             [1, 0, 0, 0, 1],
             [1, 1, 1, 1, 1]]

SCALE = 20


def main():
    display = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("LabRat")

    lab = Lab("DEMO", LAB_MAP, SCALE)
    event_queue = EventQueue()
    renderer = Renderer(display, lab)
    clock = Clock()
    game_loop = GameLoop(lab, renderer, event_queue, clock, SCALE)

    pygame.init()
    game_loop.start()

if __name__ == "__main__":
    main()
