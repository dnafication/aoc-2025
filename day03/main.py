import os


def solve_part1(lines):
    print("Solving Part 1")
    largest_number_list = []
    for line in lines:
        first_digit, first_digit_position = 0, 0
        second_digit = 0
        for i in range(len(line.strip()) - 1):
            if int(line[i]) > first_digit:
                first_digit = int(line[i])
                first_digit_position = i
        for j in range(first_digit_position + 1, len(line.strip())):
            if int(line[j]) > second_digit:
                second_digit = int(line[j])
        largest_number_list.append(int(f"{first_digit}{second_digit}"))

    total_largest_number = sum(largest_number_list)
    print(f"Total largest number from all lines: {total_largest_number}")


def pick_largest_digit(digits, start_index, end_index):
    largest_digit = -1
    largest_index = -1
    for i in range(start_index, end_index + 1):
        if digits[i] > largest_digit:
            largest_digit = digits[i]
            largest_index = i
    return largest_digit, largest_index


# Part 2: Now I need to pick twelve digits to form the largest possible number
def solve_part2(lines):
    print("Solving Part 2")
    largest_number_list = []
    for line in lines:
        digits = [int(d) for d in line.strip()]
        index = 0
        selected_digits = []
        for i in range(12):
            max_possible_index = len(digits) - (12 - (i))
            largest_digit, largest_index = pick_largest_digit(
                digits, index, max_possible_index
            )
            selected_digits.append(largest_digit)
            index = largest_index + 1
        largest_number_list.append(int("".join(map(str, selected_digits))))
    total_largest_number = sum(largest_number_list)
    print(f"Total largest number from all lines: {total_largest_number}")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Replace with text.txt for testing with smaller input
    with open(os.path.join(script_dir, "input.txt"), "r") as f:
        lines = f.readlines()
        solve_part1(lines)
        solve_part2(lines)


if __name__ == "__main__":
    main()
