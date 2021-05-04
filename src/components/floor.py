import pygame
from load_image import load_image

class Floor(pygame.sprite.Sprite):
    """A class which creates a floor to display in the game.

    Attributes:
        image: The image to be displayed as a floor.
        rect: The shape pygame will display as a floor.
        rect.x: The x-coordinate of the floor.
        rect.y: The y-coordinate of the floor.
    """

    def __init__(self, x_position=0, y_position=0):
        """The class contructor, which creates a new floor.

        Args:
            x_position: The x-position of the floor in the labyrinth.
            y_position: The y-position of the floor in the labyrinth.
        """

        super().__init__()

        self.image = load_image("floor.png")

        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position
