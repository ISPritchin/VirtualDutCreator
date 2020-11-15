import pandas as pd


class Fixer:
    """
    Класс предоставляет методы для исправления ошибок внесения тарировочных таблиц.
    Требования:
        - показания значений литров являются возрастающими
        - показания значений ДУТ являются возрастающими
    """

    @staticmethod
    def transform(table):
        """
        Исправляет ошибки в таблице (если имеются немонотонно возрастающие столбцы) на основании данных,
        введенных с клавиатуры. Предполагается, что первое и последнее значение введены верно
        :param table:
            - Тарировочная таблица
        :return:
            - Исправленная тарировочная таблица
        """
        liters = Fixer.fix_liters(table.LITERS)
        dut_values = Fixer.fix_dut_values(liters, table.iloc[:, 1:])
        return pd.concat([liters, dut_values], axis=1)

    @staticmethod
    def fix_liters(liters):
        """
        Выполняет проверку колонки liters на монотонность возрастания. В случае, если liters не является монотонно
        возрастающей - предлагает пользователю выполнить исправление вектора.
        :param liters:
            Вектор-значений литров
        :return:
            Исправленный вектор-значений литров
        """
        for i in range(1, len(liters) - 1):
            # вылет вверх
            checking_value = liters[i]
            while liters[i - 1] <= liters[i + 1] < checking_value:
                print(f"Ошибка ввода между {liters[i - 1]} и {liters[i + 1]} литрами. Введено: {checking_value}")
                checking_value = int(input("Введите корректное значение между ними: "))
                print("")
            while liters[i + 1] >= liters[i - 1] > checking_value:
                print(f"Ошибка ввода между {liters[i - 1]} и {liters[i + 1]} литрами. Введено: {checking_value}")
                checking_value = int(input("Введите корректное значение между ними: "))
                print("")
            liters[i] = checking_value
        return liters

    @staticmethod
    def fix_dut_values(liters, dut_values):
        """
        Выполняет проверку корректнеости показаний ДУТ на монотонность возрастания. Предлагает выполнить
        исправление вектора
        :param liters:
            Вектор-значений литров
        :param dut_values:
            Таблица из значений показаний ДУТ
        :return:
        """
        for device_name in dut_values.columns:
            print(f"Проверка колонки {device_name}")
            dut_vector = dut_values[device_name]
            dut_values[device_name] = Fixer.fix_dut_vector(liters, dut_vector)
        return dut_values

    @staticmethod
    def fix_dut_vector(liters, column):
        """
        Выполняет проверку корректнеости показаний ДУТ на монотонность возрастания. Предлагает выполнить исправление
        вектора
        :param liters:
            Вектор-значений литров
        :param column:
            Таблица из значений показаний ДУТ
        :return:
            Исправленные значениу ДУТ
        """
        find_start_dut = False
        for i in range(0, len(column) - 1):
            if pd.isna(column[i]):
                continue
            elif not find_start_dut:
                find_start_dut = True
                continue
            if pd.isna(column[i + 1]):
                break
            # вылет вверх
            checking_value = column[i]
            while column[i - 1] <= column[i + 1] < checking_value:
                print(f"Ошибка, ввода столбца {column.name}  в значении {liters[i]} л. Введено: {checking_value}")
                checking_value = int(input("Введите корректное значение: "))
                print("")
            while column[i + 1] >= column[i - 1] > checking_value:
                print(f"Ошибка, ввода столбца {column.name}  в значении {liters[i]} л. Введено: {checking_value}")
                checking_value = int(input("Введите корректное значение: "))
                print("")
            column[i] = checking_value
        return column
