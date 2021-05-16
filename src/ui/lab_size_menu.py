from ui.menu import Menu
from ui.lab_designer import LabDesigner

class LabSizeMenu(Menu):
    """A class which creates a Lab Size menu to be displayed before designing a labyrinth.
        The player navigates between size options (2--9) by using the left and right
        buttons.

    Attributes inherited from superclass:
        game: The game which the menu is connected to.
        run_display: A boolean value which controls whther a menu should be displayed or not.
        event_handler: The EventHandler object attached to the game to handle input from the player.
        renderer: The Renderer object attached to the game which renders different menus.
        cursor_rect: The cursor shape to be displayed in the menu.
        offset: The offset of the cursor to where it is pointing.

    Attributes:
        state: The lab size option currently being displayed.
    """

    def __init__(self, game):
        """The class contructor, which creates a new Main Menu.

        Args:
            game: The game which the menu is attached to. This is passed to the
            constructor of the Menu superclass.
        """

        Menu.__init__(self, game)
        self.state = "2"

    def display_menu(self):
        """Displays the Lab Size Menu to the player until the player chooses a lab size.
        """

        self.run_display = True
        while self.run_display:
            self.event_handler.handle_events()
            self._check_input()
            self.renderer.render_lab_size_menu(self.state)
            self.renderer.blit_screen()

    def _change_state(self):
        """Displays the current state (lab size option) to be player as
            they cycle through the options. The attribute state is used to track
            which option is being displayed.
        """

        if self.event_handler.left_key:
            if self.state == "2":
                self.state = "9"
            elif self.state == "3":
                self.state = "2"
            elif self.state == "4":
                self.state = "3"
            elif self.state == "5":
                self.state = "4"
            elif self.state == "6":
                self.state = "5"
            elif self.state == "7":
                self.state = "6"
            elif self.state == "8":
                self.state = "7"
            elif self.state == "9":
                self.state = "8"
        elif self.event_handler.right_key:
            if self.state == "2":
                self.state = "3"
            elif self.state == "3":
                self.state = "4"
            elif self.state == "4":
                self.state = "5"
            elif self.state == "5":
                self.state = "6"
            elif self.state == "6":
                self.state = "7"
            elif self.state == "7":
                self.state = "8"
            elif self.state == "8":
                self.state = "9"
            elif self.state == "9":
                self.state = "2"

    def _check_input(self):
        """A method which responds to input from the player.
        Closes the Main Menu by setting the value run_display to False
        or navigates to designing a lab.
        """

        self._change_state()
        if self.event_handler.quit_key:
            self.game.playing, self.game.running = False, False
            self.run_display = False
        elif self.event_handler.start_key:
            if self.state == "2":
                self.game.lab_designer = LabDesigner(self.game, 2)
                self.game.designing = True
                self.run_display = False
            elif self.state == "3":
                self.game.lab_designer = LabDesigner(self.game, 3)
                self.game.designing = True
                self.run_display = False
            elif self.state == "4":
                self.game.lab_designer = LabDesigner(self.game, 4)
                self.game.designing = True
                self.run_display = False
            elif self.state == "5":
                self.game.lab_designer = LabDesigner(self.game, 5)
                self.game.designing = True
                self.run_display = False
            elif self.state == "6":
                self.game.lab_designer = LabDesigner(self.game, 6)
                self.game.designing = True
                self.run_display = False
            elif self.state == "7":
                self.game.lab_designer = LabDesigner(self.game, 7)
                self.game.designing = True
                self.run_display = False
            elif self.state == "8":
                self.game.lab_designer = LabDesigner(self.game, 8)
                self.game.designing = True
                self.run_display = False
            elif self.state == "9":
                self.game.lab_designer = LabDesigner(self.game, 9)
                self.game.designing = True
                self.run_display = False
