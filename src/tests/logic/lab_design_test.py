import unittest
from logic.lab_design import LabDesign

class TestLabDesign(unittest.TestCase):
    def setUp(self):
        self.lab_design1 = LabDesign(5)

    def test_initialize_lab_design(self):
        self.lab_design1.initialize_lab_design()

        for i in range (0, self.lab_design1.size):
            for j in range(0, self.lab_design1.size):
                self.assertEqual(self.lab_design1.lab_map[i][j], 0)

    def test_error_does_not_contain_rat(self):
        self.lab_design1.initialize_lab_design()
        self.assertEqual(self.lab_design1.add_finished_lab_to_repository("newlab", self.lab_design1.lab_map,
                                                        self.lab_design1.size), "must_contain_rat")

    def test_error_does_not_contain_trap(self):
        self.lab_design1.initialize_lab_design()
        self.lab_design1.add_object_to_lab("rat", 0, 0)
        self.assertEqual(self.lab_design1.add_finished_lab_to_repository("newlab", self.lab_design1.lab_map,
                                                        self.lab_design1.size), "must_contain_trap")

    def test_error_does_not_contain_cheese(self):
        self.lab_design1.initialize_lab_design()
        self.lab_design1.add_object_to_lab("rat", 0, 0)
        self.lab_design1.add_object_to_lab("trap", 0, 1)
        self.assertEqual(self.lab_design1.add_finished_lab_to_repository("newlab", self.lab_design1.lab_map,
                                                        self.lab_design1.size), "must_contain_cheese")

    def test_error_lab_name_taken(self):
        self.lab_design1.initialize_lab_design()
        self.lab_design1.add_object_to_lab("rat", 0, 0)
        self.lab_design1.add_object_to_lab("trap", 0, 1)
        self.lab_design1.add_object_to_lab("cheese", 0, 2)
        self.assertEqual(self.lab_design1.add_finished_lab_to_repository("DEMO1", self.lab_design1.lab_map,
                                                        self.lab_design1.size), "lab_name_taken")

    def test_adding_lab_succeeds(self):
        self.lab_design1.initialize_lab_design()
        self.lab_design1.add_object_to_lab("rat", 0, 0)
        self.lab_design1.add_object_to_lab("trap", 0, 1)
        self.lab_design1.add_object_to_lab("cheese", 0, 2)
        self.assertEqual(self.lab_design1.add_finished_lab_to_repository("newlab", self.lab_design1.lab_map,
                                                        self.lab_design1.size), "success")

    def test_error_contains_rat(self):
        self.lab_design1.initialize_lab_design()
        self.lab_design1.add_object_to_lab("rat", 0, 0)
        self.assertEqual(self.lab_design1.add_object_to_lab("rat", 0, 1), "too_many_rats")

    def test_error_x_out_of_bounds(self):
        self.lab_design1.initialize_lab_design()
        self.assertEqual(self.lab_design1.add_object_to_lab("rat", 9, 0), "x_out_of_bounds")

    def test_error_y_out_of_bounds(self):
        self.lab_design1.initialize_lab_design()
        self.assertEqual(self.lab_design1.add_object_to_lab("rat", 0, 9), "y_out_of_bounds")

    def test_adding_element_succeeds(self):
        self.lab_design1.initialize_lab_design()
        self.assertEqual(self.lab_design1.add_object_to_lab("cheese", 0, 0), "success")
