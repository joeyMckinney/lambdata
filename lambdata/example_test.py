"""
Example tests using standard documentation.
https://docs.python.org/3/library/unittest.html
"""


import unittest
from oop_examples import Bicycle


class TestBicycle(unittest.TestCase):
    """tests the usage of Bicycle"""

    def setUp(self):
        self.bike1 = Bicycle('giant', 'L', 32, 'roady')
        self.bike2 = Bicycle('mongose', 'M', 26, 'BMX')


    def test_brand(self):
        self.assertEqual(self.bike1.brand, 'giant')
        self.assertEqual(self.bike2.brand, 'mongose')


    def test_size(self):
        self.assertEqual(self.bike1.size, 'L')
        self.assertEqual(self.bike2.size, 'M')
        

    def test_tire_size(self):
        self.assertEqual(self.bike1.tire_size, 32)
        self.assertEqual(self.bike2.tire_size, 26)


    def test_frame_type(self):
        self.assertEqual(self.bike1.frame_type, 'roady')
        self.assertEqual(self.bike2.frame_type, 'BMX')


    def test_petaling_fast(self):
        self.assertEqual(self.bike1.petaling_fast(), 'zooming')


    def test_condition(self):
        self.assertEqual(self.bike1.condition('new'), 
        'my bikes condition is new')


if __name__ == '__main__':
    unittest.main()