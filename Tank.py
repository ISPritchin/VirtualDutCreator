from typing import *

import pandas as pd

from FuelLevelSensor import *
from VirtualFuelLevelSensor import *


class Tank:

    def __init__(self, fuel_sensors: List[FuelLevelSensor]):
        self.fuel_sensors = fuel_sensors
        self.min_sensitivity_level = min(map(lambda fs: min(fs.liters), fuel_sensors))
        self.max_sensitivity_level = max(map(lambda fs: max(fs.liters), fuel_sensors))
        self.borders = None
        self.virtual_fuel_sensors = None
        self.levels = None
        self.formula = None

    def __getitem__(self, i) -> FuelLevelSensor:
        return self.fuel_sensors[i]

    def _get_borders(self):
        """
        Производит разбиение баков на секции
        Returns:
            pd.Series состояний из значений от 0 до (количества уровней виртуальных ДУТов - 1)
        """
        borders = []
        for fuel_sensor in self.fuel_sensors:
            borders.append(fuel_sensor.min_liters_value)
            borders.append(fuel_sensor.max_liters_value)
        borders = sorted(list(set(borders)))
        self.borders = borders[1:-1]
        return self.borders

    def get_virtual_fuel_sensors(self) -> List[VirtualFuelLevelSensor]:
        """
        Выполняет разбиение физических ДУТов на виртуальные
        :return:
        """

        borders = self._get_borders() if self.borders is None else self.borders
        virtual_fuel_sensors = []
        for fuel_sensor in self.fuel_sensors:
            liters, values = [], []
            for value, liter in zip(fuel_sensor.values, fuel_sensor.liters):
                liters.append(liter)
                values.append(value)
                if liter in borders and len(liters) > 1:
                    virtual_fuel_sensors.append(VirtualFuelLevelSensor(values, liters, fuel_sensor))
                    liters = [liter]
                    values = [value]
            if len(liters) > 1:
                virtual_fuel_sensors.append(VirtualFuelLevelSensor(values, liters, fuel_sensor))

        self.virtual_fuel_sensors = virtual_fuel_sensors
        return self.virtual_fuel_sensors

    def get_levels(self):
        self.virtual_fuel_sensors = self.get_virtual_fuel_sensors() \
            if self.virtual_fuel_sensors is None else self.virtual_fuel_sensors

        points = self.borders + [self.min_sensitivity_level, self.max_sensitivity_level]
        points.sort()
        levels = {(low, high): [] for low, high in zip(points[:-1], points[1:])}

        for virtual_fuel_sensor in self.virtual_fuel_sensors:
            avg_liters = sum(virtual_fuel_sensor.range_fuel_level_sensor_liters) / 2
            for i, (low, high) in enumerate(levels.keys()):
                if low < avg_liters < high:
                    levels[(low, high)].append(virtual_fuel_sensor)
                    break
            else:
                raise Exception()
        self.levels = levels
        return levels

    def get_formula(self):
        self.levels = self.get_levels() if self.levels is None else self.levels
        min_level = self.min_sensitivity_level
        formula = "" if min_level == 0 else f"{min_level} + "
        fuel_number = 1
        for level in self.levels:
            sensors = self.levels[level]
            if len(sensors) > 1:
                formula += "("
            for sensor in sensors:
                formula += f"[FUEL_{fuel_number}] + "
                fuel_number += 1
            if len(sensors) > 1:
                formula += f") / {len(sensors)} + "
        formula = formula.replace(" + )", ")")
        if formula[-3:] == " + ":
            formula = formula[:-3]
        self.formula = formula
        return formula
