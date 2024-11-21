# Дан список A размера N и целое число K (1 < K < 4, K < N ). Осуществить
# циклический сдвиг элементов списка влево на K позиций (при этом AN перейдет в
# AN_K, AN-1 — в AN-K-1, ..., A1 — в AN-K+1). Допускается использовать вспомогательный
# список из 4 элементов.

# Ввод данных
N = input('Введите длинну списка>> ')

# Обработка исключений
while type(N) != int:
    try:
        N = int(N)
        # Проверка на правильную длину списка
        if N < 4:
            print("Неправильно ввели!\nСписок не может содержать меньше 4 элементов!")
            N = input('Введите длинну списка>> ')
    except ValueError:
        print("Неправильно ввели!")
        N = input('Введите длинну списка>> ')

K = input('Введите количество позиций сдвига>> ')

# Обработка исключений
while type(K) != int:
    try:
        K = int(K)
        # Проверка на правильную длину списка
        if not 1 < K < 4 or not K < N:
            print("Неправильно ввели!\nЧисло K не соответствует условиям!")
            K = input('Введите количество позиций сдвига>> ')
    except ValueError:
        print("Неправильно ввели!")
        K = input('Введите количество позиций сдвига>> ')

A = []
supp = [0, 0, 0, 0]  # Вспомогательный список

# Цикл для создания списка из N элементов
for i in range(1, N + 1):
    A.append(i)

print(f'\nНачальный список>> {A}')

# Перезаписываем элементы из списка A до K в список supp
for i in range(K):
    supp[i] = A[i]

# Сдвиг оставшихся элементов влево
for i in range(K, N):
    A[i - K] = A[i]

# Вставим элементы из списка supp в конец
for i in range(K):
    A[N - K + i] = supp[i]

print(f'Конечный список>> {A}')