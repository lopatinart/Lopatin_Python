# Дан список размера N. Найти номера двух ближайших элементов из этого списка (то
# есть элементов с наименьшим модулем разности) и вывести эти номера в порядке
# возрастания.

# Импортируем нужные библиотеки
import random

count = input('Введите количество элементов списка>> ')

# Обработка исключений
while type(count) != int:
    try:
        count = int(count)
        # Проверка на правильную длину списка
        if count < 2:
            print("Неправильно ввели!\nСписок должен содержать не менее 2 элементов!")
            count = input('Введите количество элементов списка>> ')
    except ValueError:
        print("Неправильно ввели!")
        count = input('Введите количество элементов списка>> ')

nums = []

# Цикл генирирующий список из N случайных чисел
for i in range(count):
    num = random.randint(-100,100)
    nums.append(num)

print(nums)

# Задаем минимульную разницу и начальные индексы
min_diff = 200.1
closest_items = (0, 1)

#Цикл, находящий минимальную разницу путем сравнивания 2х элементов
for i in range(len(nums)):
    for a in range(i + 1, len(nums)):
        diff = abs(nums[i] - nums[a])

        if diff < min_diff:
            min_diff = diff
            closest_items = (i, a)

print(f'Индексы элементов с минимальным модулем разности>> {sorted(closest_items)}')