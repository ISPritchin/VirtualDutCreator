class FormulaCreator:

    def __init__(self, fuel_system_config):
        self.fuel_system_config = fuel_system_config

        self.formula = {}
        self.latex_formula = {}
        self.wialon_formula = {}
        self.latex_formula_full = None
        self.get_formula()
        self.get_latex()
        self.get_wialon()
        self.get_latex_full()

    def get_formula(self):
        for tank_name in self.fuel_system_config:
            formula = ""
            n_zones = self.fuel_system_config[tank_name]["virtual_duts_table"][-1].ZONE_NUMBER
            for cur_zone_number in range(1, n_zones + 1):
                virtual_dutes_in_the_zone = [vd
                                             for vd in self.fuel_system_config[tank_name]["virtual_duts_table"]
                                             if vd.ZONE_NUMBER == cur_zone_number
                                             ]
                v_duts_in_zone = len(virtual_dutes_in_the_zone)
                if v_duts_in_zone > 1: formula += "("
                for dut_number, v_dut in enumerate(virtual_dutes_in_the_zone, 1):
                    formula += f"V{v_dut.V_DUT_NUMBER}"
                    if dut_number != v_duts_in_zone:
                        formula += " + "
                if v_duts_in_zone > 1: formula += f") / {v_duts_in_zone}"
                if cur_zone_number != n_zones:
                    formula += " + "
            self.formula[tank_name] = formula

    def get_latex(self):
        for tank_name in self.fuel_system_config:
            formula = ""
            n_zones = self.fuel_system_config[tank_name]["virtual_duts_table"][-1].ZONE_NUMBER
            for cur_zone_number in range(1, n_zones + 1):
                virtual_dutes_in_the_zone = [vd
                                             for vd in self.fuel_system_config[tank_name]["virtual_duts_table"]
                                             if vd.ZONE_NUMBER == cur_zone_number]
                v_duts_in_zone = len(virtual_dutes_in_the_zone)
                if v_duts_in_zone > 1: formula += r"\frac{"
                for dut_number, v_dut in enumerate(virtual_dutes_in_the_zone, 1):
                    formula += "V_{" + str(v_dut.V_DUT_NUMBER) + "}"
                    if dut_number != v_duts_in_zone:
                        formula += " + "
                if v_duts_in_zone > 1: formula += "}{" + str(v_duts_in_zone) + "}"
                if cur_zone_number != n_zones:
                    formula += " + "
            self.latex_formula[tank_name] = formula

        return self.latex_formula

    def get_wialon(self):
        for tank_name in self.fuel_system_config:
            formula = ""
            n_zones = self.fuel_system_config[tank_name]["virtual_duts_table"][-1].ZONE_NUMBER
            for cur_zone_number in range(1, n_zones + 1):
                virtual_dutes_in_the_zone = [vd
                                             for vd in self.fuel_system_config[tank_name]["virtual_duts_table"]
                                             if vd.ZONE_NUMBER == cur_zone_number
                                             ]
                v_duts_in_zone = len(virtual_dutes_in_the_zone)
                if v_duts_in_zone > 1: formula += r"("
                for dut_number, v_dut in enumerate(virtual_dutes_in_the_zone, 1):
                    formula += "FUEL_" + str(v_dut.V_DUT_NUMBER)
                    if dut_number != v_duts_in_zone:
                        formula += " + "
                if v_duts_in_zone > 1: formula += ") / const" + str(v_duts_in_zone)
                if cur_zone_number != n_zones:
                    formula += " + "
            self.wialon_formula[tank_name] = formula

        return self.wialon_formula

    def get_latex_full(self):
        if len(self.latex_formula) == 1:
            tank_name = list(self.fuel_system_config.keys())[0]
            self.latex_formula_full =  "$" + self.latex_formula[tank_name] + "$"
            return

        formula = ""
        n_tanks = len(self.fuel_system_config)
        for i, tank in enumerate(self.latex_formula, 1):
            formula += r"\left[" + self.latex_formula[tank] + r"\right]"
            if i != n_tanks:
                formula += " + "

        self.latex_formula_full = "$" + formula + "$"
