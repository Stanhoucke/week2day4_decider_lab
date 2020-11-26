import unittest
from src.task import Task
from src.task_decider import *


class TestTask(unittest.TestCase):

    def setUp(self):
        self.task_1 = Task("Wash Dishes", 15)
        self.task_2 = Task("Cook Dinner", 30)


    def test_task_has_name(self):
        self.assertEqual("Wash Dishes", self.task_1.name)

    # - "Wash Dishes" is preferred over "Cook Dinner"
    def test_wash_dishes_preferred_over_cook_dinner(self):
        self.assertEqual("Wash Dishes", get_preferred_option(self.task_1.name, self.task_2.name))

    # - "Cook Dinner" is preferred over "Clean Windows"
    # - "Clean Windows is preferred over "Wash Dishes"