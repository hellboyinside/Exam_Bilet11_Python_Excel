# -*- coding: utf-8 -*-
"""
Екзаменаційний білет №11
Задача 1.

Дано двовимірний масив 22×2.
Знайти номери двох сусідніх рядків,
сума елементів в яких максимальна.
Відсортувати кожен рядок масиву за спаданням (функція).
"""

from typing import List, Tuple


def sort_row_desc(row: List[int]) -> List[int]:
    """Сортує елементи рядка за спаданням."""
    return sorted(row, reverse=True)


def find_max_adjacent_rows(matrix: List[List[int]]) -> Tuple[int, int]:
    """Повертає номери (1-based) двох сусідніх рядків з максимальною сумою."""
    max_sum = sum(matrix[0]) + sum(matrix[1])
    idx = 0

    for i in range(1, len(matrix) - 1):
        s = sum(matrix[i]) + sum(matrix[i + 1])
        if s > max_sum:
            max_sum = s
            idx = i

    return idx + 1, idx + 2


def main():
    # Приклад масиву 22×2
    matrix = [
        [5, 12], [7, 3], [9, 4], [2, 10], [6, 8],
        [1, 14], [11, 0], [13, 2], [4, 9], [8, 6],
        [7, 7], [10, 5], [3, 11], [12, 1], [6, 9],
        [2, 13], [14, 0], [5, 8], [9, 6], [7, 4],
        [10, 2], [1, 15]
    ]

    r1, r2 = find_max_adjacent_rows(matrix)

    print(f"Номери сусідніх рядків з максимальною сумою: {r1} і {r2}")
    print("Відсортований масив:")

    for row in matrix:
        print(sort_row_desc(row))


if __name__ == "__main__":
    main()
