my_string = input("Введити несколько слов через пробел:").split()

for i, n in enumerate(my_string, 1):
    print(f"{i} {n:.10}")