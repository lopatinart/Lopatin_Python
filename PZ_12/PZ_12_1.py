# В последовательности на n целых чисел умножить все элементы на последний
# минимальный элемент.

import random

n = int(input("Введите длину списка>> "))

sequence = []

for _ in range(n):
    sequence.append(random.randint(1, 15))

print(f"Начальный список>> {sequence}")


min_element = min(sequence)

last_min_index = len(sequence) - 1 - sequence[::-1].index(min_element)
last_min_element = sequence[last_min_index]
# print(f"Индекс последнего минимального элемента>> {last_min_index}")
print(f"Последний минимальный элемент>> {last_min_element}")


result = [x * last_min_element for x in sequence]
print(f"Конечный список>> {result}")
