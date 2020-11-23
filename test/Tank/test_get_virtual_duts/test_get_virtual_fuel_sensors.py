import unittest

from CalibrationTable import *
from TankSystem import *


class TestGetVirtualFuelSensors(unittest.TestCase):

    def eq(self, fuel_sensors, expected_fuel_sensors):
        for i, (fuel_sensor, expected_fuel_sensor) in enumerate(zip(fuel_sensors, expected_fuel_sensors)):
            self.assertListEqual(fuel_sensor.liters, expected_fuel_sensor.liters,
                                 msg=f"ошибка в показании литров на {i + 1}-ом виртуальном ДУТе")
            self.assertListEqual(expected_fuel_sensor.values, expected_fuel_sensor.values,
                                 msg=f"ошибка показании значений на {i + 1}-ом виртуальном ДУТе")

    def test_one_border_1(self):
        path = "files/test_one_border_1.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        fuel_sensors = ts[0].get_virtual_fuel_sensors()
        expected_fuel_sensors = [
            VirtualFuelLevelSensor(
                [30, 50, 70],
                [0, 10, 20],
            ),
            VirtualFuelLevelSensor(
                [70, 90, 110, 130],
                [20, 30, 40, 50]
            ),
            VirtualFuelLevelSensor(
                [30, 50, 70, 90],
                [20, 30, 40, 50]
            )
        ]
        self.eq(fuel_sensors, expected_fuel_sensors)

    def test_one_border_2(self):
        path = "files/test_one_border_2.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        fuel_sensors = ts[0].get_virtual_fuel_sensors()
        expected_fuel_sensors = [
            VirtualFuelLevelSensor(
                [30, 50, 70, 90],
                [0, 10, 20, 30],
            ),
            VirtualFuelLevelSensor(
                [90, 110, 130],
                [30, 40, 50],
            ),
            VirtualFuelLevelSensor(
                [30, 50, 70, 90],
                [0, 10, 20, 30],
            )
        ]
        self.eq(fuel_sensors, expected_fuel_sensors)

    def test_one_border_3(self):
        path = "files/test_one_border_3.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        fuel_sensors = ts[0].get_virtual_fuel_sensors()
        expected_fuel_sensors = [
            VirtualFuelLevelSensor(
                [30, 50],
                [0, 10],
            ),
            VirtualFuelLevelSensor(
                [50, 70, 90, 110, 130],
                [10, 20, 30, 40, 50],
            ),
            VirtualFuelLevelSensor(
                [30, 50, 70, 90, 110],
                [10, 20, 30, 40, 50],
            )
        ]
        self.eq(fuel_sensors, expected_fuel_sensors)

    def test_one_border_4(self):
        path = "files/test_one_border_4.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        fuel_sensors = ts[0].get_virtual_fuel_sensors()
        expected_fuel_sensors = [
            VirtualFuelLevelSensor(
                [30, 50, 70, 90, 110],
                [0, 10, 20, 30, 40],
            ),
            VirtualFuelLevelSensor(
                [110, 130],
                [40, 50],
            ),
            VirtualFuelLevelSensor(
                [30, 50, 70, 90, 110],
                [0, 10, 20, 30, 40],
            )
        ]
        self.eq(fuel_sensors, expected_fuel_sensors)

    def test_two_border_1(self):
        path = "files/test_two_border_1.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        fuel_sensors = ts[0].get_virtual_fuel_sensors()
        expected_fuel_sensors = [
            VirtualFuelLevelSensor(
                [30, 110, 130],
                [30, 40, 50],
            ),
            VirtualFuelLevelSensor(
                [130, 150, 170, 190],
                [50, 60, 70, 80],
            ),
            VirtualFuelLevelSensor(
                [30, 110, 130, 150],
                [0, 10, 20, 30],
            ),
            VirtualFuelLevelSensor(
                [150, 170, 190],
                [30, 40, 50],
            )
        ]
        self.eq(fuel_sensors, expected_fuel_sensors)

    def test_two_border_2(self):
        path = "files/test_two_border_2.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        fuel_sensors = ts[0].get_virtual_fuel_sensors()
        expected_fuel_sensors = [
            VirtualFuelLevelSensor(
                [30, 110, 130, 150],
                [0, 10, 20, 30],
            ),
            VirtualFuelLevelSensor(
                [30, 110, 130],
                [30, 40, 50],
            )
        ]
        self.eq(fuel_sensors, expected_fuel_sensors)

    def test_two_border_3(self):
        path = "files/test_two_border_3.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        fuel_sensors = ts[0].get_virtual_fuel_sensors()
        expected_fuel_sensors = [
            VirtualFuelLevelSensor(
                [30, 50],
                [0, 10],
            ),
            VirtualFuelLevelSensor(
                [50, 70, 90, 110],
                [10, 20, 30, 40],
            ),
            VirtualFuelLevelSensor(
                [110, 130],
                [40, 50],
            ),
            VirtualFuelLevelSensor(
                [30, 50, 70, 90],
                [10, 20, 30, 40],
            )
        ]
        self.eq(fuel_sensors, expected_fuel_sensors)

    def test_blind_start_1(self):
        path = "files/test_blind_start_1.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        fuel_sensors = ts[0].get_virtual_fuel_sensors()
        expected_fuel_sensors = [
            VirtualFuelLevelSensor(
                [30, 50, 70],
                [20, 30, 40],
            ),
            VirtualFuelLevelSensor(
                [70, 90, 110, 130],
                [40, 50, 60, 70],
            ),
            VirtualFuelLevelSensor(
                [30, 50, 70, 90],
                [40, 50, 60, 70],
            ),
        ]
        self.eq(fuel_sensors, expected_fuel_sensors)

    def test_blind_start_2(self):
        path = "files/test_blind_start_2.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        fuel_sensors = ts[0].get_virtual_fuel_sensors()
        expected_fuel_sensors = [
            VirtualFuelLevelSensor(
                [30, 50, 70, 90, 110, 130],
                [20, 30, 40, 50, 60, 70],
            ),
            VirtualFuelLevelSensor(
                [30, 50, 70, 90, 110, 130],
                [20, 30, 40, 50, 60, 70],
            )
        ]
        self.eq(fuel_sensors, expected_fuel_sensors)

    def test_blind_end_1(self):
        path = "files/test_blind_end_1.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        fuel_sensors = ts[0].get_virtual_fuel_sensors()
        expected_fuel_sensors = [
            VirtualFuelLevelSensor(
                [30, 50, 70],
                [0, 10, 20],
            ),
            VirtualFuelLevelSensor(
                [70, 90, 110, 130],
                [20, 30, 40, 50],
            ),
            VirtualFuelLevelSensor(
                [30, 50, 70, 90],
                [20, 30, 40, 50],
            ),
        ]
        self.eq(fuel_sensors, expected_fuel_sensors)

    def test_blind_end_2(self):
        path = "files/test_blind_end_2.xlsx"
        ts = TankSystem(
            CalibrationTable(path)
        )
        fuel_sensors = ts[0].get_virtual_fuel_sensors()
        expected_fuel_sensors = [
            VirtualFuelLevelSensor(
                [30, 50, 70, 90],
                [0, 10, 20, 30],
            ),
            VirtualFuelLevelSensor(
                [30, 50, 70, 130],
                [0, 10, 20, 30],
            )
        ]
        self.eq(fuel_sensors, expected_fuel_sensors)
