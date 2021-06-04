import matplotlib.pyplot as plt


class Plotter():

    @staticmethod
    def rectangle_grid(nplots, ncols):
        height_coefs = {
            1: 6.5,
            2: 5.5,
            3: 4.5,
            4: 3.7,
            5: 3
        }
        height_coef = height_coefs[ncols]
        full_nrows, cols_in_last_row = divmod(nplots, ncols)
        nrows = full_nrows + bool(cols_in_last_row)
        fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(16, height_coef * nrows))
        if cols_in_last_row != 0:
            for col in range(cols_in_last_row, ncols):
                if nrows != 1:
                    ax[-1][col].axis('off')
                else:
                    ax[col].axis('off')
        return fig, ax.reshape(-1)

    def get_fx(self, fuel_system_config, title=r"$\frac{V_1 + V_2}{2}$", save_path = None):
        colors = ["red", "blue", "orange", "green", "pink"]

        n_tanks = len(fuel_system_config)
        fig, axs = Plotter.rectangle_grid(n_tanks * 2, n_tanks)
        fig.suptitle(title, fontsize=30)
        for tank_number, tank_name in enumerate(fuel_system_config):
            calibration_table_plot = axs[tank_number]
            virtual_duts_plot = axs[n_tanks + tank_number]

            calibration_table = fuel_system_config[tank_name]["calibration_table"]

            dut_names = list(calibration_table.columns[1:])
            dut_colors = {dut_name : dut_color for dut_name, dut_color in zip(dut_names, colors)}

            virtual_duts_plot.set_xticks(range(len(dut_names)))
            virtual_duts_plot.set_xticklabels(map(lambda x: f"${x}$", dut_names), fontsize=20)

            liters = calibration_table.LITERS

            for dut_name in calibration_table.columns[1:]:
                calibration_table_plot.plot(calibration_table[dut_name], liters, "o-", label=dut_name, color=dut_colors[dut_name], markersize=5, alpha=0.5)
            calibration_table_plot.set_xlabel("Показание на датчике уровня топлива (ед.)", fontsize=15)
            calibration_table_plot.set_ylabel("Объем топлива по датчику (л.)", fontsize=15)
            virtual_duts_plot.set_ylabel("Объем топлива по датчику (л.)", fontsize=15)

            virtual_duts_table = fuel_system_config[tank_name]["virtual_duts_table"]

            h_lines_list = []
            for virtual_dut in virtual_duts_table:
                dut_order = dut_names.index(virtual_dut.PARENT_DUT_NAME)
                y = virtual_dut.PARENT_LITERS
                x = len(y) * [dut_order]
                virtual_duts_plot.plot(x, y, "-", color=dut_colors[virtual_dut.PARENT_DUT_NAME])
                y = virtual_dut.PARENT_LITERS
                y = [y[0], y[-1]]
                x = len(y) * [dut_order]
                virtual_duts_plot.plot(x, y, "o", color=dut_colors[virtual_dut.PARENT_DUT_NAME], markersize=10)

                min_x = virtual_dut.DUT_VALUES[0]
                min_y = virtual_dut.PARENT_LITERS[0]
                max_x = virtual_dut.DUT_VALUES[-1]
                max_y = virtual_dut.PARENT_LITERS[-1]
                calibration_table_plot.plot(min_x, min_y, "o", color=dut_colors[virtual_dut.PARENT_DUT_NAME], markersize=10, alpha=0.5)
                calibration_table_plot.plot(max_x, max_y, "o", color=dut_colors[virtual_dut.PARENT_DUT_NAME], markersize=10, alpha=0.5)

                if min_y not in h_lines_list:
                    virtual_duts_plot.hlines(min_y, xmin=-0.5, xmax=len(dut_names) - 0.5, color="black", alpha=0.1)
                    h_lines_list.append(min_y)

                y = (min_y + max_y) / 2
                virtual_duts_plot.text(dut_order + 0.03, y, "$V_{" + str(virtual_dut.V_DUT_NUMBER) + "}$", size=20)
                virtual_duts_plot.text(-0.5, min_y + (y-min_y)/2, "$Z_{" + str(virtual_dut.ZONE_NUMBER) + "}$", size=20)

            virtual_duts_plot.hlines(max_y, xmin=-0.5, xmax=len(dut_names) - 0.5, color="black", alpha=0.1)
            virtual_duts_plot.tick_params(axis='both', which='major', labelsize=15)
            virtual_duts_plot.set(frame_on=False)
            calibration_table_plot.tick_params(axis='both', which='major', labelsize=15)
            calibration_table_plot.grid(color='black', linestyle='-', linewidth=0.2)

        if save_path:
            plt.savefig(save_path + r"\plot.jpg", dpi=200)
        else:
            plt.show()
