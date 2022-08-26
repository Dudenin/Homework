def sum_num():
    s = 0
    while True:
        err = False
        in_list = input('Введите числа, для выхода введите "q" ').split()
        for num in in_list:
            if num.lower() == 'q':
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    err = True
        if err:
            print('Введены ошибочные данные!')
        print(f'Суммма чисел: {s}')

print(sum_num())


