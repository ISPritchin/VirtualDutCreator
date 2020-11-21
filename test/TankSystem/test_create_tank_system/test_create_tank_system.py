import unittest

from TankSystem import *
from CalibrationTable import *


class TestReadCalibrationTable(unittest.TestCase):

    def test_one_dut(self):
        path = "files/one_dut.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(ts[0][0].min_liters_value, 0)
        self.assertEqual(ts[0][0].max_liters_value, 60)

    def test_empty_start(self):
        path = "files/empty_start.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(ts[0][0].min_liters_value, 40)
        self.assertEqual(ts[0][0].max_liters_value, 100)

    def test_empty_end(self):
        path = "files/empty_end.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(ts[0][0].min_liters_value, 0)
        self.assertEqual(ts[0][0].max_liters_value, 60)

    def test_one_dut_empty_start_empty_end(self):
        path = "files/one_dut_empty_start_empty_end.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(ts[0][0].min_liters_value, 30)
        self.assertEqual(ts[0][0].max_liters_value, 60)

    def test_two_dut_empty_start_empty_end(self):
        path = "files/two_duts_with_empty_start_empty_end.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(ts[0][0].min_liters_value, 0)
        self.assertEqual(ts[0][0].max_liters_value, 80)
        self.assertEqual(ts[0][1].min_liters_value, 40)
        self.assertEqual(ts[0][1].max_liters_value, 140)

    def test_one_dut_small_delta_end(self):
        path = "files/small_delta_end.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(ts[0][0].min_liters_value, 40)
        self.assertEqual(ts[0][0].max_liters_value, 80)

    def test_one_dut_small_delta_start(self):
        path = "files/small_delta_start.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(ts[0][0].min_liters_value, 40)
        self.assertEqual(ts[0][0].max_liters_value, 100)
