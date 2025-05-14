# Сгенерировать двумерный список на произвольное количество элементов, в которой
# задается преобразование от предыдущего элемента к следующему на произвольное
# значение.

import random

rows = 4
cols = 4
start = 10
step = random.randint(1, 5)

# Генерация двумерного списка
matrix = []
current = start
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(current)
        current += step
    matrix.append(row)

# Вывод результатов
print("Сгенерированный двумерный список>>")
for row in matrix:
    print(row)

print(f"Начальное значение: {start}, шаг преобразования>> {step}")