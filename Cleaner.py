import numpy as np


class Cleaner:

    @staticmethod
    def transform(calibration_table):
        table = calibration_table.tables
        for i, col in enumerate(table.columns[1:], 1):
            table[col] = Cleaner.clean_series(table[col])
        return table.loc[~table.isna().iloc[:, 1:].all(axis=1), :]

    @staticmethod
    def clean_series(s):
        s = Cleaner.clean_start_series(s)
        s = Cleaner.clean_finish_series(s)
        return s

    @staticmethod
    def clean_finish_series(s):
        for i in range(len(s)-1, 0, -1):
            if s[i] == s[i - 1]:
                s[i] = np.nan
            else:
                break
        return s

    @staticmethod
    def clean_start_series(s):
        # todo возможно начало булет не с 30
        if s[0] != 30:
            raise Exception("Показания ДУТ не начинаются с 30")
        for i in range(1, len(s)):
            if s[i] - s[i - 1] <= 2:
                s[i - 1] = np.nan
            else:
                break
        return s
