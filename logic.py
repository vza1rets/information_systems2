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
        try:
            with open(path, encoding="utf-8") as f:
                return [line.rstrip() for line in f], []
        except FileNotFoundError:
            return [], [f"Файл не найден: {path}"]

    def load_from_file(self, path):
        lines, errors = self.read_lines_from_file(path)
        if lines:
            self.strings.extend(lines)
        return len(lines), errors

    def add_raw(self, s):
        if not s:
            return "Пустая строка не добавлена."
        self.strings.append(s)
        return "Строка добавлена."

    def delete_raw(self, raw):
        error = None
        if not self.strings:
            return "Список строк пуст, удалять нечего."
        try:
            ind = int(raw)
            removed = self.strings.pop(ind)
            return f"Удалено: {removed}", error
        except Exception as e:
            error = f"Ошибка - {e}"
            return "", error

    def trytoparse_extendedoil(self):
        result_objects = []
        errors = []
        for idx, string in enumerate(self.strings):
            try:
                parts = shlex.split(string)
                if len(parts) < 5:
                    raise ValueError("Недостаточно элементов для парса")
                if len(parts) > 5:
                    raise ValueError("Количество элементов больше, чем нужно")
                price = float(parts[1])
                oil_type = parts[0].strip('"')
                datee = datetime.strptime(str(parts[2]), "%Y.%m.%d").date()
                supplier = parts[3]
                volume = float(parts[4])
                result_objects.append(ExtendedOilPrice(oil_type, datee, price, supplier, volume))
            except Exception as e:
                errors.append(f"Ошибка в строке {idx}: {string} — {e}")
        return result_objects, errors

    def find_maxprice(self):
        maxprice = 0
        errors = []
        for idx, string in enumerate(self.strings):
            try:
                parts = shlex.split(string)
                price = float(parts[1])
                if price > maxprice:
                    maxprice = price
            except Exception as e:
                errors.append(f"Ошибка в строке {idx}: {string!r} — {e}")
        return maxprice, errors
