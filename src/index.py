import pygame
from lab import Lab

LAB_MAP =   [[1, 1, 1, 1, 1],
             [1, 0, 0, 0, 1],
             [1, 3, 2, 4, 1],
             [1, 1, 1, 1, 1]]

CELL_SIZE = 50


def main():
    height = len(LAB_MAP)
    width = len(LAB_MAP[0])
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE

    # alustetaan ikkuna
    display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("LabRat")

    lab = Lab(LAB_MAP, CELL_SIZE)

    # alustetaan Pygamen moduulit
    pygame.init()

    # piirretään all_sprites ryhmän spritet ikkunaan
    lab.all_sprites.draw(display)

if __name__ == "__main__":
    main()
