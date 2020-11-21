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
            FuelLevelSensor(
                [29, 30, 50, 70, 71],
                [0, 0, 10, 20, 20],
            ),
            FuelLevelSensor(
                [69, 70, 90, 110, 130, 131],
                [0, 0, 10, 20, 30, 30]
            ),
            FuelLevelSensor(
                [29, 30, 50, 70, 90, 91],
                [0, 0, 10, 20, 30, 30]
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
            FuelLevelSensor(
                [29, 30, 50, 70, 90, 91],
                [0, 0, 10, 20, 30, 30],
            ),
            FuelLevelSensor(
                [89, 90, 110, 130, 130],
                [0, 0, 10, 20, 20],
            ),
            FuelLevelSensor(
                [29, 30, 50, 70, 90, 91],
                [0, 0, 10, 20, 30, 30],
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
            FuelLevelSensor(
                [29, 30, 50, 51],
                [0, 0, 10, 10],
            ),
            FuelLevelSensor(
                [49, 50, 70, 90, 110, 130, 131],
                [0, 0, 10, 20, 30, 40, 40],
            ),
            FuelLevelSensor(
                [29, 30, 50, 70, 90, 110, 111],
                [0, 0, 10, 20, 30, 40, 40],
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
            FuelLevelSensor(
                [29, 30, 50, 70, 90, 110, 111],
                [0, 0, 10, 20, 30, 40, 40],
            ),
            FuelLevelSensor(
                [109, 110, 130, 131],
                [0, 0, 10, 10],
            ),
            FuelLevelSensor(
                [29, 30, 50, 70, 90, 110, 111],
                [0, 0, 10, 20, 30, 40, 40],
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
            FuelLevelSensor(
                [29, 30, 110, 130, 131],
                [0, 0, 10, 20, 20],
            ),
            FuelLevelSensor(
                [129, 130, 150, 170, 190, 191],
                [0, 0, 10, 20, 30, 30],
            ),
            FuelLevelSensor(
                [29, 30, 110, 130, 150, 151],
                [0, 0, 10, 20, 30, 30],
            ),
            FuelLevelSensor(
                [149, 150, 170, 190, 191],
                [0, 0, 10, 20, 20],
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
            FuelLevelSensor(
                [29, 30, 110, 130, 150, 151],
                [0, 0, 10, 20, 30, 30],
            ),
            FuelLevelSensor(
                [29, 30, 110, 130, 150, 170, 190, 191],
                [0, 0, 10, 20, 30, 40, 50, 50],
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
            FuelLevelSensor(
                [29, 30, 50, 51],
                [0, 0, 10, 10],
            ),
            FuelLevelSensor(
                [49, 50, 70, 90, 110, 111],
                [0, 0, 10, 20, 30, 30],
            ),
            FuelLevelSensor(
                [109, 110, 130, 131],
                [0, 0, 10, 10],
            ),
            FuelLevelSensor(
                [29, 30, 50, 70, 90, 90],
                [0, 0, 10, 20, 30, 30],
            )
        ]
        self.eq(fuel_sensors, expected_fuel_sensors)
