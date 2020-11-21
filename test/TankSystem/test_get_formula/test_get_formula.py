import unittest

from TankSystem import *


class TestGetFormula(unittest.TestCase):

    def test_one_border_1(self):
        path = "files/test_one_border_1.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(ts.get_formula(), '[FUEL_1] + ([FUEL_2] + [FUEL_3]) / 2')