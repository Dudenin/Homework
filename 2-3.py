mounth = int(input(f"Введите номер месяца:"))

mounth_dict = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь", 7: "Июль", 8: "Август",
               9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}
mounth_list = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
               "Ноябрь", "Декабрь"]

if mounth in mounth_dict:
    print(f"{mounth}-й месяц года - это {mounth_dict[mounth]}")
    print(f"{mounth}-й месяц года - это {mounth_list[mounth-1]}")
    season_dict = {0: "Зима", 1: "Весна", 2: "Лето", 3: "Осень", 4: "Зима"}
    season_list = ["Зима", "Весна", "Лето", "Осень", "Зима"]
    print(f"Словарь сезонов - {mounth_dict[mounth]} это {season_dict[int(mounth) // 3]}\nСписок сезонов - {mounth_dict[mounth]} это {season_list[int(mounth) // 3]}")
else:
    print(f"Неправильный номер!")

