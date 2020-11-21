import unittest
from typing import *

from VirtualFuelLevelSensor import VirtualFuelLevelSensor
from TankSystem import *


class TestGetLevels(unittest.TestCase):

    def eq_configuration(self,
                         levels: Dict[Tuple[int, int], List[VirtualFuelLevelSensor]],
                         expected_levels: Dict[Tuple[int, int], List[VirtualFuelLevelSensor]]):
        for key1, key2 in zip(levels, expected_levels):
            self.assertEqual(key1, key2)
        for key in expected_levels:
            for sensor1, sensor2 in zip(levels[key], expected_levels[key]):
                self.assertListEqual(sensor1.liters, sensor2.liters)
                self.assertListEqual(sensor1.values, sensor2.values)

    def test_one_border_1(self):
        path = "files/test_one_border_1.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        vfls1 = VirtualFuelLevelSensor(
            [30, 50, 70],
            [0, 10, 20],
        )
        vfls2 = VirtualFuelLevelSensor(
            [70, 90, 110, 130],
            [20, 30, 40, 50]
        )
        vfls3 = VirtualFuelLevelSensor(
            [30, 50, 70, 90],
            [20, 30, 40, 50]
        )
        expected_fuel_sensors = {
            (0, 20): [vfls1],
            (20, 50): [vfls2, vfls3]
        }
        self.eq_configuration(ts[0].get_levels(), expected_fuel_sensors)

    def test_one_border_2(self):
        path = "files/test_one_border_2.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        vfls1 = VirtualFuelLevelSensor(
            [30, 50, 70, 90],
            [0, 10, 20, 30],
        )
        vfls2 = VirtualFuelLevelSensor(
            [90, 110, 130],
            [30, 40, 50],
        )
        vfls3 = VirtualFuelLevelSensor(
            [30, 50, 70, 90],
            [0, 10, 20, 30],
        )
        expected_fuel_sensors = {
            (0, 30): [vfls1, vfls3],
            (30, 50): [vfls2]
        }
        self.eq_configuration(ts[0].get_levels(), expected_fuel_sensors)

    def test_one_border_3(self):
        path = "files/test_one_border_3.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        vfls1 = VirtualFuelLevelSensor(
            [30, 50],
            [0, 10],
        )
        vfls2 = VirtualFuelLevelSensor(
            [50, 70, 90, 110, 130],
            [10, 20, 30, 40, 50],
        )
        vfls3 = VirtualFuelLevelSensor(
            [30, 50, 70, 90, 110],
            [10, 20, 30, 40, 50],
        )
        expected_fuel_sensors = {
            (0, 10): [vfls1],
            (10, 50): [vfls2, vfls3]
        }
        self.eq_configuration(ts[0].get_levels(), expected_fuel_sensors)

    def test_one_border_4(self):
        path = "files/test_one_border_4.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        vfls1 = VirtualFuelLevelSensor(
            [30, 50, 70, 90, 110],
            [0, 10, 20, 30, 40],
        )
        vfls2 = VirtualFuelLevelSensor(
            [110, 130],
            [40, 50],
        )
        vfls3 = VirtualFuelLevelSensor(
            [30, 50, 70, 90, 110],
            [0, 10, 20, 30, 40],
        )
        expected_fuel_sensors = {
            (0, 40): [vfls1, vfls3],
            (40, 50): [vfls2]
        }
        self.eq_configuration(ts[0].get_levels(), expected_fuel_sensors)

    def test_two_border_1(self):
        path = "files/test_two_border_1.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        vfls1 = VirtualFuelLevelSensor(
            [30, 110, 130],
            [30, 40, 50],
        )
        vfls2 = VirtualFuelLevelSensor(
            [130, 150, 170, 190],
            [50, 60, 70, 80],
        )
        vfls3 = VirtualFuelLevelSensor(
            [30, 110, 130, 150],
            [0, 10, 20, 30],
        )
        vfls4 = VirtualFuelLevelSensor(
            [150, 170, 190],
            [30, 40, 50],
        )
        expected_fuel_sensors = {
            (0, 30): [vfls3],
            (30, 50): [vfls1, vfls4],
            (50, 80): [vfls2],
        }
        self.eq_configuration(ts[0].get_levels(), expected_fuel_sensors)

    def test_two_border_2(self):
        path = "files/test_two_border_2.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        vfls1 = VirtualFuelLevelSensor(
            [30, 110, 130, 150],
            [0, 10, 20, 30],
        )
        vfls2 = VirtualFuelLevelSensor(
            [30, 110, 130, 150, 170, 190],
            [30, 40, 50, 60, 70, 80],
        )
        expected_fuel_sensors = {
            (0, 30): [vfls1],
            (30, 80): [vfls2],
        }
        self.eq_configuration(ts[0].get_levels(), expected_fuel_sensors)

    def test_two_border_3(self):
        path = "files/test_two_border_3.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        vfls1 = VirtualFuelLevelSensor(
            [30, 50],
            [0, 10],
        )
        vfls2 = VirtualFuelLevelSensor(
            [50, 70, 90, 110],
            [10, 20, 30, 40],
        )
        vfls3 = VirtualFuelLevelSensor(
            [110, 130],
            [40, 50],
        )
        vfls4 = VirtualFuelLevelSensor(
            [30, 50, 70, 90],
            [10, 20, 30, 40],
        )
        expected_fuel_sensors = {
            (0, 10): [vfls1],
            (10, 40): [vfls2, vfls4],
            (40, 50): [vfls3],
        }
        self.eq_configuration(ts[0].get_levels(), expected_fuel_sensors)
