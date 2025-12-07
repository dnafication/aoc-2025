import os


def solve_part1(lines):
    print("Solving Part 1")
    id_ranges, ids = parse_input(lines)
    # Find all IDs that are in the ranges inclusive
    fresh_ids = set()
    for i in ids:
        for r in id_ranges:
            if r[0] <= i <= r[1]:
                fresh_ids.add(i)
                break
    print("Number of fresh IDs:", len(fresh_ids))


def solve_part2(lines):
    print("Solving Part 2")
    id_ranges, _ = parse_input(lines)
    all_possible_ids = set()

    # ** Tried the following but it was too slow for the full input
    # min number in the id ranges
    # min_id = min(r[0] for r in id_ranges)
    # max_id = max(r[1] for r in id_ranges)
    # print("ID range:", min_id, "to", max_id)
    # for i in range(min_id, max_id + 1):
    #     for r in id_ranges:
    #         if r[0] <= i <= r[1]:
    #             all_possible_ids.add(i)
    #             break

    # ** Let's try merging the ranges which overlap or are contiguous
    sorted_ranges = sorted(id_ranges, key=lambda x: x[0])
    merged_ranges = []
    current_start, current_end = sorted_ranges[0]
    for r in sorted_ranges[1:]:
        if r[0] <= current_end:  # Overlapping or contiguous
            current_end = max(current_end, r[1])
        else:
            merged_ranges.append((current_start, current_end))
            current_start, current_end = r
    merged_ranges.append((current_start, current_end))

    total_ids = 0
    for r in merged_ranges:
        total_ids += r[1] - r[0] + 1

    print("Total possible fresh IDs in ranges:", total_ids)


def parse_input(lines):
    separator_index = lines.index("\n")
    id_ranges = lines[:separator_index]
    id_ranges = [r.strip() for r in id_ranges]
    id_ranges = [tuple(map(int, r.split("-"))) for r in id_ranges]
    ids = lines[separator_index + 1 :]
    ids = [int(i.strip()) for i in ids]
    # print("id_ranges", id_ranges)
    # print("ids", ids)
    return id_ranges, ids


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Replace with text.txt for testing with smaller input
    with open(os.path.join(script_dir, "input.txt"), "r", encoding="utf-8") as f:
        lines = f.readlines()
        solve_part1(lines)
        solve_part2(lines)


if __name__ == "__main__":
    main()
