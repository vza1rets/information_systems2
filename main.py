from datetime import datetime, date
import shlex


class ExtendedOilPrice:
    def __init__(self, oil_type: str, datee : date, price: float, supplier : str, volume : float, maxvolume : float):
        self.oil_type = oil_type
        self.datee = datee
        self.price = price
        self.supplier = supplier
        self.volume = volume
        self.maxvolume = maxvolume
    def __str__(self):
        return (f"Тип топлива: {self.oil_type}, Дата: {self.datee.strftime('%Y.%m.%d')}, Цена: "
                f"{self.price}, Поставщик: {self.supplier}, Объем: {self.volume}, Max Volume: {self.maxvolume}")

def read_lines_from_file(path):
    with open(path, encoding="utf-8") as f:
        return [line.rstrip() for line in f]

def read_lines_interactive():
    print("Вводите строки; пустая строка завершит ввод.")
    lines = []
    while True:
        s = input().strip()
        if not s:
            break
        lines.append(s)
    return lines

def trytoparse_extendedoil(strings) -> ExtendedOilPrice:
    for string in strings:
        parts = shlex.split(string)
        print(parts)
        price = float(parts[2])
        oil_type = parts[0].strip('"')
        datee = (datetime.strptime(str(parts[1]), "%Y.%m.%d")).date()
        supplier = parts[3]
        volume = float(parts[4])
        maxvolume = float(parts[5])
        yield ExtendedOilPrice(oil_type, datee, price, supplier, volume, maxvolume)

def find_maxprice(strings):
    maxprice = 0
    for string in strings:
        parts = shlex.split(string)
        if float(parts[2]) > maxprice:
            maxprice = float(parts[2])
    print(f'Максимальная цена: {maxprice}')

def main():
    typee = input('File or string? ').lower()
    if typee == 'file':
        strings = read_lines_from_file((input('Путь к файлу: ')))
    elif typee == 'string':
        strings = read_lines_interactive()
    for obj in trytoparse_extendedoil(strings):
        print(obj)
    if len(strings) >= 2:
        find_maxprice(strings)


if __name__ == "__main__":
    main()



