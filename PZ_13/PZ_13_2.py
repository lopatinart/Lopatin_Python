import random

# Генерация двумерного списка
rows = 4
cols = 4
start = 10
step = random.randint(1, 5)

matrix = []
current = start
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(current)
        current += step
    matrix.append(row)

print("Сгенерированный двумерный список:\n")
for row in matrix:
    print(row)

print(f"\nНачальное значение: {start}, шаг преобразования: {step}")

# Сумма первых двух строк

sum_rows = sum(matrix[0]) + sum(matrix[1])
print(f"\nСумма элементов первых двух строк: {sum_rows}")
