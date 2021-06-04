import unittest

import pandas as pd

from main import process

class TestMain(unittest.TestCase):

    @staticmethod
    def test_0():
        configs = [
            "Case_1.xlsx",
            "Challenger_1.xlsx",
            "Deutz Fahr.xlsx",
            "Freightliner.xlsx",
            "MAN.xlsx",
            "New Holland.xlsx",
            "tmp1.xlsx",
            "tmp2.xlsx",
            "Камаз_1.xlsx",
        ]
        for config in configs:
            process(r"../configurations/Real/" + config, config.split(".")[0] + "/")

