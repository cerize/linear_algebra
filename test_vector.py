import unittest
from vector import Vector 

class VectorTest(unittest.TestCase):
    def test_minus(self):
        v1 = Vector([4, 4, 4])
        v2 = Vector([1, 2, 3])
        self.assertEqual(v1.minus(v2), Vector([3, 2, 1]))
    
    def test_cross_product(self):
        v1 = Vector([5, 3, -2])
        v2 = Vector([-1, 0, 3])
        result = Vector([9, -13, 3])
        self.assertEqual(v1.cross(v2), result)
