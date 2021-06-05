import pandas as pd


class TableTransformer:

    def __init__(self, pd_df: pd.DataFrame):
        self.table = pd_df

    def transform(self):
        res_table = [self.table.iloc[0]]
        for i in range(1, self.table.shape[0] - 1):
            row0 = self.table.iloc[i - 1]
            row1 = self.table.iloc[i]
            row2 = self.table.iloc[i + 1]
            s1 = [i for i in range(1, len(row1)) if row0[i] != row1[i]]
            s2 = [i for i in range(1, len(row2)) if row1[i] != row2[i]]
            if s1 == s2:
                res_table.append(self.table.iloc[i])
            else:
                res_table.append(self.table.iloc[i])
                res_table.append(self.table.iloc[i])
        last_row_res = res_table[-1]
        last_row_table = self.table.iloc[-1, :]
        if any(last_row_res != last_row_table):
            res_table.append(last_row_table)

        res_table = pd.DataFrame(res_table)
        res_table.index = range(res_table.shape[0])

        return res_table
