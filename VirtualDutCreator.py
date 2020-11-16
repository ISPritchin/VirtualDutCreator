﻿import os
from tkinter.filedialog import askopenfilenames

import pandas as pd
import matplotlib.pyplot as plt

from Exceptions import *
from rectangle_grid import rectangle_grid


class VirtualDutCreator:
    """
    Данные класс реализует механизм по созданию виртуальных датчиков уровня топлива.
    """

    def __create_levels(self):
        """
        Записывает в levels тарировочные таблицы для виртуальных дутов.
        """
        self.levels = []
        level = self.__create_level_vector()
        groups = [group for _, group in self.table.groupby(level)]

        n_levels = max(level) + 1

        for i in range(n_levels):
            if i == 0:
                before = None
            else:
                before = groups[i - 1]
            if i == n_levels - 1:
                after = None
            else:
                after = groups[i + 1]
            g = vdc.__concat_group_with_records(groups[i], before, after)
            g = g.loc[:, ~g.isna().all(axis=0)]
            g = g.loc[:, g.isna().sum(axis=0) + 1 != len(g)]
            g = g.loc[(~g.isna()).all(axis=1), :]
            self.levels.append(g)

        self.levels = [level for level in self.levels if len(level) > 1]

    @staticmethod
    def __concat_group_with_records(g, g_last=None, g_first=None):
        """
        Метод приписывает к датафрейму g посленюю запись датафрейма g_last и первую запись датафрейма g_first
        если они были переданы
        """
        empty_df = pd.DataFrame(columns=g.columns)
        last_row = g_last.iloc[-1:, :] if g_last is not None else empty_df
        first_row = g_first.iloc[:1, :] if g_first is not None else empty_df
        return pd.concat([last_row, g, first_row])

    def get_new_dir_name(self):
        directory = os.path.dirname(self.path)
        filename = os.path.basename(self.path)
        filename_without_extension = filename.split(".")[0]
        return directory + "/" + filename_without_extension

    def create_fuel_tables(self):
        """
        Выполняет сохранение тарировочных таблиц в csv файлы. Добавляет финализирующие значения для начала и конца
        тарировочной таблицы.
        """
        new_dir_name = self.get_new_dir_name()
        try:
            os.makedirs(new_dir_name)
        except FileExistsError:
            map(os.remove, [new_dir_name + '/' + file for file in os.listdir(new_dir_name)])

        vdc.__create_levels()

        vdut_number = 1
        for _level_number, level in enumerate(self.levels):
            liters = level.LITERS
            # обработка случая, когда ДУТ имеет слепую зону
            if _level_number != 0:
                liters -= liters.values[0]
            for dut_value_column in level.columns[1:]:
                dut_values = level[dut_value_column]
                table = pd.concat([dut_values, liters], axis=1)

                # вставка строки для хорошей апроксимации, если значения будут меньше диапозона дута
                # вставка необходима, если первые два значения в Y в тарировочной табице не 0
                if not (table["LITERS"].iloc[:2] == 0).all():
                    first_row = table.iloc[:1, :].copy()
                    first_row.iloc[0, 0] -= 1
                    table = pd.concat([first_row, table], axis=0)

                # вставка строки для хорошей апроксимации, если значения будут больше диапозона дута
                if table["LITERS"].iloc[-1] != table["LITERS"].iloc[-2]:
                    last_row = table.iloc[-1:, :].copy()
                    last_row.iloc[0, 0] += 1
                    table = pd.concat([table, last_row], axis=0)

                table.astype(int).to_csv(f"{new_dir_name}/FUEL_{vdut_number}_{dut_value_column}.csv", index=False,
                                         header=None, sep=";")
                vdut_number += 1

    def create_formula_file(self):
        """
        Вычисляет формулу для виртуальных дутов. Записывает формулу в тектовый файл.
        """
        formula = ""
        vdc.__create_levels()
        vdut_number = 1
        for level in self.levels:
            n_in_level = len(level.columns[1:])
            if n_in_level == 1:
                formula += f"[FUEL_{vdut_number}] + "
                vdut_number += 1
            elif n_in_level > 1:
                i = 0
                formula += "("
                for i in range(n_in_level - 1):
                    formula += f"[FUEL_{i + vdut_number}] + "
                formula += f"[FUEL_{i + vdut_number + 1}])/{n_in_level} + "
                vdut_number += n_in_level
        formula = formula[:-3]

        new_dir_name = self.get_new_dir_name()
        with open(f"{new_dir_name}/formula.txt", 'w') as f:
            f.write(formula)

    def create_result_plot(self):
        """
        Выполняет построение графиков и сохраняет и сохраняет в директории с тарировочными таблицами.
        """
        new_dir_name = self.get_new_dir_name()
        csv_filenames = list(filter(lambda x: x.endswith(".csv"), os.listdir(new_dir_name)))
        n_plots = len(csv_filenames)
        fig, ax = rectangle_grid(n_plots, 3)
        for i, csv_filename in enumerate(csv_filenames):
            filepath = new_dir_name + '/' + csv_filename
            fuel_info = pd.read_csv(filepath, sep=";", header=None)
            ax[i].set_title(csv_filename, fontsize=16)
            ax[i].plot(fuel_info.iloc[:, 1], fuel_info.iloc[:, 0], marker="*")
            ax[i].set_xlabel("LITERS", fontsize=12)
            ax[i].set_ylabel("DUT_value", fontsize=12)
        plt.tight_layout()
        plt.savefig(new_dir_name + '/' + "plot.png")


if __name__ == "__main__":
    pathes = askopenfilenames()
    for path in pathes:
        print(path)
        try:
            vdc = VirtualDutCreator(path)
            vdc.create_fuel_tables()
            vdc.create_formula_file()
            vdc.create_result_plot()
        except Exception as e:
            print(e)
