from django.test import TestCase
from .calc import add,subtract
class CalcTestCase(TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        
    def test_sub(self):   # function must start with test_
        """test subtact"""
        
        res=subtract(12,8)
        
        self.assertEqual(res,4)