"""Диагонали матрицы: сравнение сумм главной и побочной диагоналей."""
import math

EPS = 1e-9


def main_diagonal_sum(matrix):
    """Сумма элементов главной диагонали."""
    return sum(matrix[i][i] for i in range(len(matrix)))


def anti_diagonal_sum(matrix):
    """Сумма элементов побочной диагонали."""
    n = len(matrix)
    return sum(matrix[i][n - 1 - i] for i in range(n))


def compare_sums(main_sum, anti_sum):
    """Сравнивает суммы диагоналей и возвращает текст результата."""
    if abs(main_sum - anti_sum) <= EPS:
        return "Суммы диагоналей равны"
    if main_sum > anti_sum:
        return "Сумма главной диагонали больше суммы побочной"
    return "Сумма главной диагонали меньше суммы побочной"


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
    s_main = main_diagonal_sum(matrix)
    s_anti = anti_diagonal_sum(matrix)
    print(f"Сумма элементов главной диагонали: {s_main:.2f}")
    print(f"Сумма элементов побочной диагонали: {s_anti:.2f}")
    print(compare_sums(s_main, s_anti))


if __name__ == "__main__":
    main()
