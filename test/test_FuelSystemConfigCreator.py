import unittest

import pandas as pd

from FuelSystemConfigCreator import FuelSystemConfigCreator

class OneDUT(unittest.TestCase):

    def test_1_normal(self):
        FSC = FuelSystemConfigCreator(r"configurations/OneDUT/test1.xlsx").create()
        vduts = FSC["Tank1"]["virtual_duts_table"]
        expected = [
            pd.Series({
                "V_DUT_NUMBER": 1,
                "PARENT_DUT_NAME": "DUT",
                "PARENT_LITERS": [0, 10, 20, 30],
                "V_DUT_LITERS": [0, 10, 20, 30],
                "DUT_VALUES": [30, 200, 500, 770],
                "ZONE_NUMBER": 1
            })
        ]
        pd.testing.assert_series_equal(vduts[0], expected[0])

    def test_2_empty_full(self):
        FSC = FuelSystemConfigCreator(r"configurations/OneDUT/test2.xlsx").create()
        vduts = FSC["Tank1"]["virtual_duts_table"]
        expected = [
            pd.Series({
                "V_DUT_NUMBER": 1,
                "PARENT_DUT_NAME": "DUT",
                "PARENT_LITERS": [0, 500],
                "V_DUT_LITERS": [0, 500],
                "DUT_VALUES": [30, 1547],
                "ZONE_NUMBER": 1
            })
        ]
        pd.testing.assert_series_equal(vduts[0], expected[0])


class TwoDUTs(unittest.TestCase):

    def test_0(self):
        FSC = FuelSystemConfigCreator(r"configurations/TwoDUTs/test0.xlsx").create()
        vduts = FSC["Tank1"]["virtual_duts_table"]
        expected = [
            pd.Series({
                "V_DUT_NUMBER": 1,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [0, 10, 20, 30, 40],
                "V_DUT_LITERS": [0, 10, 20, 30, 40],
                "DUT_VALUES": [0, 100, 200, 300, 400],
                "ZONE_NUMBER": 1
            }),
            pd.Series({
                "V_DUT_NUMBER": 2,
                "PARENT_DUT_NAME": "D2",
                "PARENT_LITERS": [0, 10, 20, 30, 40],
                "V_DUT_LITERS": [0, 10, 20, 30, 40],
                "DUT_VALUES": [0, 100, 200, 300, 400],
                "ZONE_NUMBER": 1
            })
        ]
        for dut_number in range(len(expected)):
            pd.testing.assert_series_equal(vduts[dut_number], expected[dut_number])

    def test_1(self):
        FSC = FuelSystemConfigCreator(r"configurations/TwoDUTs/test1.xlsx").create()
        vduts = FSC["Tank1"]["virtual_duts_table"]
        expected = [
            pd.Series({
                "V_DUT_NUMBER": 1,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [0, 10, 20, 30],
                "V_DUT_LITERS": [0, 10, 20, 30],
                "DUT_VALUES": [0, 100, 200, 300],
                "ZONE_NUMBER": 1
            }),
            pd.Series({
                "V_DUT_NUMBER": 2,
                "PARENT_DUT_NAME": "D2",
                "PARENT_LITERS": [0, 10, 20, 30],
                "V_DUT_LITERS": [0, 10, 20, 30],
                "DUT_VALUES": [0, 100, 200, 300],
                "ZONE_NUMBER": 1
            }),
            pd.Series({
                "V_DUT_NUMBER": 3,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [30, 40],
                "V_DUT_LITERS": [0, 10],
                "DUT_VALUES": [300, 400],
                "ZONE_NUMBER": 2
            })
        ]
        for dut_number in range(len(expected)):
            pd.testing.assert_series_equal(vduts[dut_number], expected[dut_number])

    def test_2(self):
        FSC = FuelSystemConfigCreator(r"configurations/TwoDUTs/test2.xlsx").create()
        vduts = FSC["Tank1"]["virtual_duts_table"]
        expected = [
            pd.Series({
                "V_DUT_NUMBER": 1,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [0, 10, 20],
                "V_DUT_LITERS": [0, 10, 20],
                "DUT_VALUES": [0, 100, 200],
                "ZONE_NUMBER": 1
            }),
            pd.Series({
                "V_DUT_NUMBER": 2,
                "PARENT_DUT_NAME": "D2",
                "PARENT_LITERS": [0, 10, 20],
                "V_DUT_LITERS": [0, 10, 20],
                "DUT_VALUES": [0, 100, 200],
                "ZONE_NUMBER": 1
            }),
            pd.Series({
                "V_DUT_NUMBER": 3,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [20, 30, 40],
                "V_DUT_LITERS": [0, 10, 20],
                "DUT_VALUES": [200, 300, 400],
                "ZONE_NUMBER": 2
            })
        ]
        for dut_number in range(len(expected)):
            pd.testing.assert_series_equal(vduts[dut_number], expected[dut_number])

    def test_3(self):
        FSC = FuelSystemConfigCreator(r"configurations/TwoDUTs/test3.xlsx").create()
        vduts = FSC["Tank1"]["virtual_duts_table"]
        expected = [
            pd.Series({
                "V_DUT_NUMBER": 1,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [0, 10],
                "V_DUT_LITERS": [0, 10],
                "DUT_VALUES": [0, 100],
                "ZONE_NUMBER": 1
            }),
            pd.Series({
                "V_DUT_NUMBER": 2,
                "PARENT_DUT_NAME": "D2",
                "PARENT_LITERS": [0, 10],
                "V_DUT_LITERS": [0, 10],
                "DUT_VALUES": [0, 100],
                "ZONE_NUMBER": 1
            }),
            pd.Series({
                "V_DUT_NUMBER": 3,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [10, 20, 30, 40],
                "V_DUT_LITERS": [0, 10, 20, 30],
                "DUT_VALUES": [100, 200, 300, 400],
                "ZONE_NUMBER": 2
            })
        ]
        for dut_number in range(len(expected)):
            pd.testing.assert_series_equal(vduts[dut_number], expected[dut_number])

    def test_4(self):
        FSC = FuelSystemConfigCreator(r"configurations/TwoDUTs/test4.xlsx").create()
        vduts = FSC["Tank1"]["virtual_duts_table"]
        expected = [
            pd.Series({
                "V_DUT_NUMBER": 1,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [0, 10],
                "V_DUT_LITERS": [0, 10],
                "DUT_VALUES": [0, 100],
                "ZONE_NUMBER": 1
            }),
            pd.Series({
                "V_DUT_NUMBER": 2,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [10, 20, 30, 40],
                "V_DUT_LITERS": [0, 10, 20, 30],
                "DUT_VALUES": [100, 200, 300, 400],
                "ZONE_NUMBER": 2
            }),
            pd.Series({
                "V_DUT_NUMBER": 3,
                "PARENT_DUT_NAME": "D2",
                "PARENT_LITERS": [10, 20, 30, 40],
                "V_DUT_LITERS": [0, 10, 20, 30],
                "DUT_VALUES": [0, 100, 200, 300],
                "ZONE_NUMBER": 2
            })
        ]
        for dut_number in range(len(expected)):
            pd.testing.assert_series_equal(vduts[dut_number], expected[dut_number])

    def test_5(self):
        FSC = FuelSystemConfigCreator(r"configurations/TwoDUTs/test5.xlsx").create()
        vduts = FSC["Tank1"]["virtual_duts_table"]
        expected = [
            pd.Series({
                "V_DUT_NUMBER": 1,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [0, 10, 20],
                "V_DUT_LITERS": [0, 10, 20],
                "DUT_VALUES": [0, 100, 200],
                "ZONE_NUMBER": 1
            }),
            pd.Series({
                "V_DUT_NUMBER": 2,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [20, 30, 40],
                "V_DUT_LITERS": [0, 10, 20],
                "DUT_VALUES": [200, 300, 400],
                "ZONE_NUMBER": 2
            }),
            pd.Series({
                "V_DUT_NUMBER": 3,
                "PARENT_DUT_NAME": "D2",
                "PARENT_LITERS": [20, 30, 40],
                "V_DUT_LITERS": [0, 10, 20],
                "DUT_VALUES": [0, 100, 200],
                "ZONE_NUMBER": 2
            })
        ]
        for dut_number in range(len(expected)):
            pd.testing.assert_series_equal(vduts[dut_number], expected[dut_number])

    def test_6(self):
        FSC = FuelSystemConfigCreator(r"configurations/TwoDUTs/test6.xlsx").create()
        vduts = FSC["Tank1"]["virtual_duts_table"]
        expected = [
            pd.Series({
                "V_DUT_NUMBER": 1,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [0, 10, 20, 30],
                "V_DUT_LITERS": [0, 10, 20, 30],
                "DUT_VALUES": [0, 100, 200, 300],
                "ZONE_NUMBER": 1
            }),
            pd.Series({
                "V_DUT_NUMBER": 2,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [30, 40],
                "V_DUT_LITERS": [0, 10],
                "DUT_VALUES": [300, 400],
                "ZONE_NUMBER": 2
            }),
            pd.Series({
                "V_DUT_NUMBER": 3,
                "PARENT_DUT_NAME": "D2",
                "PARENT_LITERS": [30, 40],
                "V_DUT_LITERS": [0, 10],
                "DUT_VALUES": [0, 100],
                "ZONE_NUMBER": 2
            })
        ]
        for dut_number in range(len(expected)):
            pd.testing.assert_series_equal(vduts[dut_number], expected[dut_number])

    def test_7(self):
        FSC = FuelSystemConfigCreator(r"configurations/TwoDUTs/test7.xlsx").create()
        vduts = FSC["Tank1"]["virtual_duts_table"]
        expected = [
            pd.Series({
                "V_DUT_NUMBER": 1,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [0, 10],
                "V_DUT_LITERS": [0, 10],
                "DUT_VALUES": [0, 100],
                "ZONE_NUMBER": 1
            }),
            pd.Series({
                "V_DUT_NUMBER": 2,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [10, 20, 30],
                "V_DUT_LITERS": [0, 10, 20],
                "DUT_VALUES": [100, 200, 300],
                "ZONE_NUMBER": 2
            }),
            pd.Series({
                "V_DUT_NUMBER": 3,
                "PARENT_DUT_NAME": "D2",
                "PARENT_LITERS": [10, 20, 30],
                "V_DUT_LITERS": [0, 10, 20],
                "DUT_VALUES": [0, 100, 200],
                "ZONE_NUMBER": 2
            }),
            pd.Series({
                "V_DUT_NUMBER": 4,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [30, 40],
                "V_DUT_LITERS": [0, 10],
                "DUT_VALUES": [300, 400],
                "ZONE_NUMBER": 3
            })
        ]
        for dut_number in range(len(expected)):
            pd.testing.assert_series_equal(vduts[dut_number], expected[dut_number])

    def test_8(self):
        FSC = FuelSystemConfigCreator(r"configurations/TwoDUTs/test8.xlsx").create()
        vduts = FSC["Tank1"]["virtual_duts_table"]
        expected = [
            pd.Series({
                "V_DUT_NUMBER": 1,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [0, 10],
                "V_DUT_LITERS": [0, 10],
                "DUT_VALUES": [0, 100],
                "ZONE_NUMBER": 1
            }),
            pd.Series({
                "V_DUT_NUMBER": 2,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [10, 20, 30, 40, 50],
                "V_DUT_LITERS": [0, 10, 20, 30, 40],
                "DUT_VALUES": [100, 200, 300, 400, 500],
                "ZONE_NUMBER": 2
            }),
            pd.Series({
                "V_DUT_NUMBER": 3,
                "PARENT_DUT_NAME": "D2",
                "PARENT_LITERS": [10, 20, 30, 40, 50],
                "V_DUT_LITERS": [0, 10, 20, 30, 40],
                "DUT_VALUES": [0, 100, 200, 300, 400],
                "ZONE_NUMBER": 2
            }),
            pd.Series({
                "V_DUT_NUMBER": 4,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [50, 60],
                "V_DUT_LITERS": [0, 10],
                "DUT_VALUES": [500, 600],
                "ZONE_NUMBER": 3
            })
        ]
        for dut_number in range(len(expected)):
            pd.testing.assert_series_equal(vduts[dut_number], expected[dut_number])

    def test_9(self):
        FSC = FuelSystemConfigCreator(r"configurations/TwoDUTs/test9.xlsx").create()
        vduts = FSC["Tank1"]["virtual_duts_table"]
        expected = [
            pd.Series({
                "V_DUT_NUMBER": 1,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [0, 10, 20],
                "V_DUT_LITERS": [0, 10, 20],
                "DUT_VALUES": [0, 100, 200],
                "ZONE_NUMBER": 1
            }),
            pd.Series({
                "V_DUT_NUMBER": 2,
                "PARENT_DUT_NAME": "D2",
                "PARENT_LITERS": [20, 30, 40],
                "V_DUT_LITERS": [0, 10, 20],
                "DUT_VALUES": [0, 100, 200],
                "ZONE_NUMBER": 2
            })
        ]
        for dut_number in range(len(expected)):
            pd.testing.assert_series_equal(vduts[dut_number], expected[dut_number])


class HardConfig(unittest.TestCase):

    def test_1(self):
        FSC = FuelSystemConfigCreator(r"configurations/HardConfiguration/test1.xlsx").create()
        vduts = FSC["Tank1"]["virtual_duts_table"]
        expected = [
            pd.Series({
                "V_DUT_NUMBER": 1,
                "PARENT_DUT_NAME": "D2",
                "PARENT_LITERS": [0, 10, 20],
                "V_DUT_LITERS": [0, 10, 20],
                "DUT_VALUES": [30, 100, 160],
                "ZONE_NUMBER": 1
            }),
            pd.Series({
                "V_DUT_NUMBER": 2,
                "PARENT_DUT_NAME": "D2",
                "PARENT_LITERS": [20, 30, 40, 50],
                "V_DUT_LITERS": [0, 10, 20, 30],
                "DUT_VALUES": [160, 220, 280, 350],
                "ZONE_NUMBER": 2
            }),
            pd.Series({
                "V_DUT_NUMBER": 3,
                "PARENT_DUT_NAME": "D3",
                "PARENT_LITERS": [20, 30, 40, 50],
                "V_DUT_LITERS": [0, 10, 20, 30],
                "DUT_VALUES": [30, 100, 160, 220],
                "ZONE_NUMBER": 2
            }),
            pd.Series({
                "V_DUT_NUMBER": 4,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [50, 60, 70, 90, 100],
                "V_DUT_LITERS": [0, 10, 20, 40, 50],
                "DUT_VALUES": [30, 100, 160, 220, 280],
                "ZONE_NUMBER": 3
            }),
            pd.Series({
                "V_DUT_NUMBER": 5,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [100, 110, 120, 130],
                "V_DUT_LITERS": [0, 10, 20, 30],
                "DUT_VALUES": [280, 340, 400, 460],
                "ZONE_NUMBER": 4
            }),
            pd.Series({
                "V_DUT_NUMBER": 6,
                "PARENT_DUT_NAME": "D2",
                "PARENT_LITERS": [100, 110, 120, 130],
                "V_DUT_LITERS": [0, 10, 20, 30],
                "DUT_VALUES": [350, 440, 500, 560],
                "ZONE_NUMBER": 4
            }),
            pd.Series({
                "V_DUT_NUMBER": 7,
                "PARENT_DUT_NAME": "D3",
                "PARENT_LITERS": [100, 110, 120, 130],
                "V_DUT_LITERS": [0, 10, 20, 30],
                "DUT_VALUES": [220, 280, 347, 400],
                "ZONE_NUMBER": 4
            }),
            pd.Series({
                "V_DUT_NUMBER": 8,
                "PARENT_DUT_NAME": "D4",
                "PARENT_LITERS": [130, 140, 150, 160, 170, 180, 190, 200],
                "V_DUT_LITERS": [0, 10, 20, 30, 40, 50, 60, 70],
                "DUT_VALUES": [30, 100, 160, 220, 280, 340, 400, 460],
                "ZONE_NUMBER": 5
            }),
            pd.Series({
                "V_DUT_NUMBER": 9,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [200, 210, 220, 230, 240],
                "V_DUT_LITERS": [0, 10, 20, 30, 40],
                "DUT_VALUES": [460, 520, 580, 600, 664],
                "ZONE_NUMBER": 6
            }),
            pd.Series({
                "V_DUT_NUMBER": 10,
                "PARENT_DUT_NAME": "D2",
                "PARENT_LITERS": [200, 210, 220, 230, 240],
                "V_DUT_LITERS": [0, 10, 20, 30, 40],
                "DUT_VALUES": [560, 620, 680, 740, 800],
                "ZONE_NUMBER": 6
            }),
            pd.Series({
                "V_DUT_NUMBER": 11,
                "PARENT_DUT_NAME": "D3",
                "PARENT_LITERS": [200, 210, 220, 230, 240],
                "V_DUT_LITERS": [0, 10, 20, 30, 40],
                "DUT_VALUES": [400, 460, 520, 580, 620],
                "ZONE_NUMBER": 6
            }),
            pd.Series({
                "V_DUT_NUMBER": 12,
                "PARENT_DUT_NAME": "D4",
                "PARENT_LITERS": [200, 210, 220, 230, 240],
                "V_DUT_LITERS": [0, 10, 20, 30, 40],
                "DUT_VALUES": [460, 520, 580, 600, 664],
                "ZONE_NUMBER": 6
            }),
            pd.Series({
                "V_DUT_NUMBER": 13,
                "PARENT_DUT_NAME": "D2",
                "PARENT_LITERS": [240, 250, 260],
                "V_DUT_LITERS": [0, 10, 20],
                "DUT_VALUES": [800, 850, 900],
                "ZONE_NUMBER": 7
            }),
            pd.Series({
                "V_DUT_NUMBER": 14,
                "PARENT_DUT_NAME": "D3",
                "PARENT_LITERS": [240, 250, 260],
                "V_DUT_LITERS": [0, 10, 20],
                "DUT_VALUES": [620, 680, 730],
                "ZONE_NUMBER": 7
            })
        ]
        for dut_number in range(len(expected)):
            pd.testing.assert_series_equal(vduts[dut_number], expected[dut_number])

class TwoTanks(unittest.TestCase):

    def test_0(self):
        FSC = FuelSystemConfigCreator(r"configurations/TwoTanks/test0.xlsx").create()
        vduts = FSC["Tank1"]["virtual_duts_table"]
        expected = [
            pd.Series({
                "V_DUT_NUMBER": 1,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [0, 10, 20, 30, 40],
                "V_DUT_LITERS": [0, 10, 20, 30, 40],
                "DUT_VALUES": [0, 100, 200, 300, 400],
                "ZONE_NUMBER": 1
            }),
            pd.Series({
                "V_DUT_NUMBER": 2,
                "PARENT_DUT_NAME": "D2",
                "PARENT_LITERS": [0, 10, 20, 30, 40],
                "V_DUT_LITERS": [0, 10, 20, 30, 40],
                "DUT_VALUES": [0, 100, 200, 300, 400],
                "ZONE_NUMBER": 1
            })
        ]
        for dut_number in range(len(expected)):
            pd.testing.assert_series_equal(vduts[dut_number], expected[dut_number])

        vduts = FSC["Tank2"]["virtual_duts_table"]
        expected = [
            pd.Series({
                "V_DUT_NUMBER": 1,
                "PARENT_DUT_NAME": "D1",
                "PARENT_LITERS": [0, 10, 20, 30, 40],
                "V_DUT_LITERS": [0, 10, 20, 30, 40],
                "DUT_VALUES": [0, 100, 200, 300, 400],
                "ZONE_NUMBER": 1
            }),
            pd.Series({
                "V_DUT_NUMBER": 2,
                "PARENT_DUT_NAME": "D2",
                "PARENT_LITERS": [0, 10, 20, 30, 40],
                "V_DUT_LITERS": [0, 10, 20, 30, 40],
                "DUT_VALUES": [0, 100, 200, 300, 400],
                "ZONE_NUMBER": 1
            })
        ]
        for dut_number in range(len(expected)):
            pd.testing.assert_series_equal(vduts[dut_number], expected[dut_number])


class OpenError(unittest.TestCase):

    def test_0(self):
        with self.assertRaises(Exception) as context:
            FSC = FuelSystemConfigCreator(r"abc").create()

        self.assertTrue("open error file abc." == context.exception.args[0])
