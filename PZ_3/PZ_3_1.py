# Дано целое положительное число
# высказывания: «Данное число является четным двузначным».

number_input = input('Введите число>> ')

while type(number_input) != int:  # Обработка исключений
    try:
        number_input = int(number_input)
        if number_input >= 0:  # Проверка на положительность числа
            break
        else:
            print("Неправильно ввели!")
            number_input = input('Введите число>> ')
    except ValueError:
        print("Неправильно ввели!")
        number_input = input('Введите число>> ')

# Проверка условия, что число является четныи и двузначным
if (number_input % 2 == 0) and (9 < number_input < 100):
    print(True)  # Число подходит под условия
else:
    print(False)  # Число не подходит под условия
