import os
import numpy as np


def get_adjacent_neighbors(grid, row, col):
    neighbors = []
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]:
            neighbors.append(grid[r, c])
    return neighbors


def move_rolls(grid):
    moved = 0
    positions_removed = []
    for (row, col), value in np.ndenumerate(grid):
        # print(f"Position ({row}, {col}): '{value}'")
        if value == "@":
            neighbors = get_adjacent_neighbors(grid, row, col)
            count_of_rolls = neighbors.count("@")
            # print(f"  Adjacent '@' count: {count_of_rolls}")
            if count_of_rolls < 4:
                positions_removed.append((row, col))
                moved += 1
    for row, col in positions_removed:
        grid[row, col] = "."
    # print(grid)
    return moved, grid


def solve_part1(grid):
    print("Solving Part 1")
    total_moved, _ = move_rolls(grid)
    print(f"Total moved: {total_moved}")


# Keep moving '@' until no more can move
def solve_part2(grid):
    print("Solving Part 2")
    total_moved = 0
    while True:
        current_moved, grid = move_rolls(grid)
        total_moved += current_moved
        print(f"Moved this round: {current_moved}")
        if current_moved == 0:
            break
    print("Total moved:", total_moved)


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Replace with text.txt for testing with smaller input
    with open(os.path.join(script_dir, "input.txt"), "r", encoding="utf-8") as f:
        lines = f.readlines()
        grid = np.array([list(line.strip()) for line in lines])
        solve_part1(grid.copy())
        solve_part2(grid.copy())


if __name__ == "__main__":
    main()
