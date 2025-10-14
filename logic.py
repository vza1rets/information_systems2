from datetime import datetime, date
import shlex

class ExtendedOilPrice:
    def __init__(self, oil_type: str, datee : date, price: float, supplier : str, volume : float):
        self.oil_type = oil_type
        self.datee = datee
        self.price = price
        self.supplier = supplier
        self.volume = volume
    def __str__(self):
        return (f"Тип топлива: {self.oil_type}, Дата: {self.datee.strftime('%Y.%m.%d')}, Цена: "
                f"{self.price}, Поставщик: {self.supplier}, Объем: {self.volume}")

class Model:
    def __init__(self):
        self.strings = []
        self.objects = []

    @staticmethod
    def read_lines_from_file(path):
        with open(path, encoding="utf-8") as f:
            return [line.rstrip() for line in f]

    def load_from_file(self, path):
        lines = self.read_lines_from_file(path)
        self.strings.extend(lines)
        return len(lines)

    def add_raw(self, s):
        if not s:
            return "Пустая строка не добавлена."
        self.strings.append(s)
        return "Строка добавлена."

    def delete_raw(self, raw):
        if not self.strings:
            return "Список строк пуст, удалять нечего."
        if raw < 0 or raw >= len(self.strings):
            return "Индекс вне диапазона."
        removed = self.strings.pop(raw)
        return f"Удалено: {removed}"

    def trytoparse_extendedoil(self):
        result_objects = []
        for string in self.strings:
            parts = shlex.split(string)
            price = float(parts[1])
            oil_type = parts[0].strip('"')
            datee = (datetime.strptime(str(parts[2]), "%Y.%m.%d")).date()
            supplier = parts[3]
            volume = float(parts[4])
            result_objects.append(ExtendedOilPrice(oil_type, datee, price, supplier, volume))
        return result_objects

    def find_maxprice(self):
        maxprice = 0
        for string in self.strings:
            parts = shlex.split(string)
            if float(parts[1]) > maxprice:
                maxprice = float(parts[1])
        return maxprice
