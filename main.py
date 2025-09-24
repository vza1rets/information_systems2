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
        return (f"Тип топлива: {self.oil_type}, Цена: "
                f"{self.price}, Дата: {self.datee.strftime('%Y.%m.%d')}, Поставщик: {self.supplier}, Объем: {self.volume}")

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
        price = float(parts[2])
        oil_type = parts[1].strip('"')
        datee = (datetime.strptime(str(parts[2]), "%Y.%m.%d")).date()
        supplier = parts[3]
        volume = float(parts[4])
        yield ExtendedOilPrice(oil_type, datee, price, supplier, volume)

def find_maxprice(strings):
    maxprice = 0
    for string in strings:
        parts = shlex.split(string)
        if float(parts[2]) > maxprice:
            maxprice = float(parts[2])
    print(f'Максимальная цена: {maxprice}')

def print_menu():
    print("\n=== Панель управления ===")
    print("1) Добавить строку")
    print("2) Удалить строку")
    print("3) Показать строки")
    print("4) Показать объекты (парсинг)")
    print("5) Максимальная цена")
    print("6) Загрузить из файла")
    print("7) Выход")

def show_raw(strings):
    if not strings:
        print("Список строк пуст.")
        return
    print("Текущие строки:")
    for i, s in enumerate(strings):
        print(f"{i}: {s}")

def add_raw(strings):
    s = input("Введите строку формата: \"Тип\" YYYY.MM.DD price \"supplier\" volume\n> ").strip()
    if not s:
        print("Пустая строка не добавлена.")
        return
    strings.append(s)
    print("Строка добавлена.")

def delete_raw(strings):
    if not strings:
        print("Список строк пуст, удалять нечего.")
        return
    show_raw(strings)
    raw = input("Введите индекс для удаления: ").strip()
    if not raw.isdigit():
        print("Индекс должен быть числом.")
        return
    idx = int(raw)
    if idx < 0 or idx >= len(strings):
        print("Индекс вне диапазона.")
        return
    removed = strings.pop(idx)
    print(f"Удалено: {removed}")

def show_objects(strings):
    if not strings:
        print("Список строк пуст.")
    for obj in trytoparse_extendedoil(strings):
        print(obj)

def show_max_price(strings):
    if len(strings) < 1:
        print("Нет данных для вычисления.")
        return
    mx = find_maxprice(strings)
    if mx != mx:  # NaN
        print("Не удалось определить максимальную цену (проверьте данные).")
    else:
        print(f"Максимальная цена: {mx}")

def load_from_file(strings):
    path = input("Путь к файлу: ").strip()
    lines = read_lines_from_file(path)
    strings.extend(lines)
    print(f"Загружено строк: {len(lines)}")

def main():
    strings = []
    while True:
        print_menu()
        choice = input("Выберите пункт (1-8): ").strip()
        if choice == "1":
            add_raw(strings)
        elif choice == "2":
            delete_raw(strings)
        elif choice == "3":
            show_raw(strings)
        elif choice == "4":
            show_objects(strings)
        elif choice == "5":
            show_max_price(strings)
        elif choice == "6":
            load_from_file(strings)
        elif choice == "7":
            print("Программа завершена")
            break
        else:
            print("Неизвестная команда. Введите число 1-7.")



if __name__ == "__main__":
    main()



