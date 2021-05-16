from ui.menu import Menu

class LabSelectionMenu(Menu):
    """A class which creates a lab selection menu. Menu options are labyrinth names
        pulled from the lab database and displayed to the player. Labyrinths are displayed
        in groups of three to a page.

    Attributes inherited from superclass:
        game: The game which the menu is connected to.
        run_display: A boolean value which controls whther a menu should be displayed or not.
        event_handler: The EventHandler object attached to the game to handle input from the player.
        renderer: The Renderer object attached to the game which renders different menus.
        cursor_rect: The cursor shape to be displayed in the menu.
        offset: The offset of the cursor to where it is pointing.

    Attributes:
        state: The menu option to which the player's cursor is pointing.
        lab_selection: An array of sets of three labyrinths.
        page: One page shows three labyrinths. The page value shows which three to display.
        firstx: The x-coordinate of the first option on the page.
        firsty: The y-coordinate of the first option on the page.
        secondx: The x-coordinate of the second option on the page.
        secondy: The y-coordinate of the second option on the page.
        thirdx: The x-coordinate of the third option on the page.
        thirdy: The y-coordinate of the third option on the page.
        cursor_rect.midtop: The position of the cursor.
    """

    def __init__(self, game):
        """The class contructor, which creates a new Main Menu.

        Args:
            game: The game which the menu is attached to. This is passed to the
            constructor of the Menu superclass.
        """

        Menu.__init__(self, game)
        self.state = "0"
        self.lab_selection = []

        j = 0
        while j < len(self.game.labs):
            self.lab_selection.append(self.game.labs[j:j+3])
            j += 3

        self.page = 0
        mid_width, mid_height = self.renderer.display_width / 2, self.renderer.display_height / 2
        self.firstx, self.firsty = mid_width, mid_height
        self.secondx, self.secondy = mid_width, mid_height + 30
        self.thirdx, self.thirdy = mid_width, mid_height + 60
        self.cursor_rect.midtop = (self.firstx + self.offset, self.firsty)

    def update_lab_selection_menu(self):
        self.lab_selection = []

        j = 0
        while j < len(self.game.labs):
            self.lab_selection.append(self.game.labs[j:j+3])
            j += 3

    def display_menu(self):
        """Displays the Lab Selection Menu to the player until the player navigates
            to a different menu.
        """

        self.page = 0
        self.state = "0"
        self.cursor_rect.midtop = (self.firstx + self.offset, self.firsty)
        self.run_display = True
        while self.run_display:
            self.event_handler.handle_events()
            self._check_input()
            self.renderer.render_lab_selection_menu(self.lab_selection[self.page])
            self.renderer.draw_cursor(self.cursor_rect.x, self.cursor_rect.y)
            self.renderer.blit_screen()

    def _move_cursor(self):
        """Displays the cursor to the player as it moves across different options
            on the Lab Selection Menu. The attribute state is used to track where
            the cursor is.
        """

        if self.event_handler.down_key:
            if self.state == "0":
                if len(self.lab_selection[self.page]) > 1:
                    self.cursor_rect.midtop = (self.secondx + self.offset, self.secondy)
                    self.state = "1"
            elif self.state == "1":
                if len(self.lab_selection[self.page]) > 2:
                    self.cursor_rect.midtop = (self.thirdx + self.offset, self.thirdy)
                    self.state = "2"
            elif self.state == "2":
                if len(self.lab_selection[self.page]) > 2:
                    self.cursor_rect.midtop = (self.firstx + self.offset, self.firsty)
                    self.state = "0"
        elif self.event_handler.up_key:
            if self.state == "0":
                if len(self.lab_selection[self.page]) > 2:
                    self.cursor_rect.midtop = (self.thirdx + self.offset, self.thirdy)
                    self.state = "2"
            elif self.state == "1":
                if len(self.lab_selection[self.page]) > 1:
                    self.cursor_rect.midtop = (self.firstx + self.offset, self.firsty)
                    self.state = "0"
            elif self.state == "2":
                if len(self.lab_selection[self.page]) > 2:
                    self.cursor_rect.midtop = (self.secondx + self.offset, self.secondy)
                    self.state = "1"
        elif self.game.event_handler.left_key:
            self.state = "0"
            self.cursor_rect.midtop = (self.firstx + self.offset, self.firsty)
        elif self.game.event_handler.right_key:
            self.state = "0"
            self.cursor_rect.midtop = (self.firstx + self.offset, self.firsty)

    def _check_input(self):
        """A method which responds to input from the player. Either changes pages or
        closes the Lab Selection Menu and opens the chosen labyrinth game.
        """

        self._move_cursor()
        if self.event_handler.quit_key:
            self.game.playing, self.game.running = False, False
            self.run_display = False
        elif self.event_handler.start_key:
            if self.state == "0":
                choice = self.page*3
                self.game.lab = self.game.labs[choice]
                self.game.playing = True
                self.run_display = False
            elif self.state == "1":
                choice = self.page*3 + 1
                self.game.lab = self.game.labs[choice]
                self.game.playing = True
                self.run_display = False
            elif self.state == "2":
                choice = self.page*3 + 2
                self.game.lab = self.game.labs[choice]
                self.game.playing = True
                self.run_display = False
        elif self.event_handler.left_key:
            if self.page > 0:
                self.page -= 1
        elif self.event_handler.right_key:
            if self.page + 1 < len(self.lab_selection):
                self.page += 1
