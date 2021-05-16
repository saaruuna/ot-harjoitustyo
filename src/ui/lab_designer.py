import tkinter
from tkinter import messagebox
import pygame
import pygame_gui
from load_image import load_image
from logic.lab_design import LabDesign

SCALE = 20

class LabDesigner:
    """A class which creates a lab designer graphical interface for the player to use
        when designing a lab.

    Attributes:
        game: The game to which the lad designer is attached.
        size: The size n of the n*n lab to be designed.
        mode: The mode represents the element (floor, rat, cheese, trap, wall) to be
        added to the lab.
        lab_design: A LabDesign object to keep track of the lab design.
        manager: The pygame_gui manager object to manage the interface.
        window_surface: The window to which the interface is displayed:
        design_surface: The surface on which the current lab design is displayed.
        design_surface_center: The center of the design surface.
    """

    def __init__(self, game, size):
        """The class contructor, which creates a new Main Menu.

        Args:
            game: The game which the menu is attached to.
            size: The size n of the n*n lab to be designed.
        """

        pygame.init()
        self.game = game
        self.size = size
        self.mode = "floor"
        self.lab_design = LabDesign(self.size)
        self.manager = pygame_gui.UIManager((480, 270))
        self.window_surface = self.game.renderer.window

        design_surface_width = SCALE * self.size
        design_surface_height = SCALE * self.size

        self.design_surface = pygame.Surface((design_surface_width, design_surface_height))
        self.design_surface_center = (
        (350 - design_surface_width) / 2,
        (270 - design_surface_height) / 2,
        )

    def start(self):
        """The method to initialize the lab design and interpret user input. This method
            is overlong, but I couldn't find a way to initialize the text entry lines and
            buttons outside of this method.
        """

        self.lab_design.initialize_lab_design()
        background = self.game.renderer.display
        background.fill(self.game.renderer.black)

        name_entry_rect = pygame.Rect((235, 10), (100, 20))
        name_entry = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(name_entry_rect,
                                                    manager=self.manager)
        name_entry.set_text('MyLab')

        x_entry_rect =  pygame.Rect((370, 185), (25, 20))
        x_entry = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(x_entry_rect,
                                                    manager=self.manager)
        x_entry.set_allowed_characters('numbers')
        x_entry.set_text('0')

        y_entry_rect =  pygame.Rect((420, 185), (25, 20))
        y_entry = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(y_entry_rect,
                                                    manager=self.manager)
        y_entry.set_allowed_characters('numbers')
        y_entry.set_text('0')

        options = ['floor', 'wall', 'trap', 'cheese', 'rat']

        mode_menu = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(
                                                    options_list=options,
                                                    starting_option=self.mode,
                                                    relative_rect=pygame.Rect((350, 32), (120, 20)),
                                                    manager=self.manager)

        place_element_button = pygame_gui.elements.UIButton(
                                                    relative_rect=pygame.Rect((350, 215), (120, 20)),
                                                    text='Place element!',
                                                    manager=self.manager)

        finished_button = pygame_gui.elements.UIButton(
                                                    relative_rect=pygame.Rect((350, 240), (120, 20)),
                                                    text='Finished!',
                                                    manager=self.manager)

        clock = pygame.time.Clock()

        while self.game.designing:
            time_delta = clock.tick(60)/1000.0
            self.mode = mode_menu.selected_option

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.running, self.game.playing = False, False
                    self.game.designing = False

                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == place_element_button:
                            x_coordinate = int(x_entry.get_text())
                            y_coordinate = int(y_entry.get_text())
                            if self._add_object_to_lab(self.mode, x_coordinate,
                                                                y_coordinate):
                                x_entry.set_text('0')
                                y_entry.set_text('0')
                        elif event.ui_element == finished_button:
                            if self._add_finished_lab_to_repository(name_entry.get_text(),
                                                    self.lab_design.lab_map, self.size):
                                self.game.curr_menu = self.game.main_menu
                                self.game.designing = False

                self.manager.process_events(event)

            self.manager.update(time_delta)
            self.window_surface.blit(background, (0,0))
            self._display_text_components()
            self._display_lab_design()
            self.manager.draw_ui(self.window_surface)
            pygame.display.update()

    def _display_text_components(self):
        """The method to display the text components of the lab design.
        """

        self.window_surface.blit(self._get_name_text()[0], self._get_name_text()[1])
        self.window_surface.blit(self._get_place_text()[0], self._get_place_text()[1])
        self.window_surface.blit(self._get_position_text()[0], self._get_position_text()[1])
        self.window_surface.blit(self._get_x_text()[0], self._get_x_text()[1])
        self.window_surface.blit(self._get_y_text()[0], self._get_y_text()[1])

    def _get_name_text(self):
        """The method to get the 'Name your lab' text component of the lab design.

        Returns:
            tuple name_text_surface and its position name_text_rect
        """

        name_text_surface = self.game.renderer.font.render('Name your lab', True,
                                                        self.game.renderer.white)
        name_text_rect = name_text_surface.get_rect()
        name_text_rect.left = 10
        name_text_rect.top = 12

        return name_text_surface, name_text_rect

    def _get_place_text(self):
        """The method to get the 'Place' text component of the lab design.

        Returns:
            tuple place_text_surface and its position place_text_rect
        """

        place_text_surface = self.game.renderer.font.render('Place', True,
                                                        self.game.renderer.white)
        place_text_rect = place_text_surface.get_rect()
        place_text_rect.left = 350
        place_text_rect.top = 12

        return place_text_surface, place_text_rect

    def _get_position_text(self):
        """The method to get the 'Position' text component of the lab design.

        Returns:
            tuple position_text_surface and its position position_text_rect
        """

        position_text_surface = self.game.renderer.font.render('Position', True,
                                                        self.game.renderer.white)
        position_text_rect = position_text_surface.get_rect()
        position_text_rect.left = 350
        position_text_rect.top = 155

        return position_text_surface, position_text_rect

    def _get_x_text(self):
        """The method to get the 'x' text component of the lab design.

        Returns:
            tuple x_text_surface and its position x_text_rect
        """

        x_text_surface = self.game.renderer.font.render('x', True,
                                                        self.game.renderer.white)
        x_text_rect = x_text_surface.get_rect()
        x_text_rect.left = 350
        x_text_rect.top = 185

        return x_text_surface, x_text_rect

    def _get_y_text(self):
        """The method to get the 'y' text component of the lab design.

        Returns:
            tuple y_text_surface and its position y_text_rect
        """

        y_text_surface = self.game.renderer.font.render('y', True,
                                                        self.game.renderer.white)
        y_text_rect = y_text_surface.get_rect()
        y_text_rect.left = 400
        y_text_rect.top = 185

        return y_text_surface, y_text_rect

    def _display_lab_design(self):
        """The method to display the lab design as the player inputs elements into it.
        """

        for y_position in range(self.size):
            for x_position in range(self.size):
                cell = self.lab_design.lab_map[y_position][x_position]
                normalized_x = x_position * SCALE
                normalized_y = y_position * SCALE

                if cell == 0:
                    floor_image = load_image("floor.png")
                    floor_rect = floor_image.get_rect()
                    floor_rect.left = normalized_x
                    floor_rect.top = normalized_y
                    self.design_surface.blit(floor_image, floor_rect)
                elif cell == 1:
                    wall_image = load_image("wall.png")
                    wall_rect = wall_image.get_rect()
                    wall_rect.left = normalized_x
                    wall_rect.top = normalized_y
                    self.design_surface.blit(wall_image, wall_rect)
                elif cell == 2:
                    trap_image = load_image("trap.png")
                    trap_rect = trap_image.get_rect()
                    trap_rect.left = normalized_x
                    trap_rect.top = normalized_y
                    self.design_surface.blit(trap_image, trap_rect)
                elif cell == 3:
                    cheese_image = load_image("cheese.png")
                    cheese_rect = cheese_image.get_rect()
                    cheese_rect.left = normalized_x
                    cheese_rect.top = normalized_y
                    self.design_surface.blit(cheese_image, cheese_rect)
                elif cell == 4:
                    rat_image = load_image("rat.png")
                    rat_rect = rat_image.get_rect()
                    rat_rect.left = normalized_x
                    rat_rect.top = normalized_y
                    self.design_surface.blit(rat_image, rat_rect)

        self.window_surface.blit(self.design_surface, self.design_surface_center)

    def _add_finished_lab_to_repository(self, name, lab_map, size):
        """The method to display error messages if adding the finished lab
            to the lab repository was unsuccessful.

        Returns:
            True, if adding the lab was successful.
            False, if the lab does not contain a rat.
            False, if the lab does not contain a trap.
            False, if the lab does not contain a cheese.
            False, if the lab name is taken.
        """

        root = tkinter.Tk()
        root.withdraw()

        lab_design_status = self.lab_design.add_finished_lab_to_repository(name, lab_map, size)

        if lab_design_status == "success":
            return True
        elif lab_design_status == "must_contain_rat":
            messagebox.showerror("Error", "Your lab must contain a rat!")
            return False
        elif lab_design_status == "must_contain_trap":
            messagebox.showerror("Error", "Your lab must contain at least one trap!")
            return False
        elif lab_design_status == "must_contain_cheese":
            messagebox.showerror("Error", "Your lab must contain at least one cheese!")
            return False
        elif lab_design_status == "lab_name_taken":
            messagebox.showerror("Error", "This lab name is taken! Choose a different name.")
            return False

    def _add_object_to_lab(self, mode, x_coordinate, y_coordinate):
        """The method to display error messages if adding an element
            to the lab design was unsuccessful.

        Returns:
            True, if adding the element was successful.
            False, if the x-coordinate was out of bounds.
            False, if the y-coordinate was out of bounds.
            False, if the lab already contains a rat.
        """

        root = tkinter.Tk()
        root.withdraw()

        lab_design_status = self.lab_design.add_object_to_lab(mode, x_coordinate, y_coordinate)

        if lab_design_status == "success":
            return True
        elif lab_design_status == "x_out_of_bounds":
            messagebox.showerror("Error", "Your x-coordinate is out of bounds!")
            return False
        elif lab_design_status == "y_out_of_bounds":
            messagebox.showerror("Error", "Your y-coordinate is out of bounds!")
            return False
        elif lab_design_status == "too_many_rats":
            messagebox.showerror("Error", "Your lab can only contain one rat!")
            return False
