import os
import numpy as np
from functools import reduce


def solve_part1(grid: np.ndarray):
    print("Solving Part 1")
    grid = np.transpose(grid)
    total = 0
    for row in grid:
        op = row[-1]
        numbers = list(map(int, row[:-1]))
        if op == "+":
            total += reduce(lambda x, y: x + y, numbers)
        elif op == "*":
            total += reduce(lambda x, y: x * y, numbers)
    print("Total:", total)


def solve_part2(lines: list[str]):
    print("Solving Part 2")
    # evaluate all lines together in reverse order: right to left character by character
    total = 0
    l = zip(*lines)
    l = list(l)  # remove last line
    l = l[::-1]  # reverse
    # print(l)

    curr_list_of_numbers: list[int] = []
    for col in l:
        op = col[-1]
        digits = [x for x in col[:-1] if x.isdigit()]
        digits = "".join(digits)
        if not digits:
            curr_list_of_numbers = []
            continue
        curr_list_of_numbers.append(int(digits))
        if op == "+":
            total += reduce(lambda x, y: x + y, curr_list_of_numbers)
        elif op == "*":
            total += reduce(lambda x, y: x * y, curr_list_of_numbers)

    print("Total:", total)


def parse_input(lines: list[str]) -> np.ndarray:
    data = [line.split() for line in lines]
    data = np.array(data)
    return data


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Replace with text.txt for testing with smaller input
    with open(os.path.join(script_dir, "input.txt"), "r", encoding="utf-8") as f:
        lines = f.readlines()
        data = parse_input(lines)
        solve_part1(data.copy())
        solve_part2(lines)  # parsing input needs a different way for part 2


if __name__ == "__main__":
    main()
