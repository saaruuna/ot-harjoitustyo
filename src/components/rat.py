import pygame
from load_image import load_image


class Rat(pygame.sprite.Sprite):
    """A class which creates a rat to display in the game.

    Attributes:
        image: The image to be displayed as a rat.
        rect: The shape pygame will display as a rat.
        rect.x: The x-coordinate of the rat.
        rect.y: The y-coordinate of the rat.
    """

    def __init__(self, x_position=0, y_position=0):
        """The class contructor, which creates a new rat.

        Args:
            x_position: The x-position of the rat in the labyrinth.
            y_position: The y-position of the rat in the labyrinth.
        """

        super().__init__()

        self.image = load_image("rat.png")
        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position
