import re

import pandas as pd

from TankSystem import *


class Saver:

    def __init__(self, ts: TankSystem):
        self.tanks = ts.tanks
        self.formula = ts.formula

    def fuel_sensors_level_plot(self):

        def numerate_dut_numbers():
            for i in range(len(self.tanks)):
                tank = self.tanks[i]
                j = 1
                for k in tank.levels:
                    level = tank.levels[k]
                    for virtual_fuel_sensor in level:
                        virtual_fuel_sensor.dut_number = j
                        j += 1

        c = ["red", "blue", "green", "black"]
        numerate_dut_numbers()
        n_tanks = len(self.tanks)
        fig, axs = rectangle_grid(n_tanks * 2, n_tanks)
        for i in range(len(self.tanks)):
            tank = self.tanks[i]
            for j, fuel_sensor in enumerate(tank.fuel_sensors):
                axs[i].scatter(fuel_sensor.values, fuel_sensor.liters, c=c[i])
                axs[i].plot(fuel_sensor.values, fuel_sensor.liters, c=c[i])
                axs[i + n_tanks].scatter([j + 1] * len(fuel_sensor.liters), fuel_sensor.liters, c=c[i])
                axs[i + n_tanks].plot([j + 1] * len(fuel_sensor.liters), fuel_sensor.liters, c=c[i])
            max_values = max([max(sensor.values) for sensor in tank.fuel_sensors])
            for border in tank.borders:
                axs[i].hlines(border, xmin=0, xmax=max_values, color="black")
                axs[i + n_tanks].hlines(border, xmin=1, xmax=len(tank.fuel_sensors), color="black")
        fig.suptitle(f"Кол-во баков = {len(self.tanks)}. Формула = {self.formula}", size=15, y=0.95)
        # подписи к верхнему графику
        axs[n_tanks].set_ylabel("LITERS")
        for i in range(len(self.tanks)):
            axs[i].set_xlabel("FUEL SENSOR VALUE")
            axs[i].set_ylabel("LITERS")
            tank = self.tanks[i]
            j = 1
            for k in tank.levels:
                level = tank.levels[k]
                for virtual_fuel_sensor in level:
                    low_liters, high_liters = virtual_fuel_sensor.range_fuel_level_sensor_liters
                    low_values, high_values = virtual_fuel_sensor.range_fuel_level_sensor_values
                    x = (low_values + high_values) / 2
                    y = (low_liters + high_liters) / 2
                    axs[i].text(x, y, f"FUEL_{virtual_fuel_sensor.dut_number}")
                    j += 1
        # подписи к нижнему графику
        for i in range(len(self.tanks)):
            tank = self.tanks[i]
            axs[i + n_tanks].set_xlabel("FUEL SENSOR")
            axs[i+n_tanks].set_ylabel("LITERS")
            axs[i+n_tanks].set_xticks([])
            for j, fuel_level_sensor in enumerate(tank.fuel_sensors, 1):
                for virtual_fuel_sensor in tank.virtual_fuel_sensors:
                    if virtual_fuel_sensor.parent_fuel_level_sensor == fuel_level_sensor:
                        low_liters, high_liters = virtual_fuel_sensor.range_fuel_level_sensor_liters
                        x = j
                        y = (low_liters + high_liters) / 2
                        axs[i+n_tanks].text(x, y, f"FUEL_{virtual_fuel_sensor.dut_number}")
        # задание пределов к нижнему графику:
        for i, tank in enumerate(self.tanks):
            n_duts = len(tank.fuel_sensors)
            axs[i+n_tanks].set_xlim(0.5, n_duts+0.5)
        return fig

    def save_fuel_sensors_level_plot(self, path):
        fig = self.fuel_sensors_level_plot()
        fig.savefig(path)

    def get_formula_to_wialon(self):
        formula = self.formula
        xs = [x for x in re.finditer("FUEL_\d+", formula)][::-1]
        i = len(xs)
        for x in xs:
            formula = formula[:x.start()] + f"FUEL_{i}" + formula[x.end():]
            i -= 1
        xs = [x for x in re.finditer(" \d+", formula)][::-1]
        for x in xs:
            formula = formula[:x.start()] + f" const{formula[x.start()+1:x.end()]}" + formula[x.end():]
            i -= 1
        return formula

    def save_virtual_duts(self, dir_path):
        add = 0
        for tank in self.tanks:
            for virtual_fuel_sensor in tank.virtual_fuel_sensors:
                df = pd.DataFrame({
                    "x": virtual_fuel_sensor.values,
                    "y": virtual_fuel_sensor.liters,
                })
                df.to_csv(f"{dir_path}//FUEL_{int(virtual_fuel_sensor.name[-1])+add}.csv", header=False, index=False)
            add += len(tank.virtual_fuel_sensors)