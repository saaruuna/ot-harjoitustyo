import pygame
from components.rat import Rat
from components.wall import Wall
from components.trap import Trap
from components.floor import Floor
from components.cheese import Cheese

SCALE = 20

class Lab:
    def __init__(self, name, lab_map):
        self.name = name
        self.lab_map = lab_map
        self.rat = None
        self.floors = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.traps = pygame.sprite.Group()
        self.cheeses = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self.initialize_sprites(lab_map)

    def initialize_sprites(self, lab_map):
        height = len(lab_map)
        width = len(lab_map[0])

        for y_position in range(height):
            for x_position in range(width):
                cell = lab_map[y_position][x_position]
                normalized_x = x_position * SCALE
                normalized_y = y_position * SCALE

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

    def move_rat(self, x_change=0, y_change=0):
        if not self.rat_can_move(x_change, y_change):
            return

        self.rat.rect.move_ip(x_change, y_change)

    def rat_can_move(self, x_change=0, y_change=0):
        self.rat.rect.move_ip(x_change, y_change)
        colliding_walls = pygame.sprite.spritecollide(self.rat, self.walls, False)
        can_move = not colliding_walls
        self.rat.rect.move_ip(-x_change, -y_change)

        return can_move

    def rat_got_cheese(self):
        if pygame.sprite.spritecollide(self.rat, self.cheeses, False):
            return True
        return False

    def rat_hit_trap(self):
        if pygame.sprite.spritecollide(self.rat, self.traps, False):
            return True
        return False

    def reset_lab(self):
        self.initialize_sprites(self.lab_map)
