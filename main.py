from datetime import datetime

inputOil_str = '"Дизель"          2025.04.27    66.43'
# inputOil = ['"Дизель"          2025.04.27    66.43', '"АИ92"          2025.04.27    65.43' ]

# inputoilstation_str = '17 "Киренского 58" "Бензиновая"'



def trytoparse_oil(inputOil):
    result = []
    for string in inputOil:
        parts = string.split()
        price = parts[2]
        oilType = parts[0]
        date_str = str(parts[1])
        date = datetime.strptime(date_str, "%Y.%m.%d")
        result_tuple = (price, oilType, date_str)
        result.append(result_tuple)
        result = f"Тип топлива: {oilType}, Дата: {date.strftime('%Y.%m.%d')}, Цена: {price}"
    return result

def cheapestoil(listoils):
    typeoil = ''
    minValue = 999
    minIndex = 0
    for string in listoils:
        if float(string[0]) < minValue:
            typeoil = string[1]
            minValue = float(string[0])
    print(f'Название {typeoil}, цена: {minValue}')


# def trytoparse_oilstation(input_str):
#     parts = input_str.split('"')
#     parts = list(filter(None, parts))
#     print(parts)
#     number = int(parts[0])
#     adress = parts[1]
#     oilType = parts[2]
#     result_tuple = (number, adress, oilType)
#     result = f"Номер: {number}, Адрес: {adress}, Тип топлива: {oilType}"
#     return result
#

test = trytoparse_oil(inputOil)
print(test)
cheapestoil(test)
# print(trytoparse_oilstation(inputoilstation_str))