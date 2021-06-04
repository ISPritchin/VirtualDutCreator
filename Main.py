import os
from tkinter import filedialog

import pandas as pd

from FuelSystemConfigCreator import FuelSystemConfigCreator
from Plotter import Plotter
from FormulaCreator import FormulaCreator


def process(path=None, save_path=None):
    if path is None:
        path = filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])
        save_path = ".".join(path.split(".")[:-1]) + "/"

    os.makedirs(save_path, exist_ok=True)
    fsc = FuelSystemConfigCreator(path).create()
    fc = FormulaCreator(fsc)

    for tank_name in fsc:
        os.makedirs(save_path + r"/" + tank_name, exist_ok=True)
        for virtual_dut in fsc[tank_name]["virtual_duts_table"]:
            liters = list(virtual_dut.V_DUT_LITERS)
            liters = [liters[0]] + liters + [liters[-1]]
            dut_values = list(virtual_dut.DUT_VALUES)
            dut_values = [dut_values[0] - 1] + dut_values + [dut_values[-1] + 1]
            df = pd.DataFrame({
                "values": dut_values,
                "liters": liters,

            })
            with open(save_path + r"/" + tank_name + r"/wialon formula.txt", "w") as f:
                f.write(fc.wialon_formula[tank_name])
            df.to_csv(save_path + r"/" + tank_name + f"//V{virtual_dut.V_DUT_NUMBER}.csv",
                      sep=";", header=False, index=False)

    Plotter().get_fx(fsc, fc.latex_formula_full, save_path=save_path)


if __name__ == "__main__":
    process()
