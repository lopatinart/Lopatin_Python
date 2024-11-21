# Дан список A ненулевых целых чисел размера 10. Вывести значение первого из тех
# его элементов AK, которые удовлетворяют неравенству AK < A10. Если таких
# элементов нет, то вывести 0

# Импортируем нужные библиотеки
import random

A = []
counter = 0

# Цикл генирирующий список из 10 случайных ненулевых чисел
while counter != 10:
    num = random.randint(-100,100)
    if num != 0:
        A.append(num)
        counter += 1


print(A)

last_item = A[9]

is_found = False

# Цикл, проходящий по всем элементам списка и проверяющий правдивость условия
for item in A:
    if item < last_item:
        print(f'Элемент удовлетворяющий условию>> {item}')
        is_found = True
        break

if not is_found:
    print(0)
