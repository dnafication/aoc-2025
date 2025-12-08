import os
import numpy as np


def solve_part1(grid: np.ndarray):
    print("Solving Part 1")
    print(grid)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            current = grid[i, j]
            bottom = grid[i + 1, j] if i < grid.shape[0] - 1 else None
            bottom_left = (
                grid[i + 1, j - 1] if i < grid.shape[0] - 1 and j > 0 else None
            )
            bottom_right = (
                grid[i + 1, j + 1]
                if i < grid.shape[0] - 1 and j < grid.shape[1] - 1
                else None
            )

            if current == "S" or current == "|":
                # Set bottom cells to '|'
                if bottom is not None and bottom != "^":
                    grid[i + 1, j] = "|"
            if current == "^":
                # Set bottom-left and bottom-right cells to '|'
                if bottom_left is not None:
                    grid[i + 1, j - 1] = "|"
                if bottom_right is not None:
                    grid[i + 1, j + 1] = "|"

    # Find the number of '^' with '|' directly above them
    count = 0
    for i in range(1, grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == "^" and grid[i - 1, j] == "|":
                count += 1

    print(f"Number of time the beam is split: {count}")


def solve_part2(grid: np.ndarray):
    print("Solving Part 2")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Replace with text.txt for testing with smaller input
    with open(os.path.join(script_dir, "test.txt"), "r", encoding="utf-8") as f:
        lines = f.readlines()
        grid = np.array([list(line.strip()) for line in lines])
        solve_part1(grid.copy())
        solve_part2(grid.copy())


if __name__ == "__main__":
    main()
