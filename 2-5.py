my_list = [9, 8 , 7, 7, 7, 6, 5, 4, 2, 3, 3, 2, 1]

while True:
    new_number = input("Entre new element:\n")
    if new_number.isdigit():
        my_list.append(float(new_number))
        my_list.sort(reverse=True)
        print(my_list)
    elif new_number == "q":
        break