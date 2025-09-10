print('File or string?')
typee = input()
strings = []
if typee.lower() == 'file':
    path = input('Введите путь к файлу: ')
    with open(f'{path}', encoding='utf-8') as f:
        strings = f.readlines()
        strings = [line.rstrip() for line in strings]
elif typee.lower() == 'string':
    strings.append('"Дизель"             2025.04.27 66.43         "Газпром Нефть" 10000')