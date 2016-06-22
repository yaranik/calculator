from Calculator import CalculatingPart
import unittest


class TestForCalculatingPart(unittest.TestCase):
    def setUp(self):
        self.Calculatingpart = CalculatingPart()

    def test_sqrt(self):
        self.assertEqual(CalculatingPart.Sqrt(9.0), 3)

    def test_sqared(self):
        self.assertEqual(CalculatingPart.Squared(2), 4)

    def test_swith(self):
        self.assertEqual(CalculatingPart.Switch(2), -2)

    def test_c(self):
        self.assertEqual(CalculatingPart.C(2), " ")

    def test_point(self):
        self.assertEqual(CalculatingPart.PointClicked(2), ".")

    def test_plus(self):
        self.assertEqual(CalculatingPart.Plus(2, 2), 4)

    def test_minus(self):
        self.assertEqual(CalculatingPart.Minus(2, 2), 0)

    def test_umn(self):
        self.assertEqual(CalculatingPart.Umn(2, 2), 4)

    def test_del(self):
        self.assertEqual(CalculatingPart.Del(49, 7), 7)

if __name__ == '__main__':
    unittest.main()
