from typing import *

import pandas as pd

from FuelLevelSensor import *


class Tank:

    def __init__(self, fuel_sensors: List[FuelLevelSensor]):
        self.fuel_sensors = fuel_sensors

    def __getitem__ (self, i) -> FuelLevelSensor:
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
        borders = list(set(sorted(borders)))
        return borders[1:-1]

    def get_virtual_duts(self):
        borders = self._get_borders()


