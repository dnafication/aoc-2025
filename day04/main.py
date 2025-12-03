import os


def solve_part1(lines):
    print("Solving Part 1")


def solve_part2(lines):
    print("Solving Part 2")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Replace with text.txt for testing with smaller input
    with open(os.path.join(script_dir, "input.txt"), "r", encoding="utf-8") as f:
        lines = f.readlines()
        solve_part1(lines)
        solve_part2(lines)


if __name__ == "__main__":
    main()
