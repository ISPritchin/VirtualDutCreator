import pandas as pd


class TableSplitter:

    def __init__(self, table: pd.DataFrame):
        self.table = table
        self.virtual_duts_table = []
        self.zone_number = 0
        self.__split()

    def __split(self):
        n = len(self.table)
        i = 0
        while i < n - 1:
            tmp = self.table.iloc[i:i+2][:]
            i += 2
            while i < n:
                row1 = self.table.iloc[i - 1][:]
                row2 = self.table.iloc[i][:]
                change = [i for i in range(1, len(row1)) if row1[i] != row2[i]]
                if not change:
                    break
                tmp = tmp.append(row2)
                i += 1
            self.__update(tmp)
        return self

    def __update(self, tmp):
        self.zone_number += 1
        for dut_name in tmp.columns[1:]:
            if tmp[dut_name].iloc[0] != tmp[dut_name].iloc[-1]:
                d = pd.Series({
                    "V_DUT_NUMBER": len(self.virtual_duts_table) + 1,
                    "PARENT_DUT_NAME": dut_name,
                    "PARENT_LITERS": tmp.LITERS.values,
                    "V_DUT_LITERS": [x - tmp.LITERS.values[0] for x in tmp.LITERS.values],
                    "DUT_VALUES": tmp[dut_name].values,
                    "ZONE_NUMBER": self.zone_number
                })
                self.virtual_duts_table.append(d)

    def split(self):
        return self.virtual_duts_table
