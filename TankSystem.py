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
            names = [f"DUT_{i}" for i in range(1, sensors_values.shape[1]+1)]
            fuel_sensors = [FuelLevelSensor(ct[dut_name].values, liters.values, need_clear=True, name=name)
                            for name, dut_name in zip(names, sensors_values)]
            self.tanks.append(Tank(fuel_sensors))

    def __getitem__(self, index) -> Tank:
        return self.tanks[index]

    def get_formula(self):
        formula = ""
        for tank in self.tanks:
            formula += tank.get_formula()
        return formula
