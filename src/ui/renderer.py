import os
import pygame

SCALE = 20
dirname = os.path.dirname(__file__)

class Renderer:
    """A class which renders the user interface and games to play.

    Attributes:
        game: The game which the renderer is connected to.
        display_width: The width parameter of the display.
        display_height: The height parameter of the display.
        display: The pygame Surface object to which the game and menus are rendered.
        window: The window to which the display in rendered.
        font: The font to be used in the game.
        black: The RGB value for black to be used in the game.
        white: The RGB value for white to be used in the game.

    """

    def __init__(self, game):
        """The class contructor, which creates a new Renderer.

        Args:
            game: The game which the renderer is attached to.
        """

        pygame.init()
        self.game = game
        self.display_width, self.display_height = 480, 270
        self.display = pygame.Surface((self.display_width, self.display_height))
        self.window = pygame.display.set_mode((self.display_width, self.display_height))
        self.font = pygame.font.Font(os.path.join(dirname, "8-BIT WONDER.TTF"), 18)
        self.black, self.white = (0, 0, 0), (255, 255, 255)

    def render_lab(self, lab):
        """The method to render a chosen labyrinth.

        Args:
            lab: The Lab object to be rendered.
        """

        self.display.fill(self.black)

        self._draw_text("You are solving " + lab.name, self.display_width / 2, 20)

        surface_width = SCALE * len(lab.lab_map)
        surface_height = SCALE * len(lab.lab_map[0])
        surface = pygame.Surface((surface_width, surface_height))

        surface_center = (
        (self.display_width - surface_width) / 2,
        (self.display_height - surface_height) / 2,
        )

        lab.all_sprites.draw(surface)
        self.display.blit(surface, surface_center)

        self.blit_screen()

    def render_game_over_menu(self, replayx, replayy, quitx, quity, status):
        """The method to render a Game Over Menu.

        Args:
            replayx: The x-position of the Play again option.
            replayy: The y-position of the Play again option.
            quitx: The x-position of the Quit option.
            quity: The y-position of the Quit option.
            status: The status of the game when it finishes: whether the player won or lost.
        """

        self.display.fill(self.black)
        self._draw_text(status, self.display_width / 2, self.display_height / 2)
        self._draw_text("PLAY AGAIN", replayx, replayy)
        self._draw_text("QUIT", quitx, quity)

    def render_main_menu(self, solvex, solvey, createx, createy):
        """The method to render a Main Menu.

        Args:
            solvex: The x-position of the Solve option.
            solvey: The y-position of the Solve option.
            createx: The x-position of the Create option.
            createy: The y-position of the Create option.
        """

        self.display.fill(self.black)
        self._draw_text("Welcome to LabRat", self.display_width / 2,
        self.display_height / 2 - 20)
        self._draw_text("SOLVE MAZE", solvex, solvey)
        self._draw_text("CREATE MAZE", createx, createy)

    def render_lab_selection_menu(self, lab_selection):
        """The method to render a Lab Selection Menu.

        Args:
            lab_selection: The set of three labs to display on the page.
        """

        self.display.fill(self.black)
        self._draw_text("Choose your lab", self.display_width / 2,
        self.display_height / 2 - 50)
        mid_width, mid_height = self.display_width / 2, self.display_height / 2
        firstx, firsty = mid_width, mid_height
        secondx, secondy = mid_width, mid_height + 30
        thirdx, thirdy = mid_width, mid_height + 60

        if len(lab_selection) == 1:
            self._draw_text(lab_selection[0].name, firstx, firsty)
        elif len(lab_selection) == 2:
            self._draw_text(lab_selection[0].name, firstx, firsty)
            self._draw_text(lab_selection[1].name, secondx, secondy)
        elif len(lab_selection) == 3:
            self._draw_text(lab_selection[0].name, firstx, firsty)
            self._draw_text(lab_selection[1].name, secondx, secondy)
            self._draw_text(lab_selection[2].name, thirdx, thirdy)

        pygame.draw.polygon(self.display, self.white, ((mid_width+150, mid_height),
        (mid_width+150, mid_height-20), (mid_width+170, mid_height-10)))
        pygame.draw.polygon(self.display, self.white, ((mid_width-150, mid_height),
        (mid_width-150, mid_height-20), (mid_width-170, mid_height-10)))

    def render_lab_size_menu(self, state):
        """The method to render a Lab Selection Menu.

        Args:
            lab_selection: The state (desired size of the lab) to be displayed.
        """

        self.display.fill(self.black)
        mid_width, mid_height = self.display_width / 2, self.display_height / 2
        self._draw_text("Choose lab size", mid_width, mid_height - 50)
        self._draw_text(state, mid_width, mid_height)

        pygame.draw.polygon(self.display, self.white, ((mid_width+150, mid_height),
        (mid_width+150, mid_height-20), (mid_width+170, mid_height-10)))
        pygame.draw.polygon(self.display, self.white, ((mid_width-150, mid_height),
        (mid_width-150, mid_height-20), (mid_width-170, mid_height-10)))

    def _draw_text(self, text, x_position, y_position):
        """A convienient method to write text on the display.

        Args:
            text: The text to be written.
            x_position: The desired x-position of the text on the display.
            y_position: The desired y-position of the text on the display.
        """

        text_surface = self.font.render(text, True, self.white)
        text_rect = text_surface.get_rect()
        text_rect.center = (x_position, y_position)
        self.display.blit(text_surface, text_rect)

    def draw_cursor(self, x_position, y_position):
        """A method to draw the player's cursor on the screen.

        Args:
            x_position: The x-position of the cursor on the display.
            y_position: The y-position of the cursor on the display.
        """
        self._draw_text("*", x_position, y_position)

    def blit_screen(self):
        """A method to update the display.
        """
        self.window.blit(self.display, (0, 0))
        pygame.display.update()
        self.game.event_handler.reset_keys()
