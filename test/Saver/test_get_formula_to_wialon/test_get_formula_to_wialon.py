import unittest

from TankSystem import *
from Saver import *

class TestGetFormulaToWialon(unittest.TestCase):

    def test_one_tank_one_dut_1(self):
        filename = "test_one_tank_one_dut_1"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(Saver(ts).get_formula_to_wialon(), "[FUEL_1]")


    def test_one_tank_one_border_1(self):
        filename = "test_one_tank_one_border_1"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(Saver(ts).get_formula_to_wialon(), "[FUEL_1] + ([FUEL_2] + [FUEL_3]) / const2")

    def test_one_tank_one_border_2(self):
        filename = "test_one_tank_one_border_2"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(Saver(ts).get_formula_to_wialon(), "([FUEL_1] + [FUEL_2]) / const2 + [FUEL_3]")

    def test_one_tank_one_border_3(self):
        filename = "test_one_tank_one_border_3"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(Saver(ts).get_formula_to_wialon(), "[FUEL_1] + ([FUEL_2] + [FUEL_3]) / const2")

    def test_one_tank_two_borders_1(self):
        filename = "test_one_tank_two_borders_1"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(Saver(ts).get_formula_to_wialon(), "[FUEL_1] + ([FUEL_2] + [FUEL_3]) / const2 + [FUEL_4]")

    def test_one_tank_two_borders_2(self):
        filename = "test_one_tank_two_borders_2"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(Saver(ts).get_formula_to_wialon(), "[FUEL_1] + [FUEL_2]")

    def test_one_tank_two_borders_3(self):
        filename = "test_one_tank_two_borders_3"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(Saver(ts).get_formula_to_wialon(), "[FUEL_1] + ([FUEL_2] + [FUEL_3]) / const2 + [FUEL_4]")

    def test_two_tanks_1(self):
        filename = "test_two_tanks_1"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(Saver(ts).get_formula_to_wialon(), "( ([FUEL_1] + [FUEL_2]) / const2 + [FUEL_3] )  +  ( [FUEL_4] + ([FUEL_5] + [FUEL_6]) / const2 )")

    def test_two_tanks_2(self):
        filename = "test_two_tanks_2"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(Saver(ts).get_formula_to_wialon(), "( [FUEL_1] + ([FUEL_2] + [FUEL_3]) / const2 )  +  ( ([FUEL_4] + [FUEL_5]) / const2 + [FUEL_6] )")
