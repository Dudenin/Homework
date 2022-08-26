def my_func():
    for word in input('Введите текст:\n').split():                      
        chars = 0
        for symbol in word:
            if 97 <= ord(symbol) <= 122:
                chars += 1
        print(word.title() if chars == len(word) else f'{word} - только латинские буквы нижнего регистра!')
my_func()