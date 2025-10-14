import logic

class View:
    def __init__(self):
        self.model = logic.Model()
        self.path = ""
        self.strings = []


    @staticmethod
    def print_menu():
        print("\n=== Панель управления ===")
        print("1) Добавить строку")
        print("2) Удалить строку")
        print("3) Показать строки")
        print("4) Показать объекты (парсинг)")
        print("5) Максимальная цена")
        print("6) Загрузить из файла")
        print("7) Выход")

    @staticmethod
    def show_raw(self):
        for i, s in enumerate(self.model.strings):
            print(f"{i}: {s}")

    def main(self):
        while True:
            self.print_menu()
            choice = input("Выберите пункт (1-8): ").strip()
            if choice == "1":
                s = input("Введите строку формата: \"Тип\" YYYY.MM.DD price \"supplier\" volume\n> ").strip()
                print(self.model.add_raw(s))
            elif choice == "2":
                self.show_raw(self)
                raw = input("Введите индекс для удаления: ")
                removed, error = self.model.delete_raw(raw)
                if error:
                    print(error)
                else:
                    print(removed)
            elif choice == "3":
                print("Текущие строки:")
                self.show_raw(self)
            elif choice == "4":
                objects, errors = self.model.trytoparse_extendedoil()
                if errors:
                    print("\nВнимание! Некоторые строки не были обработаны корректно:")
                    for err in errors:
                        print(err)
                print("Объекты:")
                for obj in objects:
                    print(obj)
            elif choice == "5":
                maxprice, errors = self.model.find_maxprice()
                if errors:
                    print("\nНекоторые строки пропущены:")
                    for err in errors:
                        print(err)
                print(f'Максимальная цена: {maxprice if maxprice is not None else "Нет корректных цен"}')
            elif choice == "6":
                path = input("Путь к файлу: ").strip()
                count, errors = self.model.load_from_file(path)
                for err in errors:
                    print(err)
                print(f"Загружено строк: {count}")
            elif choice == "7":
                print("Программа завершена")
                break
            else:
                print("Неизвестная команда. Введите число 1-7.")


if __name__ == "__main__":
    View().main()



