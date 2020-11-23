from typing import *

from FuelLevelSensor import FuelLevelSensor


class VirtualFuelLevelSensor:
    "Класс для реализации работы с виртуальными ДУТами"

    def __init__(self,
                 values: List[int],
                 liters: List[int],
                 parent_fuel_level_sensor: Union[FuelLevelSensor, None] = None):
        self.range_fuel_level_sensor_liters = (min(liters), max(liters))
        self.range_fuel_level_sensor_values = (min(values), max(values))

        min_liters = min(liters)
        liters = list(map(lambda x: x - min_liters, liters))
        # финализация значений в начале
        liters.insert(0, 0)
        values.insert(0, min(values) - 1)
        # финализация значений в конце

        liters.append(max(liters))
        values.append(max(values) + 1)
        self.liters = liters
        self.values = values
        assert len(self.liters) == len(self.values)
        self.parent_fuel_level_sensor = parent_fuel_level_sensor
