from typing import *
import pathlib

import pandas as pd

from Fixer import *
from Exceptions import *


class CalibrationTable:
    """
    Тарировочная таблица
    """

    def __init__(self, path: Union[str, pathlib.Path]):
        self.tables = []
        self.path = path
        try:
            xl = pd.ExcelFile(path)
            n_sheets = len(xl.sheet_names)
            for sheet in range(n_sheets):
                self.tables.append(pd.read_excel(self.path, sheet_name=sheet))
        except OpenFileException:
            print(f"Не удалось выполнить чтение файла {self.path}.")

    def get_stats(self) -> Dict[str, Union[int, List[int]]]:
        """
        Возвращает словарь, с информацией о количестве баков и дутов на основании считанной тарировочной таблицы
        :return:
        """
        return {
            "tanks": len(self.tables),
            "duts": [tank.shape[1] - 1 for tank in self.tables]
        }

    def check_tables(self) -> None:

        def check_table(table: pd.DataFrame) -> None:
            """
            Выполняет проверку на корректность введенных данных и отсутствие ошибок в тарировочной таблице
            """
            for column_name in table:
                column = table[column_name]
                if len(column.dropna()) != len(table):
                    raise EmptyValueException(f"Колонка {column_name} содержит пропущенные значения")

        for table in self.tables:
            check_table(table)
