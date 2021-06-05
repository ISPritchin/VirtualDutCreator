import pandas as pd


class DataChecker:

    def __init__(self, calibration_table: pd.DataFrame):
        self.calibration_table = calibration_table

    def check_has_na(self):
        if self.calibration_table.isnull().values.any():
            raise Exception(f"table has NA")

    def check_liters_column(self):
        """
        Выполняет проверку первого столбца тарировочной таблицы.
        Если значения не являются возрастающими - генерируется исключение.
        """
        liters = self.calibration_table.LITERS
        is_increase = True
        for i in range(1, len(liters)):
            if liters[i-1] >= liters[i]:
                is_increase = False
                break
        if not is_increase:
            raise Exception(f"liters column is not increased (values: [{liters[i-1]}, {liters[i]}])")

    def check_dut_values(self):
        """
        Выполняет проверку столбцов, отвечающих за показания ДУТов на неубывание.
        Если значения не являются неубывающими - генерируется исключение.
        """
        liters = self.calibration_table.LITERS
        for dut_name in self.calibration_table.columns[1:]:
            dut_values = self.calibration_table[dut_name].values
            is_increase = True
            for i in range(1, len(dut_values)):
                if dut_values[i - 1] > dut_values[i]:
                    is_increase = False
                    break
            if not is_increase:
                raise Exception(f"dut_values column is not increased (dut_values: [{dut_values[i - 1]}, {dut_values[i]}]"
                                f" (liters values: [{liters[i - 1]}, {liters[i]}]))")

    def check_all_dut_values(self):
        """
        Проверяет проверку показаний датчиков на неравенство значений в соседних рядах
        """
        n_duts = len(self.calibration_table.columns) - 1
        n_rows = len(self.calibration_table)
        liters = self.calibration_table.LITERS
        row1 = [-1] * n_duts
        for i in range(n_rows):
            row2 = [self.calibration_table.iloc[i][dut_number] for dut_number in range(1, n_duts + 1)]
            if row1 == row2:
                raise Exception(f"dut_values columns is equal (liters values: [{liters[i - 1]}, {liters[i]}]))")
            row1 = row2

    def check_table(self):
        self.check_has_na()
        self.check_liters_column()
        self.check_dut_values()
        self.check_all_dut_values()