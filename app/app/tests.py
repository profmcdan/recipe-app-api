from django.test import TestCase
from .calc import add, subtract


class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test that two numbers are addess together"""
        self.assertEqual(add(3, 8), 11)
        self.assertEqual(add(-2, 0), -2)

    def test_subtract_numbers(self):
        """Should subtract numbers"""
        self.assertEqual(subtract(5, 11), -6)
