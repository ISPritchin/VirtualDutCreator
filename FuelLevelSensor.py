from typing import *
import pathlib

import pandas as pd


class FuelLevelSensor:

    def __init__(self, values: List[int], liters: List[int], need_clear=False, name=None):
        self.liters = liters
        self.values = values
        assert len(self.liters) == len(self.values)
        if name:
            self.name = name
        if need_clear:
            self.clear_start(5)
            self.clear_end(3)
        assert len(self.liters) == len(self.values)

    def clear_start(self, min_delta) -> None:
        """
        Удаляет с начала тарировки те пары (количество литров; ацп), ацп на которых изменяется меньше чем на min_delta
        в сравнении с прошлым показателем
        :param min_delta:
            минимальный порог ацп
        :return:
        """
        n_observations = len(self.liters)

        i = 0
        while i < n_observations - 1 and self.values[i + 1] - self.values[i] < min_delta:
            i += 1
        assert i != n_observations - 1
        start_index = i

        self.liters = self.liters[start_index:]
        self.values = self.values[start_index:]

    def clear_end(self, min_delta) -> None:
        """
        Удаляет с конца тарировки те пары (количество литров; ацп), ацп на которых изменяется меньше чем на min_delta
        в сравнении с прошлым показателем
        :param min_delta:
            минимальный порог ацп
        :return:
        """
        n_observations = len(self.liters)

        i = n_observations - 1
        while i > 0 and self.values[i] - self.values[i - 1] < min_delta:
            i -= 1
        assert i != 0
        end_index = i + 1

        self.liters = self.liters[:end_index]
        self.values = self.values[:end_index]

    @property
    def min_liters_value(self):
        """Минимальный объем топлива, фиксируемый ДУТом"""
        return min(self.liters)

    @property
    def max_liters_value(self):
        """Максимальный объем топлива, фиксируемый ДУТом"""
        return max(self.liters)

    def save_to_xlsx(self, path: Union[str, pathlib.Path]) -> None:
        """
        Выполняет сохранение тарировочной таблицы по пути path
        :return:
        """
        table = pd.DataFrame([self.values, self.liters])
        table.to_excel(path, header=True, index=None)
