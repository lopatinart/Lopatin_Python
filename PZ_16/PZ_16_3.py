import pickle
from PZ_16_1 import Matrix


def save_def(matrices, filename):
    """
    Сохраняет список матриц в бинарный файл.
    """
    with open(filename, 'wb') as file:
        pickle.dump(matrices, file)
    print(f"Матрицы успешно сохранены в файл '{filename}'.")


def load_def(filename):
    """
    Загружает список матриц из бинарного файла.
    """
    with open(filename, 'rb') as file:
        matrices = pickle.load(file)
    print(f"Матрицы успешно загружены из файла '{filename}'.")
    return matrices

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
m3 = Matrix([[9, 10], [11, 12]])

save_def([m1, m2, m3], 'matrices.pkl')

loaded_matrices = load_def('matrices.pkl')

# Вывод
print("\nЗагруженные матрицы:")
for matrix in loaded_matrices:
    matrix.print()
    print()