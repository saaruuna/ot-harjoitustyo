import pygame
from rat import Rat
from wall import Wall
from trap import Trap
from floor import Floor
from cheese import Cheese

class Lab:
    def __init__(self, lab_map, cell_size):
        self.cell_size = cell_size
        self.rat = None
        self.floors = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.traps = pygame.sprite.Group()
        self.cheeses = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites(lab_map)

    def _initialize_sprites(self, lab_map):
        height = len(lab_map)
        width = len(lab_map[0])

        for y in range(height):
            for x in range(width):
                cell = lab_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                    self.floors.add(Floor(normalized_x, normalized_y))
                elif cell == 1:
                    self.walls.add(Wall(normalized_x, normalized_y))
                elif cell == 2:
                    self.traps.add(Trap(normalized_x, normalized_y))
                elif cell == 3:
                    self.cheeses.add(Cheese(normalized_x, normalized_y))
                elif cell == 4:
                    self.rat = Rat(normalized_x, normalized_y)
                    self.floors.add(Floor(normalized_x, normalized_y))

        self.all_sprites.add(
            self.floors,
            self.walls,
            self.traps,
            self.cheeses,
            self.rat
        )
