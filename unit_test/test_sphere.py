import unittest
from math import pi
from sphere import sphere_vol

class TestSphereVol(unittest.TestCase):
    def test_vol(self):
        # Test volume calculation when radius >= 0
        self.assertAlmostEqual(sphere_vol(1), 4.0 / 3.0 * pi)
        self.assertAlmostEqual(sphere_vol(0), 0)
        self.assertAlmostEqual(sphere_vol(2.1), 4.0 / 3.0 * pi * 2.1**3)

    def test_values(self):
        # Test value errors of radius
        self.assertRaises(ValueError, sphere_vol, -2)

    def test_types(self):
        # Test type errors of radius
        self.assertRaises(TypeError, sphere_vol, 3 + 5j)
        self.assertRaises(TypeError, sphere_vol, True)
        self.assertRaises(TypeError, sphere_vol, "string")

if __name__ == '__main__':
    print(f'Unit Testing: sphere.py begins...\n')
    unittest.main()
