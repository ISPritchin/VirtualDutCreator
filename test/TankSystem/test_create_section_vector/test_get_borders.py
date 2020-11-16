import unittest

from TaskSystem import *
from CalibrationTable import *


class TestGetBorders(unittest.TestCase):

    def test_one_dut(self):
        path = "files/one_dut.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(ts[0]._get_borders(), [])

    def test_two_duts_conf_1(self):
        path = "files/two_duts-conf_1.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(ts[0]._get_borders(), [40])

    def test_two_duts_conf_2(self):
        path = "files/two_duts-conf_2.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(ts[0]._get_borders(), [40])

    def test_two_duts_conf_3(self):
        path = "files/two_duts-conf_3.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        self.assertEqual(ts[0]._get_borders(), [])
