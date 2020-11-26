import unittest

from src.task import Task

class TestTask(unittest.TestCase):

# - "Wash Dishes" is preferred over "Cook Dinner"
    def test_wash_dishes_preferred_over_cook_dinner(self):
        self.assertEqual("Wash Dishes", task())

# - "Cook Dinner" is preferred over "Clean Windows"
# - "Clean Windows is preferred over "Wash Dishes"