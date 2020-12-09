from django.test import TestCase

from app.calc import add, subtract


class TestCalc(TestCase):

    def test_add_numbers(self):
        """Test add function"""
        self.assertEqual(add(4, 5), 9)

    def test_subtract_numbers(self):
        """Test subtract function"""
        self.assertEqual(subtract(5, 11), 6)
