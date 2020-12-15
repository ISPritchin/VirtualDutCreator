import unittest
import os

from TankSystem import *
from Saver import *

class TestSaveVirtualDuts(unittest.TestCase):


    def test_one_tank_one_dut_1(self):
        filename = "test_one_tank_one_dut_1"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        if not os.path.exists("res_files"):
            os.makedirs("res_files")
        if not os.path.exists("res_files/test_one_tank_one_dut_1"):
            os.makedirs("res_files/test_one_tank_one_dut_1")
        Saver(ts).save_virtual_duts(r"res_files/test_one_tank_one_dut_1/")


    def test_one_tank_one_border_1(self):
        filename = "test_one_tank_one_border_1"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        if not os.path.exists("res_files"):
            os.makedirs("res_files")
        if not os.path.exists("res_files/test_one_tank_one_border_1"):
            os.makedirs("res_files/test_one_tank_one_border_1")
        Saver(ts).save_virtual_duts(r"res_files/test_one_tank_one_border_1/")

    def test_one_tank_one_border_2(self):
        filename = "test_one_tank_one_border_2"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        if not os.path.exists("res_files"):
            os.makedirs("res_files")
        if not os.path.exists("res_files/test_one_tank_one_border_2"):
            os.makedirs("res_files/test_one_tank_one_border_2")
        Saver(ts).save_virtual_duts(r"res_files/test_one_tank_one_border_2/")

    def test_one_tank_one_border_3(self):
        filename = "test_one_tank_one_border_3"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        if not os.path.exists("res_files"):
            os.makedirs("res_files")
        if not os.path.exists("res_files/test_one_tank_one_border_3"):
            os.makedirs("res_files/test_one_tank_one_border_3")
        Saver(ts).save_virtual_duts(r"res_files/test_one_tank_one_border_3/")

    def test_one_tank_two_borders_1(self):
        filename = "test_one_tank_two_borders_1"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        if not os.path.exists("res_files"):
            os.makedirs("res_files")
        if not os.path.exists("res_files/test_one_tank_two_borders_1"):
            os.makedirs("res_files/test_one_tank_two_borders_1")
        Saver(ts).save_virtual_duts(r"res_files/test_one_tank_two_borders_1/")

    def test_one_tank_two_borders_2(self):
        filename = "test_one_tank_two_borders_2"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        if not os.path.exists("res_files"):
            os.makedirs("res_files")
        if not os.path.exists("res_files/test_one_tank_two_borders_2"):
            os.makedirs("res_files/test_one_tank_two_borders_2")
        Saver(ts).save_virtual_duts(r"res_files/test_one_tank_two_borders_2/")

    def test_one_tank_two_borders_3(self):
        filename = "test_one_tank_two_borders_3"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        if not os.path.exists("res_files"):
            os.makedirs("res_files")
        if not os.path.exists("res_files/test_one_tank_two_borders_3"):
            os.makedirs("res_files/test_one_tank_two_borders_3")
        Saver(ts).save_virtual_duts(r"res_files/test_one_tank_two_borders_3/")

    def test_two_tanks_1(self):
        filename = "test_two_tanks_1"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        if not os.path.exists("res_files"):
            os.makedirs("res_files")
        if not os.path.exists("res_files/test_two_tanks_1"):
            os.makedirs("res_files/test_two_tanks_1")
        Saver(ts).save_virtual_duts(r"res_files/test_two_tanks_1/")

    def test_two_tanks_2(self):
        filename = "test_two_tanks_2"
        path = f"files/{filename}.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        if not os.path.exists("res_files"):
            os.makedirs("res_files")
        if not os.path.exists("res_files/test_two_tanks_2"):
            os.makedirs("res_files/test_two_tanks_2")
        Saver(ts).save_virtual_duts(r"res_files/test_two_tanks_2/")
