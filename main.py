inputOil_str = '"Дизель"          2025.04.27    66.43'

def trytoparse_oil(string):
    parts = string.split()
    price = parts[2]
    oilType = parts[0]
    date_str = str(parts[1])
    result = f"Тип топлива: {oilType}, Дата: {date_str}, Цена: {price}"
    return result

print(trytoparse_oil(inputOil_str))