import os
from tkinter.filedialog import askopenfilenames

import pandas as pd
import matplotlib.pyplot as plt

from CalibrationTable import CalibrationTable
from rectangle_grid import rectangle_grid
from Cleaner import *


class VirtualDutCreator:
    """
    Данные класс реализует механизм по созданию виртуальных датчиков уровня топлива.
    """

    def __init__(self, path):
        """
        Args:
            path - путь к файлу .xlsx с тарировочной таблицей
        """
        self.calibration_table = CalibrationTable(path)
        self.original_table = self.calibration_table.table.copy()
        self.calibration_table.change_table(Cleaner.transform(self.calibration_table))
        self.virtual_DUTs = []  # (DUT_name, level, start, finish, calibration_subtable)
        self.path = path

    def __create_level_vector(self):
        """
        Returns:
            pd.Series состояний из значений от 0 до (количества уровней виртуальных ДУТов - 1)
        """
        table = self.calibration_table.dut_values
        n_records = len(table)
        level_columns = pd.Series([0] * n_records, index=table.index)
        k = 1
        for device_name in self.calibration_table.get_fuel_level_sensor_names():
            level_columns += k * table[device_name].isna()
            k *= 2
        level_vector = []
        cur_level = level_columns.iloc[0]
        level_number_in_level_vector = 0
        for x in level_columns:
            if x != cur_level:
                level_number_in_level_vector += 1
                cur_level = x
            level_vector.append(level_number_in_level_vector)
        return level_vector

    def __create_levels(self):
        """
        Записывает в levels тарировочные таблицы для виртуальных дутов.
        """
        self.levels = []
        level = self.__create_level_vector()
        groups = [group for _, group in self.calibration_table.table.groupby(level)]

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

    @staticmethod
    def __concat_group_with_records(g, g_last=None, g_first=None):
        """
        Метод приписывает к датафрейму g посленюю запись датафрейма g_last и первую запись датафрейма g_first
        если они были переданы
        """
        empty_df = pd.DataFrame(columns=g.columns)
        last_row = empty_df if g_last is None else g_last.iloc[-1:, :]
        first_row = empty_df if g_first is None else g_first.iloc[:1, :]
        return pd.concat([last_row, g, first_row])

    def __get_new_dir_name(self):
        directory = os.path.dirname(self.path)
        filename = os.path.basename(self.path)
        filename_without_extension = filename.split(".")[0]
        return directory + "/" + filename_without_extension

    def __constuct_fuel_tables(self):
        """
        Выполняет сохранение тарировочных таблиц в csv файлы. Добавляет финализирующие значения для начала и конца
        тарировочной таблицы.
        """
        self.__create_levels()
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

                self.virtual_DUTs.append((
                    dut_value_column,    # DUT_name
                    _level_number,       # level
                    level.LITERS.iloc[0],     # start
                    level.LITERS.iloc[-1],    # finish
                    table                # calibration_subtable
                ))

    def write_fuel_tables(self):

        if not self.virtual_DUTs:
            self.__constuct_fuel_tables()

        new_dir_name = self.__get_new_dir_name()
        create_directory_or_delete_if_exists(new_dir_name)
        create_directory_or_delete_if_exists(new_dir_name + "/wialon")

        for i, (DUT_name, level, _, _, table) in enumerate(self.virtual_DUTs, 1):
            filename = new_dir_name + f"/wialon/FUEL{i}_{DUT_name}_level={level}.csv"
            table.to_csv(filename, sep=";", index=None, header=None)

    def __create_formula_file(self):
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
        return formula

    def write_formula_file(self):
        formula = self.__create_formula_file()
        new_dir_name = self.__get_new_dir_name()
        with open(f"{new_dir_name}/wialon/formula.txt", 'w') as f:
            f.write(formula)

    def create_result_plot(self):
        """
        Выполняет построение графиков и сохраняет и сохраняет в директории с тарировочными таблицами.
        """
        if not self.virtual_DUTs:
            self.__constuct_fuel_tables()
        new_dir_name = self.__get_new_dir_name()

        n_plots = len(self.virtual_DUTs)
        fig, ax = rectangle_grid(n_plots, 3)
        for i, (DUT_name, level, _, _, table) in enumerate(self.virtual_DUTs):
            title = f"FUEL_{i + 1} ({DUT_name})"
            ax[i].set_title(title, fontsize=16)
            ax[i].plot(table.iloc[:, 0], table.LITERS, marker="*")
            ax[i].set_xlabel("DUT_value", fontsize=12)
            ax[i].set_ylabel("LITERS", fontsize=12)
        plt.tight_layout()
        plt.savefig(new_dir_name + '/wialon/plot.png')

    def write_dut_info(self):
        table = self.original_table

        new_dir_name = self.__get_new_dir_name()
        create_directory_or_delete_if_exists(new_dir_name)
        create_directory_or_delete_if_exists(new_dir_name + "/1C")

        for i in range(1, table.shape[1]):
            table.iloc[:, [0, i]].to_csv(new_dir_name + "/1C/" + table.columns[i] + ".csv", sep=";", index=None, header=None)


def create_directory_or_delete_if_exists(dir_path):
    try:
        os.makedirs(dir_path)
    except FileExistsError:
        map(os.remove, [dir_path + '/' + file for file in os.listdir(dir_path)])


if __name__ == "__main__":
    pathes = askopenfilenames()
    for path in pathes:
        print(path)
        try:
            vdc = VirtualDutCreator(path)
            vdc.write_fuel_tables()
            vdc.write_formula_file()
            vdc.create_result_plot()
            vdc.write_dut_info()
        except Exception:
            print(f"Ошибка при обработке файла {path}")