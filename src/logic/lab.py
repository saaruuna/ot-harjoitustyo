import pygame
from components.rat import Rat
from components.wall import Wall
from components.trap import Trap
from components.floor import Floor
from components.cheese import Cheese

SCALE = 20

class Lab:
    """A class describe a Lab object.

    Attributes:
        name: The name of the Lab.
        lab_map: The array of an array of integers which describe the layout of the lab.
        rat: The Rat object.
        floors: The group of Floor objects.
        walls: The group of Wall objects.
        traps: The group of Trap objects.
        cheeses: The group of Cheese objects.
        all_sprites: The group of all pygame sprites.
    """

    def __init__(self, name, lab_map):
        """The class contructor, which creates a new Lab object.

        Args:
            name: The name of the Lab object fetched from the lab database.
            lab_map: The array of arrays of integers which describe the layout of the Lab,
                        fetched from the lab database.
        """

        self.name = name
        self.lab_map = lab_map
        self.rat = None
        self.floors = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.traps = pygame.sprite.Group()
        self.cheeses = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites(lab_map)

    def _initialize_sprites(self, lab_map):
        """The method to read the given map and initialize sprites in the game.

        Args:
            lab_map: The array of arrays of integers which describe the layout of the Lab,
                        fetched from the lab database.
        """

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
        """The method to move the Rat sprite in the game.

        Args:
            x_change: The change in x-position input by the player.
            y_change: The change in y-position input by the player.
        """

        if not self.rat_can_move(x_change, y_change):
            return

        self.rat.rect.move_ip(x_change, y_change)

    def rat_can_move(self, x_change=0, y_change=0):
        """The method to check whether the player's input to move the rat is allowed.

        Args:
            x_change: The change in x-position input by the player.
            y_change: The change in y-position input by the player.

        Returns:
            True, if the input move is allowed i.e. rat is in bounds and not moving through a wall.
            False, if the input move is not allowed i.e. a wall is in the way or the rat is out of
            bounds.
        """

        self.rat.rect.move_ip(x_change, y_change)
        colliding_walls = pygame.sprite.spritecollide(self.rat, self.walls, False)
        out_of_bounds = False

        if (self.rat.rect.x < 0 or self.rat.rect.x >= (len(self.lab_map[0])*SCALE)):
            out_of_bounds = True
        if (self.rat.rect.y < 0 or self.rat.rect.y >= (len(self.lab_map)*SCALE)):
            out_of_bounds = True

        can_move = not colliding_walls and not out_of_bounds
        self.rat.rect.move_ip(-x_change, -y_change)

        return can_move

    def rat_got_cheese(self):
        """The method to check whether the player has won by getting the cheese with the rat.

        Returns:
            True, if the rat has collided with a cheese.
            False, if the rat has not collided with a cheese.
        """

        if pygame.sprite.spritecollide(self.rat, self.cheeses, False):
            return True
        return False

    def rat_hit_trap(self):
        """The method to check whether the player has lost by hitting a trap with the rat.

        Returns:
            True, if the rat has collided with a trap.
            False, if the rat has not collided with a trap.
        """

        if pygame.sprite.spritecollide(self.rat, self.traps, False):
            return True
        return False

    def reset_lab(self):
        """The method to reset a lab to its initial position defined by the lab map.
        """
        self._initialize_sprites(self.lab_map)
