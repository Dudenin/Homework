num_init = int(input("Введите целое положительное число: "))
gratest_dig = 0
num =  num_init

while num > 0:
    digit = num % 10
    if digit > gratest_dig:
        gratest_dig = digit
        if gratest_dig == 9:
            break
    num = num // 10
print(f"Наибольша цифра в числе {num_init} равна {gratest_dig}")