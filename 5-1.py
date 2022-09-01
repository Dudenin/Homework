file_name = input('Введите имя файла для создания:')

with open(f'{file_name}.txt', 'w', encoding='utf-8') as f:
    print('Для завершения ввода данных введите пустую строку.')
    while True:
        line = input('Введите данные:')
        if not line:
            break
        f.write(f'{line}\n')

