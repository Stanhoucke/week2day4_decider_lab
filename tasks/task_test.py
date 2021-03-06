import unittest
from src.task import Task
from src.task_decider import *


class TestTask(unittest.TestCase):

    def setUp(self):
        self.task_1 = Task("Wash Dishes", 15)
        self.task_2 = Task("Cook Dinner", 30)
        self.task_3 = Task("Clean Windows", 20)


    def test_task_has_name(self):
        self.assertEqual("Wash Dishes", self.task_1.name)

    # - "Wash Dishes" is preferred over "Cook Dinner"
    def test_wash_dishes_preferred_over_cook_dinner(self):
        self.assertEqual(self.task_1, get_preferred_option(self.task_1, self.task_2))
    
    def test_cook_dinner_not_preferred_over_wash_dishes(self):
        self.assertEqual(self.task_1, get_preferred_option(self.task_2, self.task_1))

    # - "Cook Dinner" is preferred over "Clean Windows"

    def test_cook_dinner_preferred_over_clean_windows(self):
        self.assertEqual(self.task_2, get_preferred_option(self.task_2, self.task_3))

    def test_clean_windows_not_preferred_over_cook_dinner(self):
        self.assertEqual(self.task_2, get_preferred_option(self.task_3, self.task_2))

    # - "Clean Windows is preferred over "Wash Dishes"
    
    def test_clean_windows_preferred_over_wash_dishes(self):
        self.assertEqual(self.task_3, get_preferred_option(self.task_3, self.task_1))

    def test_wash_dishes_not_preferred_over_clean_windows(self):
        self.assertEqual(self.task_3, get_preferred_option(self.task_1, self.task_3))

    