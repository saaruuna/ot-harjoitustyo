import pygame
from ui.menu import Menu

class GameOverMenu(Menu):
    """A class which creates a Game Over menu to be displayed at the end of a game.
        There are two menu options, Play again and Quit. Play again leads the player
        back to the main menu. Quit closes the game.

    Attributes inherited from superclass:
        game: The game which the menu is connected to.
        run_display: A boolean value which controls whther a menu should be displayed or not.
        event_handler: The EventHandler object attached to the game to handle input from the player.
        renderer: The Renderer object attached to the game which renders different menus.
        cursor_rect: The cursor shape to be displayed in the menu.
        offset: The offset of the cursor to where it is pointing.

    Attributes:
        state: The menu option to which the player's cursor is pointing.
        status: The status is passed to the Renderer object to display whether the player lost or won.
        replayx: The x-position of "Play again" text.
        replayy: The y-position of "Play again" text.
        quitx: The x-position of "Quit" text.
        quity: The y-position of "Quit" text.
        cursor_rect.midtop: The position of the cursor on the menu.
    """

    def __init__(self, game):
        """The class contructor, which creates a new Main Menu.

        Args:
            game: The game which the menu is attached to. This is passed to the constructor of the Menu superclass.
        """

        Menu.__init__(self, game)
        self.state = "Play again"
        self.status = ""
        self.replayx, self.replayy = 200, 240
        self.quitx, self.quity = 400, 240
        self.cursor_rect.midtop = (self.replayx + self.offset, self.replayy)

    def display_menu(self):
        """Displays the Game Over Menu to the player until the player navigates to a different menu.
        """

        self.run_display = True
        while self.run_display:
            self.event_handler.handle_events()
            self._check_input()
            self.renderer.render_game_over_menu(self.replayx, self.replayy, self.quitx, self.quity, self.status)
            self.renderer.draw_cursor(self.cursor_rect.x, self.cursor_rect.y)
            self.renderer.blit_screen()

    def _move_cursor(self):
        """Displays the cursor to the player as it moves across different options on the Game Over Menu.
            The attribute state is used to track where the cursor is.
        """

        if self.event_handler.right_key:
            if self.state == "Play again":
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = "Quit"
            elif self.state == "Quit":
                self.cursor_rect.midtop = (self.replayx + self.offset, self.replayy)
                self.state = "Play again"
        elif self.event_handler.left_key:
            if self.state == "Play again":
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = "Quit"
            elif self.state == "Quit":
                self.cursor_rect.midtop = (self.replayx + self.offset, self.replayy)
                self.state = "Play again"

    def _check_input(self):
        """A method which responds to input from the player.
        Closes the Game Over Menu by setting the value run_display to False
        and either navigates back to the Main Menu or closes the game.
        """

        self._move_cursor()
        if self.event_handler.quit_key:
            self.game.playing, self.game.running = False, False
            self.run_display = False
        elif self.event_handler.start_key:
            if self.state == "Play again":
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            elif self.state == "Quit":
                self.game.playing, self.game.running = False, False
                self.run_display = False
