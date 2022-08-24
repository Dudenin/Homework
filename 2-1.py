my_list = [(-1 + 0j), 4, 3.5, True, None, 'stroka', [3, 4], (5, 14, 15.3), {7: 'seven', 8: 'eight'}, {9, 10}]
for i, val in enumerate(my_list, 1):
    print(f"{i}) {val} - {type(val)}")