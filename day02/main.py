import os


def is_invalid_id(ID: str) -> bool:
    if len(ID) % 2 != 0:
        return False
    if ID[: len(ID) // 2] != ID[len(ID) // 2 :]:
        return False
    return True


def solve_part1(lines):
    print("Solving Part 1")
    ranges = lines[0].strip().split(",")
    invalid_ids = []
    for r in ranges:
        start, end = map(int, r.split("-"))
        for number in range(start, end + 1):
            if is_invalid_id(str(number)):
                invalid_ids.append(number)

    # print("Invalid IDs:")
    # print(invalid_ids)
    print(f"Total invalid IDs: {len(invalid_ids)}")
    print(f"Sum of invalid IDs: {sum(invalid_ids)}")


def is_invalid_id_part2(ID: str) -> bool:
    n = len(ID)
    for pattern_len in range(1, n):
        if n % pattern_len == 0:  # if divisible by pattern len
            pattern = ID[:pattern_len]
            if pattern * (n // pattern_len) == ID:
                return True

    return False


def solve_part2(lines):
    print("Solving Part 2")
    ranges = lines[0].strip().split(",")
    invalid_ids = []
    for r in ranges:
        start, end = map(int, r.split("-"))
        for n in range(start, end + 1):
            if is_invalid_id_part2(str(n)):
                invalid_ids.append(n)

    print(f"Total invalid IDs: {len(invalid_ids)}")
    print(f"Sum of invalid IDs: {sum(invalid_ids)}")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Replace with text.txt for testing with smaller input
    with open(os.path.join(script_dir, "input.txt"), "r", encoding="utf-8") as f:
        lines = f.readlines()
        solve_part1(lines)
        solve_part2(lines)


if __name__ == "__main__":
    main()
