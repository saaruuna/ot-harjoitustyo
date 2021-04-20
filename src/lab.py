import pygame
from rat import Rat
from wall import Wall
from trap import Trap
from floor import Floor
from cheese import Cheese

class Lab:
    def __init__(self, name, lab_map, cell_size):
        self.name = name
        self.lab_map = lab_map
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

        for y_position in range(height):
            for x_position in range(width):
                cell = lab_map[y_position][x_position]
                normalized_x = x_position * self.cell_size
                normalized_y = y_position * self.cell_size

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
        if not self._rat_can_move(x_change, y_change):
            return

        self.rat.rect.move_ip(x_change, y_change)

    def _rat_can_move(self, x_change=0, y_change=0):
        self.rat.rect.move_ip(x_change, y_change)
        colliding_walls = pygame.sprite.spritecollide(self.rat, self.walls, False)
        can_move = not colliding_walls
        self.rat.rect.move_ip(-x_change, -y_change)

        return can_move

    def rat_got_cheese(self):
        if pygame.sprite.spritecollide(self.rat, self.cheeses, False):
            self.rat.is_happy = True
            self.rat.update()
            return True
        return False

    def rat_hit_trap(self):
        if pygame.sprite.spritecollide(self.rat, self.traps, False):
            self.rat.is_dead = True
            self.rat.update()
            return True
        return False
