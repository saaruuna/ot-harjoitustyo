import unittest
from initialize_database import initialize_database
from repositories.lab_repository import lab_repository
from logic.lab import Lab

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

    def test_find_all(self):
        labs = lab_repository.find_all()
        self.assertEqual(len(labs), 5)

    def test_find_by_name(self):
        demo1 = lab_repository.find_by_name("DEMO1")
        demo2 = lab_repository.find_by_name("DEMO2")
        self.assertEqual(demo1.name, self.lab1.name)
        self.assertEqual(demo1.lab_map, self.lab1.lab_map)
        self.assertEqual(demo2.name, self.lab2.name)
        self.assertEqual(demo2.lab_map, self.lab2.lab_map)

    def test_add_lab(self):
        labs = lab_repository.find_all()
        self.assertEqual(len(labs), 5)
        lab_repository.add_lab("DEMOX", LAB_MAP2, 5)
        labs = lab_repository.find_all()
        self.assertEqual(len(labs), 6)

    def test_contains_lab(self):
        self.assertEqual(lab_repository.contains_lab(self.lab1.name), True)

    def test_does_not_contain_lab(self):
        self.assertEqual(lab_repository.contains_lab("IMPOSSIBLE"), False)
