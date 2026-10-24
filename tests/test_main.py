import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import main  # noqa: E402


class TestDiagonalSums(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(main.main_diagonal_sum([[5.0]]), 5.0)
        self.assertEqual(main.anti_diagonal_sum([[5.0]]), 5.0)

    def test_three_by_three(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 10]]
        self.assertEqual(main.main_diagonal_sum(m), 16)
        self.assertEqual(main.anti_diagonal_sum(m), 15)

    def test_negative_values(self):
        m = [[-1.5, 2], [3, -4]]
        self.assertEqual(main.main_diagonal_sum(m), -5.5)
        self.assertEqual(main.anti_diagonal_sum(m), 5)


class TestCompare(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(main.compare_sums(5, 5), "Суммы диагоналей равны")

    def test_greater(self):
        self.assertEqual(main.compare_sums(16, 15),
                         "Сумма главной диагонали больше суммы побочной")

    def test_less(self):
        self.assertEqual(main.compare_sums(-5.5, 5),
                         "Сумма главной диагонали меньше суммы побочной")


if __name__ == "__main__":
    unittest.main()
