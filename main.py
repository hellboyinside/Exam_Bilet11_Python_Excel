
"""
Екзаменаційний білет №11
Задача 1 (Python):
- Дано двовимірний масив 22×2.
- Знайти номери двох сусідніх рядків, сума елементів в яких максимальна.
- Відсортувати кожен рядок масиву за спаданням (функція).
"""

from __future__ import annotations
from typing import List, Tuple


def sort_row_desc(row: List[int]) -> List[int]:
    """Сортує елементи рядка за спаданням і повертає новий список."""
    return sorted(row, reverse=True)


def row_sum(row: List[int]) -> int:
    """Повертає суму елементів рядка."""
    return sum(row)


def find_max_adjacent_rows(matrix: List[List[int]]) -> Tuple[int, int, int]:
    """
    Знаходить два сусідні рядки з максимальною сумою елементів.
    Повертає: (idx1, idx2, max_sum) де idx1/idx2 — індекси (0-based).
    """
    if len(matrix) < 2:
        raise ValueError("Масив має містити щонайменше 2 рядки.")
    if any(len(r) != 2 for r in matrix):
        raise ValueError("Кожен рядок має містити рівно 2 елементи (2 стовпці).")


  
    max_sum = row_sum(matrix[0]) + row_sum(matrix[1])
    idx1 = 0

    
    for i in range(1, len(matrix) - 1):
        s = row_sum(matrix[i]) + row_sum(matrix[i + 1])
        if s > max_sum:
            max_sum = s
            idx1 = i

    return idx1, idx1 + 1, max_sum


def read_matrix_22x2() -> List[List[int]]:
    """Зчитує матрицю 22×2 з клавіатури (44 числа)."""
    print("Введіть 44 цілі числа для масиву 22×2 (по 2 числа в рядку):")
    matrix: List[List[int]] = []
    for r in range(22):
        while True:
            try:
                parts = input(f"Рядок {r + 1} (2 числа через пробіл): ").strip().split()
                if len(parts) != 2:
                    print("Потрібно рівно 2 числа. Спробуйте ще раз.")
                    continue
                row = [int(parts[0]), int(parts[1])]
                matrix.append(row)
                break
            except ValueError:
                print("Помилка: введіть саме цілі числа. Спробуйте ще раз.")
    return matrix


def main() -> None:
   
    mode = input("Оберіть режим: i — введення з клавіатури, d — приклад за замовчуванням [d]: ").strip().lower()
    if mode == "i":
        matrix = read_matrix_22x2()
    else:
        
        matrix = [
            [5, 12], [7, 3], [9, 4], [2, 10], [6, 8],
            [1, 14], [11, 0], [13, 2], [4, 9], [8, 6],
            [7, 7], [10, 5], [3, 11], [12, 1], [6, 9],
            [2, 13], [14, 0], [5, 8], [9, 6], [7, 4],
            [10, 2], [1, 15],
        ]

    
    idx_a, idx_b, max_s = find_max_adjacent_rows(matrix)
    sorted_matrix = [sort_row_desc(row) for row in matrix]

 
    print("\nРезультати:")
    print(f"Максимальна сума двох сусідніх рядків = {max_s}")
    print(f"Номери сусідніх рядків з максимальною сумою: {idx_a + 1} та {idx_b + 1}\n")

    print("Відсортований масив (кожен рядок за спаданням):")
    for r, row in enumerate(sorted_matrix, start=1):
        print(f"{r:>2}: {row}")


if __name__ == "__main__":
    main()
