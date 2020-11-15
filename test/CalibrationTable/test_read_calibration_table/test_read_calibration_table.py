import unittest

from CalibrationTable import *
from Exceptions import EmptyValueException


class TestReadCalibrationTable(unittest.TestCase):

    def test_one_dut_one_tank(self):
        ct = CalibrationTable("files/one_dut_one_tank.xlsx")
        self.assertDictEqual(
            ct.get_stats(),
            {
                "tanks": 1,
                "duts": [1],
            }
        )

    def test_two_dut_one_tank(self):
        ct = CalibrationTable("files/two_dut_one_tank.xlsx")
        self.assertDictEqual(
            ct.get_stats(),
            {
                "tanks": 1,
                "duts": [2],
            }
        )

    def test_two_dut_two_tank(self):
        ct = CalibrationTable("files/two_dut_two_tank.xlsx")
        self.assertDictEqual(
            ct.get_stats(),
            {
                "tanks": 2,
                "duts": [1, 1],
            }
        )

    def test_three_dut_two_tank(self):
        ct = CalibrationTable("files/three_dut_two_tank.xlsx")
        self.assertDictEqual(
            ct.get_stats(),
            {
                "tanks": 2,
                "duts": [2, 1],
            }
        )

    def test_calibration_table_with_empty_value(self):
        ct = CalibrationTable("files/table_with_na.xlsx")
        with self.assertRaises(EmptyValueException):
            ct.check_tables()