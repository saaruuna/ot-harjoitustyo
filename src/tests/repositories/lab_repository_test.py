import unittest
from initialize_database import initialize_database
from repositories.lab_repository import lab_repository
from ui.lab import Lab

LAB_MAP1 =     [[1, 1, 1, 1, 1],
               [1, 0, 0, 0, 1],
               [1, 3, 2, 4, 1],
               [1, 0, 0, 0, 1],
               [1, 1, 1, 1, 1]]

LAB_MAP2 =     [[1, 1, 1, 1, 1],
               [1, 3, 2, 0, 1],
               [1, 0, 2, 4, 1],
               [1, 0, 0, 0, 1],
               [1, 1, 1, 1, 1]]

class TestLabRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.lab1 = Lab("DEMO1", LAB_MAP1)
        self.lab2 = Lab("DEMO2", LAB_MAP2)

    def test_initilization(self):
        labs = lab_repository.find_all()

        self.assertEqual(len(labs), 2)
        self.assertEqual(labs[0].name, self.lab1.name)
        self.assertEqual(labs[1].name, self.lab2.name)
        self.assertEqual(labs[0].lab_map, self.lab1.lab_map)
        self.assertEqual(labs[1].lab_map, self.lab2.lab_map)

    def test_find_by_name(self):
        demo1 = lab_repository.find_by_name("DEMO1")
        demo2 = lab_repository.find_by_name("DEMO2")
        self.assertEqual(demo1.name, self.lab1.name)
        self.assertEqual(demo1.lab_map, self.lab1.lab_map)
        self.assertEqual(demo2.name, self.lab2.name)
        self.assertEqual(demo2.lab_map, self.lab2.lab_map)
