# Создайте класс «Матрица», который имеет атрибуты количества строк и столбцов.
# Добавьте методы для сложения, вычитания и умножения матриц.

class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def add(self, other):
        """Сложение двух матриц."""
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)

    def subtract(self, other):
        """Вычитание двух матриц."""
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] - other.data[i][j])
            result.append(row)
        return Matrix(result)

    def multiply(self, other):
        """Умножение двух матриц."""
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                s = 0
                for k in range(self.cols):
                    s += self.data[i][k] * other.data[k][j]
                row.append(s)
            result.append(row)
        return Matrix(result)

    def print(self):
        """Вывод матрицы на экран."""
        for row in self.data:
            print(row)


# Создание мамтриц
m1_rows = int(input("Введите количество строк в первой матрице>> "))
m1_cols = int(input("Введите количество столбцов в первой матрице>> "))
m1_start = int(input("Введите начальное значение первой матрицы>> "))
m1 = []
current = m1_start
for i in range(m1_rows):
    row = []
    for j in range(m1_cols):
        row.append(current)
        current += 1
    m1.append(row)

m2_rows = int(input("\nВведите количество строк во второй матрице>> "))
m2_cols = int(input("Введите количество столбцов во второй матрице>> "))
m2_start = int(input("Введите начальное значение второй матрицы>> "))
m2 = []
current = m2_start
for i in range(m2_rows):
    row = []
    for j in range(m2_cols):
        row.append(current)
        current += 1
    m2.append(row)

M1 = Matrix(m1)
M2 = Matrix(m2)


print("\nСложение:")
M1.add(M2).print()

print("\nВычитание:")
M1.subtract(M2).print()

print("\nУмножение:")
M1.multiply(M2).print()
