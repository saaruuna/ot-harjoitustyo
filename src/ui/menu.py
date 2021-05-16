import pygame

class Menu:
    """A superclass which creates common attributes of different menus to inherit.

    Attributes:
        game: The game which the menu is connected to.
        run_display: A boolean value which controls whther a menu should be displayed or not.
        event_handler: The EventHandler object attached to the game to handle input from the player.
        renderer: The Renderer object attached to the game which renders different menus.
        cursor_rect: The cursor shape to be displayed in the menu.
        offset: The offset of the cursor to where it is pointing.
    """

    def __init__(self, game):
        """The class contructor, which creates a new menu.

        Args:
            game: The game which the menu is attached to.
        """

        self.game = game
        self.run_display = True
        self.event_handler = self.game.event_handler
        self.renderer = self.game.renderer
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100
