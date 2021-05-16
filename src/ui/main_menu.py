from ui.menu import Menu

class MainMenu(Menu):
    """A class which creates a main menu to be displayed at the beginning of a game.
        There are two menu options, Solve and Create. Solve leads the player to a list of playable
        labyrinths. Create leads the player to a labyrinth designer.

    Attributes inherited from superclass:
        game: The game which the menu is connected to.
        run_display: A boolean value which controls whether a menu should be displayed or not.
        event_handler: The EventHandler object attached to the game to handle input from the player.
        renderer: The Renderer object attached to the game which renders different menus.
        cursor_rect: The cursor shape to be displayed in the menu.
        offset: The offset of the cursor to where it is pointing.

    Attributes:
        state: The menu option to which the player's cursor is pointing.
        solvex: The x-position of "Solve" text.
        solvey: The y-position of "Solve" text.
        createx: The x-position of "Create" text.
        createy: The y-position of "Create" text.
    """

    def __init__(self, game):
        """The class contructor, which creates a new Main Menu.

        Args:
            game: The game which the menu is attached to. This is passed to the
            constructor of the Menu superclass.
        """

        Menu.__init__(self, game)
        self.state = "Solve"
        mid_width, mid_height = self.renderer.display_width / 2, self.renderer.display_height / 2
        self.solvex, self.solvey = mid_width, mid_height + 30
        self.createx, self.createy = mid_width, mid_height + 50
        self.cursor_rect.midtop = (self.solvex + self.offset, self.solvey)

    def display_menu(self):
        """Displays the Main Menu to the player until the player navigates to a different menu.
        """

        self.run_display = True
        while self.run_display:
            self.event_handler.handle_events()
            self._check_input()
            self.renderer.render_main_menu(self.solvex, self.solvey, self.createx, self.createy)
            self.renderer.draw_cursor(self.cursor_rect.x, self.cursor_rect.y)
            self.renderer.blit_screen()

    def _move_cursor(self):
        """Displays the cursor to the player as it moves across different options on the Main Menu.
            The attribute state is used to track where the cursor is.
        """

        if self.event_handler.down_key:
            if self.state == "Solve":
                self.cursor_rect.midtop = (self.createx + self.offset, self.createy)
                self.state = "Create"
            elif self.state == "Create":
                self.cursor_rect.midtop = (self.solvex + self.offset, self.solvey)
                self.state = "Solve"
        elif self.event_handler.up_key:
            if self.state == "Solve":
                self.cursor_rect.midtop = (self.createx + self.offset, self.createy)
                self.state = "Create"
            elif self.state == "Create":
                self.cursor_rect.midtop = (self.solvex + self.offset, self.solvey)
                self.state = "Solve"

    def _check_input(self):
        """A method which responds to input from the player.
        Closes the Main Menu by setting the value run_display to False
        and either opens a new Menu or closes the game.
        """

        self._move_cursor()
        if self.event_handler.quit_key:
            self.game.playing, self.game.running = False, False
            self.run_display = False
        elif self.event_handler.start_key:
            if self.state == "Solve":
                self.game.curr_menu = self.game.lab_selection_menu
                self.run_display = False
            if self.state == "Create":
                self.game.curr_menu = self.game.lab_size_menu
                self.run_display = False
