from Tank import *
from FuelLevelSensor import *
from CalibrationTable import *


class TankSystem:
    """Класс, реализующий методы для работы с топливной системой единицы"""

    def __init__(self, calibration_table: CalibrationTable):
        self.tanks = []
        for ct in calibration_table.tables:
            liters = ct["LITERS"]
            sensors_values = ct.drop(columns="LITERS")
            fuel_sensors = [FuelLevelSensor(ct[dut_name].values, liters.values, need_clear=True)
                            for dut_name in sensors_values]
            self.tanks.append(Tank(fuel_sensors))

    def __getitem__(self, index) -> Tank:
        return self.tanks[index]
