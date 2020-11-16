from typing import *

import pandas as pd

from FuelLevelSensor import *


class Tank:

    def __init__(self, fuel_sensors: List[FuelLevelSensor]):
        self.fuel_sensors = fuel_sensors

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
        return borders[1:-1]

    def get_virtual_fuel_sensors(self) -> List[FuelLevelSensor]:
        """
        Выполняет разбиение физических ДУТов на виртуальные
        :return:
        """

        def create_virtual_fuel_sensor(values, liters):
            min_liters = min(liters)
            liters = list(map(lambda x: x - min_liters, liters))
            # финализация значений в начале
            liters.insert(0, 0)
            values.insert(0, min(values) - 1)
            # финализация значений в конце
            liters.append(max(liters))
            values.append(max(values) + 1)
            return FuelLevelSensor(values, liters)

        borders = self._get_borders()
        virtual_fuel_sensors = []
        for fuel_sensor in self.fuel_sensors:
            liters, values = [], []
            for value, liter in zip(fuel_sensor.values, fuel_sensor.liters):
                liters.append(liter)
                values.append(value)
                if liter in borders and len(liters) > 1:
                    virtual_fuel_sensors.append(create_virtual_fuel_sensor(values, liters))
                    liters = [liter]
                    values = [value]
            if len(liters) > 1:
                virtual_fuel_sensors.append(create_virtual_fuel_sensor(values, liters))
        return virtual_fuel_sensors
