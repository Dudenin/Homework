revenue = float(input("Введите значение выручки:"))
costs = float(input("Введите значение издержек:"))
result = revenue - costs
if result > 0:
    print(f"Компания работает с прибылью {result}")
    print(f"Рентабельность выручки составила {100 * (result / costs):1f}%")
    personsal_n = int(input("Сколько сотрудников в вашей комапнии? "))
    print(f"На каждого сотрудника приходится {result / personsal_n}")
elif result < 0:
    print(f"Ваша компания работает с убытком.")
else:
    print(f"Ваша компания работает без прибыли.")