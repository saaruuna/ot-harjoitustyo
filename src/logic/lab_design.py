import pygame
from repositories.lab_repository import lab_repository

SCALE = 20

class LabDesign:
    """A class to display the lab design to the player.

    Attributes:
        size: The size n of the n*n map.
        lab_map: An array of arrays describing the elements of the lab design.

    Args:
        size: The size n of the n*n map.
    """

    def __init__(self, size):
        """The class contructor, which creates a new LabDesign object.

        Attributes:
            size: The size n of the n*n map.
            lab_map: An array of arrays describing the elements of the lab design.

        Args:
            size: The size n of the n*n map.
        """

        pygame.init()
        self.size = size
        self.lab_map = []

    def initialize_lab_design(self):
        """The method to initialize all the elements in the Lab Design to 0, which
            will be displayed as floor to the player.
        """

        self.lab_map = []

        for i in range (0, self.size):
            temp_row = []
            for j in range(0, self.size):
                temp_row.insert(j, 0)
            self.lab_map.insert(i, temp_row)

    def add_finished_lab_to_repository(self, name, lab_map, size):
        """The method to check if a design can be added to the lab database and add
            it if possible.

        Args:
            name: The name of the lab.
            lab_map: The array of arrays of integers which describe the layout of
            the lab design.
            size: The size n of the n*n lab.

        Returns:
            string must_contain_rat, if the lab design does not contain a rat.
            string must_contain_trap, if the lab design does not contain a trap.
            string must_contain_cheese, if the lab design does not contain a cheese.
            string lab_name_taken, if the database already contains a lab of this name.
            string success, if the lab design was successfully inserted into the database
        """

        if len(name) == 0:
            return "unnamed_lab"

        if not self._contains_rat():
            return "must_contain_rat"

        if not self._contains_trap():
            return "must_contain_trap"

        if not self._contains_cheese():
            return "must_contain_cheese"

        if lab_repository.contains_lab(name):
            return "lab_name_taken"

        lab_repository.add_lab(name, lab_map, size)

        return "success"

    def add_object_to_lab(self, mode, x_coordinate, y_coordinate):
        """The method to check if an object can be added to the lab design and add
            it if possible.

        Args:
            mode: The element (rat, floor, cheese, trap, wall) to be added.
            x_coordinate: The x_coordinate of the element to be added.
            y_coordinate: The y_coordinate of the element to be added.

        Returns:
            string x_out_of_bounds, if the x-coordinate is out of the bounds of
            the lab design.
            string y_out_of_bounds, if the y-coordinate is out of the bounds of
            the lab design.
            string too_many_rats, if the lab_design already contains a rat.
            string success, if the element was successfully added to the lab design.
        """

        if x_coordinate < 0 or x_coordinate > self.size:
            return "x_out_of_bounds"

        if y_coordinate < 0 or y_coordinate > self.size:
            return "y_out_of_bounds"

        if mode == 'rat' and self._contains_rat():
            return "too_many_rats"

        if mode == 'floor':
            self.lab_map[x_coordinate][y_coordinate] = 0
        elif mode == 'wall':
            self.lab_map[x_coordinate][y_coordinate] = 1
        elif mode == 'trap':
            self.lab_map[x_coordinate][y_coordinate] = 2
        elif mode == 'cheese':
            self.lab_map[x_coordinate][y_coordinate] = 3
        elif mode == 'rat':
            self.lab_map[x_coordinate][y_coordinate] = 4

        return "success"

    def _contains_trap(self):
        """A method to check of the lab design contains a trap.

        Returns:
            False, if the lab design does not contain a trap.
            True, if the lab design contains a trap.
        """
        contains_trap = False

        for row in self.lab_map:
            for element in row:
                if element == 2:
                    contains_trap = True

        return contains_trap

    def _contains_cheese(self):
        """A method to check of the lab design contains a cheese.

        Returns:
            False, if the lab design does not contain a cheese.
            True, if the lab design contains a cheese.
        """

        contains_cheese = False

        for row in self.lab_map:
            for element in row:
                if element == 3:
                    contains_cheese = True

        return contains_cheese

    def _contains_rat(self):
        """A method to check of the lab design contains a rat.

        Returns:
            False, if the lab design does not contain a rat.
            True, if the lab design contains a rat.
        """

        contains_rat = False

        for row in self.lab_map:
            for element in row:
                if element == 4:
                    contains_rat = True

        return contains_rat
