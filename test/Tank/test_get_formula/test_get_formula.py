import unittest

from TankSystem import *


class TestGetFormula(unittest.TestCase):

    def test_one_border_1(self):
        path = "files/test_one_border_1.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(ts[0].get_formula(), '[FUEL_1] + ([FUEL_2] + [FUEL_3]) / 2')

    def test_one_border_2(self):
        path = "files/test_one_border_2.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(ts[0].get_formula(), '([FUEL_1] + [FUEL_2]) / 2 + [FUEL_3]')

    def test_one_border_3(self):
        path = "files/test_one_border_3.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(ts[0].get_formula(), '[FUEL_1] + ([FUEL_2] + [FUEL_3]) / 2')

    def test_one_border_4(self):
        path = "files/test_one_border_4.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(ts[0].get_formula(), '([FUEL_1] + [FUEL_2]) / 2 + [FUEL_3]')

    def test_two_border_1(self):
        path = "files/test_two_border_1.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(ts[0].get_formula(), '[FUEL_1] + ([FUEL_2] + [FUEL_3]) / 2 + [FUEL_4]')

    def test_two_border_2(self):
        path = "files/test_two_border_2.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(ts[0].get_formula(), '[FUEL_1] + [FUEL_2]')

    def test_two_border_3(self):
        path = "files/test_two_border_3.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(ts[0].get_formula(), '[FUEL_1] + ([FUEL_2] + [FUEL_3]) / 2 + [FUEL_4]')

    def test_blind_start_1(self):
        path = "files/test_blind_start_1.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(ts[0].get_formula(), '20 + [FUEL_1] + ([FUEL_2] + [FUEL_3]) / 2')

    def test_blind_start_2(self):
        path = "files/test_blind_start_2.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(ts[0].get_formula(), '20 + ([FUEL_1] + [FUEL_2]) / 2')

    def test_blind_end_1(self):
        path = "files/test_blind_end_1.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(ts[0].get_formula(), '[FUEL_1] + ([FUEL_2] + [FUEL_3]) / 2')

    def test_blind_end_2(self):
        path = "files/test_blind_end_2.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(ts[0].get_formula(), '([FUEL_1] + [FUEL_2]) / 2')
