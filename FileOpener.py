print('File or string?')
typee = input()
strings = []
if typee.lower() == 'file':
    path = input('Введите путь к файлу: ')
    try:
        with open(f'{path}', encoding='utf-8') as f:
            strings = f.readlines()
            strings = [line.rstrip() for line in strings]
    except:
        print('Не удалось открыть файл')
elif typee.lower() == 'string':
    print('Введите строку')
    strings.append(input())