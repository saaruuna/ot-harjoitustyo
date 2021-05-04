import pygame
from load_image import load_image

class Cheese(pygame.sprite.Sprite):
    """A class which creates a cheese to display in the game.

    Attributes:
        image: The image to be displayed as a cheese.
        rect: The shape pygame will display as a cheese.
        rect.x: The x-coordinate of the cheese.
        rect.y: The y-coordinate of the cheese.
    """

    def __init__(self, x_position=0, y_position=0):
        """The class contructor, which creates a new cheese.

        Args:
            x_position: The x-position of the cheese in the labyrinth.
            y_position: The y-position of the cheese in the labyrinth.
        """
        super().__init__()

        self.image = load_image("cheese.png")

        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position
