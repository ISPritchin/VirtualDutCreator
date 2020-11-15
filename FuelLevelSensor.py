from typing import *
import pathlib

import pandas as pd


class FuelLevelSensor:

    def __init__(self, values, liters):
        self.liters = liters
        self.values = values
        assert len(self.liters) == len(self.values)
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
        while i < n_observations-1 and self.values.iloc[i+1] - self.values.iloc[i] < min_delta:
            i += 1
        assert i != n_observations-1
        start_index = i

        self.liters = self.liters.iloc[start_index:]
        self.values = self.values.iloc[start_index:]

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
        while i > 0 and self.values.iloc[i] - self.values.iloc[i-1] < min_delta:
            i -= 1
        assert i != 0
        end_index = i + 1

        self.liters = self.liters.iloc[:end_index]
        self.values = self.values.iloc[:end_index]

    @property
    def min_liters_value(self):
        "Минимальный объем топлива, фиксируемый ДУТом"
        return min(self.liters)

    @property
    def max_liters_value(self):
        "Максимальный объем топлива, фиксируемый ДУТом"
        return max(self.liters)

    def save_to_xlsx(self, path: Union[str, pathlib.Path, None] = None ) -> None:
        """
        Выполняет сохранение тарировочной таблицы по пути path
        :return:
        """
        path = self.path if path is None else path
        # todo: сохранение в файл
        table = pd.DataFrame([self.values, self.liters])
        table.to_excel(path, header=True, index=None)