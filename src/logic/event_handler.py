import pygame
from logic.event_queue import EventQueue

class EventHandler:
    """A class to handle keyboard input from the player.

    Attributes:
        event_queue: An EventQueue object to listen to player input.
        up_key: A boolean value to express whether the up key has been pressed.
        down_key: A boolean value to express whether the down key has been pressed.
        right_key: A boolean value to express whether the right key has been pressed.
        left_key: A boolean value to express whether the left key has been pressed.
        start_key: A boolean value to express whether the start key has been pressed.
        back_key: A boolean value to express whether the back key has been pressed.
        quit_key: A boolean value to express whether the quit key has been pressed.
    """

    def __init__(self):
        """The class contructor, which creates a new EventHandler with all keys initialized
        to False i.e. not pressed.
        """

        pygame.init()
        self.event_queue = EventQueue()
        self.up_key, self.down_key, self.right_key = False, False, False
        self.left_key, self.start_key, self.back_key = False, False, False
        self.quit_key, self.zero_key, self.one_key = False, False, False
        self.two_key, self.three_key, self.four_key = False, False, False

    def handle_events(self):
        """The method to set the value of a key to True when pressed.
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_key = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.start_key = True
                if event.key == pygame.K_BACKSPACE:
                    self.back_key = True
                if event.key == pygame.K_LEFT:
                    self.left_key = True
                if event.key == pygame.K_RIGHT:
                    self.right_key = True
                if event.key == pygame.K_UP:
                    self.up_key = True
                if event.key == pygame.K_DOWN:
                    self.down_key = True
                if event.key == pygame.K_0:
                    self.zero_key = True
                if event.key == pygame.K_1:
                    self.one_key = True
                if event.key == pygame.K_2:
                    self.two_key = True
                if event.key == pygame.K_3:
                    self.three_key = True
                if event.key == pygame.K_4:
                    self.four_key = True
                if event.key == pygame.K_ESCAPE:
                    self.quit_key = True

    def reset_keys(self):
        """The method to reset all key values to False.
        """
        self.up_key, self.down_key, self.right_key = False, False, False
        self.left_key, self.start_key, self.back_key = False, False, False
        self.quit_key, self.zero_key, self.one_key = False, False, False
        self.two_key, self.three_key, self.four_key = False, False, False
