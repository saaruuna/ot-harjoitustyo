import pygame

class EventQueue:
    """A class to listen to player input.
    """

    def get(self):
        """This method returns the events input by the player.
        """

        return pygame.event.get()
