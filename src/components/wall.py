import pygame
from load_image import load_image

class Wall(pygame.sprite.Sprite):
    """A class which creates a wall to display in the game.

    Attributes:
        image: The image to be displayed as a wall.
        rect: The shape pygame will display as a wall.
        rect.x: The x-coordinate of the wall.
        rect.y: The y-coordinate of the wall.
    """

    def __init__(self, x_position=0, y_position=0):
        """The class contructor, which creates a new wall.

        Args:
            x_position: The x-position of the wall in the labyrinth.
            y_position: The y-position of the wall in the labyrinth.
        """

        super().__init__()

        self.image = load_image("wall.png")

        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position
