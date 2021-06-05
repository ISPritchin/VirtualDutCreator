import unittest

import pandas as pd

from TableTransformer import TableTransformer


class Transform(unittest.TestCase):

    def test_1(self):
        df1: pd.DataFrame = pd.read_excel(r"test_TableTransformer_files/test1/1.xlsx")
        df2: pd.DataFrame = pd.read_excel(r"test_TableTransformer_files/test1/2.xlsx")
        df3: pd.DataFrame = TableTransformer(df1).transform()

        pd.testing.assert_frame_equal(df3, df2)

    def test_2(self):
        df1: pd.DataFrame = pd.read_excel(r"test_TableTransformer_files/test2/1.xlsx")
        df2: pd.DataFrame = pd.read_excel(r"test_TableTransformer_files/test2/2.xlsx")
        df3: pd.DataFrame = TableTransformer(df1).transform()

        pd.testing.assert_frame_equal(df3, df2)

    def test_3(self):
        df1: pd.DataFrame = pd.read_excel(r"test_TableTransformer_files/test3/1.xlsx")
        df2: pd.DataFrame = pd.read_excel(r"test_TableTransformer_files/test3/2.xlsx")
        df3: pd.DataFrame = TableTransformer(df1).transform()

        pd.testing.assert_frame_equal(df3, df2)

    def test_4(self):
        df1: pd.DataFrame = pd.read_excel(r"test_TableTransformer_files/test4/1.xlsx")
        df2: pd.DataFrame = pd.read_excel(r"test_TableTransformer_files/test4/2.xlsx")
        df3: pd.DataFrame = TableTransformer(df1).transform()

        pd.testing.assert_frame_equal(df3, df2)

