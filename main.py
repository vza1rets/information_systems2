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
        return f"Тип топлива: {self.oil_type}, Дата: {self.datee.strftime('%Y.%m.%d')}, Цена: {self.price}, Поставщик: {self.supplier}, Объем: {self.volume}"

inputOil_str = '"Дизель"             2025.04.27 66.43         "Газпром Нефть" 10000'

def trytoparse_extendedoil(string) -> ExtendedOilPrice:
    parts = shlex.split(string)
    print(parts)
    price = float(parts[2])
    oil_type = parts[0].strip('"')
    datee = (datetime.strptime(str(parts[1]), "%Y.%m.%d")).date()
    supplier = "hello"
    volume = 5.5
    return ExtendedOilPrice(oil_type, datee, price, supplier, volume)

print(trytoparse_extendedoil(inputOil_str))
