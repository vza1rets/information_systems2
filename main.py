from datetime import datetime, date
import shlex
from FileOpener import strings

class ExtendedOilPrice:
    def __init__(self, oil_type: str, datee : date, price: float, supplier : str, volume : float):
        self.oil_type = oil_type
        self.datee = datee
        self.price = price
        self.supplier = supplier
        self.volume = volume
    def __str__(self):
        return f"Тип топлива: {self.oil_type}, Дата: {self.datee.strftime('%Y.%m.%d')}, Цена: {self.price}, Поставщик: {self.supplier}, Объем: {self.volume}"

input_str = strings

def trytoparse_extendedoil(string) -> ExtendedOilPrice:
    for string in strings:
        parts = shlex.split(string)
        price = float(parts[2])
        oil_type = parts[0].strip('"')
        datee = (datetime.strptime(str(parts[1]), "%Y.%m.%d")).date()
        supplier = parts[3]
        volume = parts[4]
        yield ExtendedOilPrice(oil_type, datee, price, supplier, volume)

for string in trytoparse_extendedoil(input_str):
    print(string)

