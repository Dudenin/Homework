def my_func(x, y):
    try:
        x, y = float(x), int(y)
        if x <=0 or y >=0:
            return 'Условие ввода данных не выполненно'
        else:
            result = 1
            for _ in range(abs(y)):
                result /= x
            print('Результат возведения X в степень Y:')
            return round(result, 6)
    except ValueError:
        return 'Программа работатет только с числами.'
number1 = input('Введите дествительное положительное число х = ')
number2 = input('Введите целое отрицтельное число y = ')

print(my_func(number1, number2))
