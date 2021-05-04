import pygame
from load_image import load_image

class Trap(pygame.sprite.Sprite):
    """A class which creates a trap to display in the game.

    Attributes:
        image: The image to be displayed as a trap.
        rect: The shape pygame will display as a trap.
        rect.x: The x-coordinate of the trap.
        rect.y: The y-coordinate of the trap.
    """

    def __init__(self, x_position=0, y_position=0):
        """The class contructor, which creates a new trap.

        Args:
            x_position: The x-position of the trap in the labyrinth.
            y_position: The y-position of the trap in the labyrinth.
        """

        super().__init__()

        self.image = load_image("trap.png")

        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position
