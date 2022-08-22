while True:
    days = 1
    start_km = float(input(f"Введите стартовый результат в км:"))
    last_km = float(input(f"Введите итоговый результат в км:"))
    if start_km <= 0 or last_km < 0 :
        print(f"Введено ошибочное значение!")
    else:
        while start_km < last_km:
            start_km += start_km * 0.1
            days += 1
        print(f"Спортсмен добъется результата за {days} дней")
        break