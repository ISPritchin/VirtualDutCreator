import unittest

import pandas as pd
import numpy as np

from DataChecker import DataChecker


class CheckLitersColumn(unittest.TestCase):

    @staticmethod
    def test_is_monotonic_increase_0():
        table = pd.DataFrame({
            "LITERS": [0, 1, 2, 3]
        })
        DataChecker(table).check_liters_column()

    def test_is_monotonic_increase_1(self):
        table = pd.DataFrame({
            "LITERS": [0, 2, 2, 3]
        })
        with self.assertRaises(Exception) as context:
            DataChecker(table).check_liters_column()

        self.assertTrue("liters column is not increased (values: [2, 2])" == context.exception.args[0])

    def test_is_monotonic_increase_2(self):
        table = pd.DataFrame({
            "LITERS": [1, 2, 3, 3]
        })
        with self.assertRaises(Exception) as context:
            DataChecker(table).check_liters_column()

        self.assertTrue("liters column is not increased (values: [3, 3])" == context.exception.args[0])

    def test_is_monotonic_increase_3(self):
        table = pd.DataFrame({
            "LITERS": [1, 2, 3, 2]
        })
        with self.assertRaises(Exception) as context:
            DataChecker(table).check_liters_column()

        self.assertTrue("liters column is not increased (values: [3, 2])" == context.exception.args[0])


class CheckDutValues(unittest.TestCase):

    @staticmethod
    def test_is_monotonic_increase_0():
        table = pd.DataFrame({
            "LITERS": [0, 1, 2, 3],
            "DUT_1": [0, 0, 2, 5]
        })
        DataChecker(table).check_dut_values()

    @staticmethod
    def test_is_monotonic_increase_1():
        table = pd.DataFrame({
            "LITERS": [0, 1, 2, 3],
            "DUT_1": [0, 1, 2, 3]
        })
        DataChecker(table).check_dut_values()

    @staticmethod
    def test_is_monotonic_increase_2():
        table = pd.DataFrame({
            "LITERS": [0, 1, 2, 3],
            "DUT_1": [0, 1, 3, 3]
        })
        DataChecker(table).check_dut_values()

    def test_is_monotonic_increase_error_1(self):
        table = pd.DataFrame({
            "LITERS": [0, 1, 2, 3],
            "DUT_1": [2, 1, 2, 3]
        })
        with self.assertRaises(Exception) as context:
            DataChecker(table).check_dut_values()

        self.assertTrue(
            "dut_values column is not increased (dut_values: [2, 1] (liters values: [0, 1]))" == context.exception.args[
                0])

    def test_is_monotonic_increase_error_2(self):
        table = pd.DataFrame({
            "LITERS": [0, 1, 2, 3],
            "DUT_1": [0, 2, 2, 1]
        })
        with self.assertRaises(Exception) as context:
            DataChecker(table).check_dut_values()

        self.assertTrue(
            "dut_values column is not increased (dut_values: [2, 1] (liters values: [2, 3]))" == context.exception.args[
                0])

    def test_is_monotonic_increase_error_3(self):
        table = pd.DataFrame({
            "LITERS": [0, 1, 2, 3, 4],
            "DUT_1": [0, 1, 2, 1, 3]
        })
        with self.assertRaises(Exception) as context:
            DataChecker(table).check_dut_values()

        self.assertTrue(
            "dut_values column is not increased (dut_values: [2, 1] (liters values: [2, 3]))" == context.exception.args[
                0])


class CheckAllDutValues(unittest.TestCase):

    def test_t1(self):
        table = pd.DataFrame({
            "LITERS": [0, 1, 2, 3],
            "DUT_1": [0, 0, 2, 5]
        })
        with self.assertRaises(Exception) as context:
            DataChecker(table).check_all_dut_values()

        self.assertTrue("dut_values columns is equal (liters values: [0, 1]))" == context.exception.args[0])

    def test_t2(self):
        table = pd.DataFrame({
            "LITERS": [0, 1, 2, 3],
            "DUT_1": [0, 0, 2, 5],
            "DUT_2": [0, 0, 2, 5]
        })
        with self.assertRaises(Exception) as context:
            DataChecker(table).check_all_dut_values()

        self.assertTrue("dut_values columns is equal (liters values: [0, 1]))" == context.exception.args[0])

    def test_t3(self):
        table = pd.DataFrame({
            "LITERS": [0, 1, 2, 3],
            "DUT_1": [0, 1, 5, 5],
            "DUT_2": [0, 1, 5, 5]
        })
        with self.assertRaises(Exception) as context:
            DataChecker(table).check_all_dut_values()

        self.assertTrue("dut_values columns is equal (liters values: [2, 3]))" == context.exception.args[0])

    def test_t4(self):
        table = pd.DataFrame({
            "LITERS": [0, 1, 2, 3],
            "DUT_1": [0, 1, 1, 5],
            "DUT_2": [0, 1, 1, 5]
        })
        with self.assertRaises(Exception) as context:
            DataChecker(table).check_all_dut_values()

        self.assertTrue("dut_values columns is equal (liters values: [1, 2]))" == context.exception.args[0])


class CheckTable(unittest.TestCase):

    def test_t1(self):
        table = pd.DataFrame({
            "LITERS": [0, 1, 2, 3],
            "DUT_1": [0, 0, 2, 5]
        })
        with self.assertRaises(Exception) as context:
            DataChecker(table).check_table()

        self.assertTrue("dut_values columns is equal (liters values: [0, 1]))" == context.exception.args[0])

    def test_t2(self):
        table = pd.DataFrame({
            "LITERS": [0, 1, 2, 3],
            "DUT_1": [0, 0, 2, 5],
            "DUT_2": [0, 0, 2, 5]
        })
        with self.assertRaises(Exception) as context:
            DataChecker(table).check_table()

        self.assertTrue("dut_values columns is equal (liters values: [0, 1]))" == context.exception.args[0])


class CheckNa(unittest.TestCase):

    def test_t1(self):
        table = pd.DataFrame({
            "LITERS": [0, 1, 2, 3],
            "DUT_1": [0, 0, 2, np.nan]
        })
        with self.assertRaises(Exception) as context:
            DataChecker(table).check_table()

        self.assertTrue("table has NA" == context.exception.args[0])
