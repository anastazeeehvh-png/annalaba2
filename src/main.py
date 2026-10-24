"""Диагонали матрицы: сравнение сумм главной и побочной диагоналей."""
import math


def main_diagonal_sum(matrix):
    """Сумма элементов главной диагонали."""
    return sum(matrix[i][i] for i in range(len(matrix)))


def anti_diagonal_sum(matrix):
    """Сумма элементов побочной диагонали."""
    n = len(matrix)
    return sum(matrix[i][n - 1 - i] for i in range(n))


def read_size():
    """Запрашивает размерность n (1..100) до корректного ввода."""
    while True:
        text = input("Введите размерность матрицы n (1..100): ").strip()
        try:
            n = int(text)
        except ValueError:
            print("Ошибка: n должно быть целым числом.")
            continue
        if 1 <= n <= 100:
            return n
        print("Ошибка: n должно быть в диапазоне от 1 до 100.")


def read_matrix(n):
    """Читает матрицу n x n построчно с проверкой ввода."""
    print("Введите элементы матрицы построчно (через пробел):")
    matrix = []
    while len(matrix) < n:
        parts = input().split()
        try:
            row = [float(p) for p in parts]
        except ValueError:
            print("Ошибка: элементы должны быть числами. Повторите ввод строки.")
            continue
        if len(row) != n or not all(math.isfinite(x) for x in row):
            print(f"Ошибка: нужно ввести ровно {n} конечных чисел (неверный элемент или количество). Повторите ввод строки.")
            continue
        matrix.append(row)
    return matrix


def main():
    n = read_size()
    matrix = read_matrix(n)
    print(f"Сумма элементов главной диагонали: {main_diagonal_sum(matrix):.2f}")
    print(f"Сумма элементов побочной диагонали: {anti_diagonal_sum(matrix):.2f}")


if __name__ == "__main__":
    main()
