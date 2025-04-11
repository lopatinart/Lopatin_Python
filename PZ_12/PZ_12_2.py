# Составить генератор (yield), который переведет символы строки из верхнего
# регистра в нижний.

def lower_case_generator(string):
    for char in string:
        yield char.lower()


input_str = input("Введите строку>> ")
generator = lower_case_generator(input_str)

print("Вывод>> ")
for char in generator:
    print(char, end=", ")
