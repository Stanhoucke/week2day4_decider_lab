import unittest

from src.task import Task

class TestTask(unittest.TestCase):

    def setUp(self):
        self.task_1 = Task("Wash Dishes", 15)


    def test_task_has_name(self):
        self.assertEqual("Wash Dishes", self.task_1.name)

    # - "Wash Dishes" is preferred over "Cook Dinner"
    # def test_wash_dishes_preferred_over_cook_dinner(self):
    #     self.assertEqual("Wash Dishes", self.task_1())

    # - "Cook Dinner" is preferred over "Clean Windows"
    # - "Clean Windows is preferred over "Wash Dishes"