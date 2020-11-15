class IsNotMonotonicException(Exception):
    "Класс-исключение для случаев, когда показания ДУТа не являются неубывающими"

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class OpenFileException(Exception):
    "Класс-исключение для ошибок открытия файла"

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class EmptyValueException(Exception):
    "Класс-исключение для проверки пустых значений в тарировочной таблице"
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)