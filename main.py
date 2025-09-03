from datetime import datetime

inputOil_str = '"Дизель"          2025.04.27    66.43'

inputoilstation_str = '17          "Киренского 58"             "Бензиновая"'



def trytoparse_oil(input_str):
    parts = input_str.split()
    price = parts[2]
    oilType = parts[0]
    date_str = str(parts[1])
    date = datetime.strptime(date_str, "%Y.%m.%d")
    result = f"Тип топлива: {oilType}, Дата: {date.strftime('%Y.%m.%d')}, Цена: {price}"
    return result

def trytoparse_oilstation(input_str):
    parts = input_str.split('"')
    number = int(parts[0])
    adress = parts[1]
    oilType = parts[2]
    result = f"Номер: {number}, Адрес: {adress}, Тип топлива: {oilType}"
    return result




print(trytoparse_oil(inputOil_str))
print(trytoparse_oilstation(inputoilstation_str))