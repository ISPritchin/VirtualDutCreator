import unittest

from TankSystem import *
from Saver import *

class TestSensorsLevelPlot(unittest.TestCase):

    def test_one_tank_one_dut_1(self):
        filename = "test_one_tank_one_dut_1"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        

    def test_one_tank_one_border_1(self):
        filename = "test_one_tank_one_border_1"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )

    def test_one_tank_one_border_2(self):
        filename = "test_one_tank_one_border_2"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )

    def test_one_tank_one_border_3(self):
        filename = "test_one_tank_one_border_3"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )

    def test_one_tank_two_borders_1(self):
        filename = "test_one_tank_two_borders_1"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )

    def test_one_tank_two_borders_2(self):
        filename = "test_one_tank_two_borders_2"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )

    def test_one_tank_two_borders_3(self):
        filename = "test_one_tank_two_borders_3"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )

    def test_two_tanks_1(self):
        filename = "test_two_tanks_1"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )

    def test_two_tanks_2(self):
        filename = "test_two_tanks_2"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
