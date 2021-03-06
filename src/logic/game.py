import pygame
from repositories.lab_repository import lab_repository
from logic.event_handler import EventHandler
from ui.renderer import Renderer
from ui.main_menu import MainMenu
from ui.game_over_menu import GameOverMenu
from ui.lab_selection_menu import LabSelectionMenu
from ui.lab_size_menu import LabSizeMenu
from ui.lab_designer import LabDesigner

SCALE = 20

class Game:
    """A class to handle the overall game and transitioning from game to menu.

    Attributes:
        labs: The array of Lab objects fetched from the lab database.
        renderer: The Renderer object to render games and menus.
        event_handler: The EventHandler object to interpret keyboard input from the player.
        running: A boolean value to tell whether the game is running. When this value is
        false, the game closes.
        playing: A boolean value to tell whether a game is being played. True displays a lab
        to play.
        main_menu: A Main Menu object to be displayed to the player.
        game_over_menu: A Game Over Menu to be displayed to the player.
        lab_selection_menu: A Lab Selection Menu to be displayed to the player.
        lab_size_menu: A Lab Size Menu to be displayed to the player.
        lab: The chosen lab to be played.
        curr_menu: The current menu being displayed to the player.
    """

    def __init__(self):
        """The class contructor, which creates a new Game.
        """

        pygame.init()
        self.labs = lab_repository.find_all()
        self.renderer = Renderer(self)
        self.event_handler = EventHandler()
        self.lab_designer = LabDesigner(self, 2)
        self.running, self.playing, self.designing = True, False, False
        self.main_menu = MainMenu(self)
        self.game_over_menu = GameOverMenu(self)
        self.lab_selection_menu = LabSelectionMenu(self)
        self.lab_size_menu = LabSizeMenu(self)
        self.lab = self.labs[0]
        self.curr_menu = self.main_menu

    def run(self):
        """The method to run a Game; either a game is being played or a menu is being displayed.
        """

        while self.playing:
            self._play()

        if self.designing:
            self._design()

        self.lab.reset_lab()
        self.labs = lab_repository.find_all()
        self.lab_selection_menu.update_lab_selection_menu()

    def _play(self):
        """The method to play a chosen lab. This method handles player input,
            checks whether a player has won or lost, and renders the lab.
        """

        if self.lab.rat_got_cheese():
            self.game_over_menu.status = "You win"
            self.curr_menu = self.game_over_menu
            self.playing = False

        if self.lab.rat_hit_trap():
            self.game_over_menu.status = "You lose"
            self.curr_menu = self.game_over_menu
            self.playing = False

        self.event_handler.handle_events()

        if self.event_handler.quit_key:
            self.running, self.playing = False, False
        if self.event_handler.left_key:
            self.lab.move_rat(x_change=-SCALE)
        if self.event_handler.right_key:
            self.lab.move_rat(x_change=SCALE)
        if self.event_handler.up_key:
            self.lab.move_rat(y_change=-SCALE)
        if self.event_handler.down_key:
            self.lab.move_rat(y_change=SCALE)

        self.renderer.render_lab(self.lab)

    def _design(self):
        """The method to initiate designing a lab. This method passes the display
            over to the LabDesigner object.
        """

        self.lab_designer.start()
