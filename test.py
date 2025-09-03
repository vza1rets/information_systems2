from datetime import datetime


def parse_input(input_str):
        parts = input_str.split('"')
        date_str = parts[0].strip().split()
        date_str = str(date_str[0])
        product_name = parts[1]
        quantity = int(parts[2])
        date = datetime.strptime(date_str, "%Y.%m.%d")
        return f"Дата: {date.strftime('%Y.%m.%d')}, Название: {product_name}, Количество: {quantity}"

input_str = '2024.09.01 "Виноград" 150'

print(parse_input(input_str))