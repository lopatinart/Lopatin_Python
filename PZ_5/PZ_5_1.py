# Составить программу, в которой функция построит изображение, в котором в первой
# строке 1 звездочка, во второй - 2, в третьей -3, .., в строке с номером m - m звездочек.

count = input('Введите количество строк>> ')

# Обработка исключений
while type(count) != int:
    try:
        count = int(count)
        # Проверка на положительность count
        if count < 0:
            print("Неправильно ввели!")
            count = input('Введите количество строк>> ')
    except ValueError:
        print("Неправильно ввели!")
        count = input('Введите количество строк>> ')


def stars(m):
    for i in range(1, m + 1):
        print(i * '*')

stars(count)
