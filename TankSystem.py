from Tank import *
from FuelLevelSensor import *
from CalibrationTable import *
from rectangle_grid import *

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
        self.formula = self.get_formula()

    def __getitem__(self, index) -> Tank:
        return self.tanks[index]

    def get_formula(self):
        formula = ""
        if len(self.tanks) == 1:
            return self.tanks[0].get_formula()
        for tank in self.tanks:
            formula += "( " + tank.get_formula() + " )  +  "
        formula = formula[:-5]
        self.formula = formula
        return formula

    def fuel_sensors_level_plot(self):
        c = ["red", "blue", "green", "black"]
        n_tanks = len(self.tanks)
        fig, axs = rectangle_grid(n_tanks*2, n_tanks)
        for i in range(len(self.tanks)):
            tank = self.tanks[i]
            for j, fuel_sensor in enumerate(tank.fuel_sensors):
                axs[i].scatter(fuel_sensor.values, fuel_sensor.liters, c=c[i])
                axs[i].plot(fuel_sensor.values, fuel_sensor.liters, c=c[i])
                axs[i+n_tanks].scatter([j+1]*len(fuel_sensor.liters), fuel_sensor.liters, c=c[i])
                axs[i+n_tanks].plot([j+1]*len(fuel_sensor.liters), fuel_sensor.liters, c=c[i])
            max_values = max([max(sensor.values) for sensor in tank.fuel_sensors])
            for border in tank.borders:
                axs[i].hlines(border, xmin=0, xmax=max_values, color="black")
                axs[i+n_tanks].hlines(border, xmin=1, xmax=len(tank.fuel_sensors), color="black")
        fig.suptitle(f"Кол-во баков = {len(self.tanks)}. Формула = {self.formula}", size=15, y=0.95)
        for i in range(len(self.tanks)):
            tank = self.tanks[i]
            j = 1
            for k in tank.levels:
                level = tank.levels[k]
                for virtual_fuel_sensor in level:
                    low_liters, high_liters = virtual_fuel_sensor.range_fuel_level_sensor_liters
                    low_values, high_values = virtual_fuel_sensor.range_fuel_level_sensor_values
                    x = (low_values + high_values) / 2
                    y = (low_liters + high_liters) / 2
                    axs[i].text(x, y, f"FUEL_{j}")
                    j += 1
        return fig

    def save_fuel_sensors_level_plot(self, path):
        fig = self.fuel_sensors_level_plot()
        fig.savefig(path)